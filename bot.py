import re
import requests
from bs4 import BeautifulSoup
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from db import insert_product, get_all_products, update_price, delete_all_products, update_product_name
from config import TELEGRAM_BOT_TOKEN, CHAT_ID

# ---------- SCRAPERS ----------

def get_price_amazon(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-IN,en;q=0.9"}
        res = requests.get(url, headers=headers, timeout=20)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        title_tag = soup.select_one("#productTitle")
        title = title_tag.get_text(strip=True) if title_tag else "Unknown Product"
        candidates = [
            soup.select_one("#priceblock_ourprice"),
            soup.select_one("#priceblock_dealprice"),
            soup.select_one(".a-price .a-offscreen"),
            soup.select_one("#sns-base-price"),
        ]
        price = None
        for tag in candidates:
            if tag:
                cleaned = re.sub(r"[^0-9.]", "", tag.get_text())
                if cleaned:
                    price = float(cleaned)
                    break
        return title, price
    except Exception as e:
        print(f"Error fetching Amazon price: {e}")
        return None, None

def get_price_flipkart(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-IN,en;q=0.9"}
        res = requests.get(url, headers=headers, timeout=20)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        title_tag = soup.select_one("span.B_NuCI")
        title = title_tag.get_text(strip=True) if title_tag else "Unknown Product"
        price_tag = soup.select_one("div._30jeq3._16Jk6d")
        price = None
        if price_tag:
            cleaned = re.sub(r"[^0-9.]", "", price_tag.get_text())
            if cleaned:
                price = float(cleaned)
        return title, price
    except Exception as e:
        print(f"Error fetching Flipkart price: {e}")
        return None, None

def get_price(url):
    if "amazon" in url:
        return get_price_amazon(url)
    elif "flipkart" in url:
        return get_price_flipkart(url)
    else:
        print("Unsupported site:", url)
        return None, None

# ---------- ALERT SENDER ----------

async def send_price_message(title, price, url):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    text = f"✅ Price drop!\n\n{title}\nCurrent Price: ₹{price}\n\n{url}"
    await bot.send_message(chat_id=CHAT_ID, text=text)

# ---------- PRICE CHECK ----------

async def check_prices(context: ContextTypes.DEFAULT_TYPE):
    products = get_all_products()
    for product in products:
        title, current_price = get_price(product["url"])
        if not title or current_price is None:
            continue
        update_product_name(product["id"], title)
        update_price(product["id"], current_price)
        if current_price <= product["target_price"]:
            await send_price_message(title, current_price, product["url"])

# ---------- BOT COMMANDS ----------

def is_valid_url(url):
    return url.startswith("http") and ("amazon" in url or "flipkart" in url)

async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage: /track <product_url> <target_price>")
        return
    url = args[0]
    try:
        target_price = float(args[1])
    except ValueError:
        await update.message.reply_text("Please provide a valid target price.")
        return
    if not is_valid_url(url):
        await update.message.reply_text("URL must be an Amazon or Flipkart product.")
        return

    title, current_price = get_price(url)
    if not title or current_price is None:
        await update.message.reply_text("Failed to fetch product details. Try again later.")
        return

    insert_product(title, url, target_price, current_price)
    await update.message.reply_text(f"✅ Tracking!\n{url}\nTarget Price: ₹{target_price}\nCurrent Price: ₹{current_price}")

    if current_price <= target_price:
        await send_price_message(title, current_price, url)

async def list_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    products = get_all_products()
    if not products:
        await update.message.reply_text("No products being tracked.")
        return
    text = "📦 Tracked Products:\n" + "\n".join(
        f"{p['id']}: {p['url']} (Target: ₹{p['target_price']}, Last: ₹{p['last_price']})"
        for p in products
    )
    await update.message.reply_text(text)

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    delete_all_products()
    await update.message.reply_text("🗑️ All tracked products have been deleted.")

# ---------- MAIN ----------

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("track", track))
    app.add_handler(CommandHandler("list", list_products))
    app.add_handler(CommandHandler("clear", clear))

    # Scheduler: check prices every 30 minutes
    app.job_queue.run_repeating(check_prices, interval=1800, first=5)

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

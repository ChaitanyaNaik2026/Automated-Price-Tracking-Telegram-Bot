import asyncio
from config import TELEGRAM_BOT_TOKEN
from telegram import Bot

# ✅ Your actual chat ID
CHAT_ID = 1717756634

async def send_message():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="✅ Hello from SmartSaver bot! Your Telegram is now connected.")

asyncio.run(send_message())


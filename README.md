# 🤖 Automated Price Tracking Telegram Bot

Automated Price Tracking Telegram Bot is a Python project that tracks product prices on **Amazon** and **Flipkart**.  
It stores products in a **MySQL database**, checks prices automatically, and sends **Telegram alerts** when the price falls below your target.

---

## 🚀 Features
- Track multiple products from Amazon & Flipkart.
- Store & update prices in MySQL.
- Automatic background checks every 30 minutes.
- Instant Telegram alerts on price drops.
- Easy-to-use commands.

---

## 📂 Project Structure
```
Automated-Price-Tracking-Telegram-Bot/
│── bot.py              # Main bot logic (commands, scheduler, alerts)
│── db.py               # Database helper functions
│── init_db.py          # Initializes MySQL database & tables
│── test_bot.py         # Tests Telegram bot connection
│── config.example.py   # Example config (edit & rename to config.py)
│── requirements.txt    # Dependencies
│── .gitignore          # Ignores config.py, venv, cache files
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Automated-Price-Tracking-Telegram-Bot.git
cd Automated-Price-Tracking-Telegram-Bot
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the Project
- Copy `config.example.py` → `config.py`
- Add your credentials:

```python
# MySQL database
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "smartsaver"

# Telegram bot
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

⚠️ **Note:** `config.py` is ignored in GitHub (`.gitignore`) to keep your credentials; your Token and ID safe.  

---

## 🤖 Get Telegram Bot Token & Chat ID

1. Open Telegram → search `@BotFather`.  
2. Run `/newbot` and copy the generated **Bot Token**.  
3. Send a message to your new bot in Telegram.  
4. Run:
   ```bash
   python test_bot.py
   ```
   → It will print your **Chat ID**.  

Add both values in `config.py`.  

---

## 🛠️ How It Works
1. Bot scrapes product price using **Requests** + **BeautifulSoup4**.  
2. Data is stored in **MySQL** via `db.py`.  
3. A background **scheduler (APScheduler)** checks prices every 30 minutes.  
4. If current price ≤ target, bot sends a **Telegram notification**.  

---

## 📌 Commands
- `/track <url> <price>` → Start tracking a product.  
- `/list` → Show all tracked products.  
- `/clear` → Remove all tracked products.  

---

## 📚 Libraries Used
- **python-telegram-bot** → Telegram integration.  
- **apscheduler** → Task scheduling.  
- **requests** → Fetch product HTML.  
- **beautifulsoup4** → Extract product details.  
- **mysql-connector-python** → Database operations.  

---

## ✅ Run the Bot
```bash
# Initialize database
python init_db.py

# Start bot
python bot.py
```

Now, in Telegram:
```
/track https://www.amazon.in/dp/XXXX 50000
-This gives a immediate notification if the price is below target or it saves the product in the database 
 and notify whenever the price drops below target

/list
 -This gives the list of products whose prices are being monitored.

/clear
 - Clears the list/products in the database to start fresh search.

## 📖 Project Summary
The **Automated Price Tracking Telegram Bot** is a smart shopping assistant.  
It combines **web scraping, MySQL, Telegram API, and scheduling** to make sure you never miss a good deal.  
Simple, effective, and fully automated.

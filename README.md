# 🤖 Automated Price Tracking Telegram Bot

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-43B02A?style=for-the-badge&logo=python&logoColor=white)
![APScheduler](https://img.shields.io/badge/APScheduler-FF6F00?style=for-the-badge&logo=clockify&logoColor=white)
![Amazon](https://img.shields.io/badge/Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white)
![Flipkart](https://img.shields.io/badge/Flipkart-2874F0?style=for-the-badge&logo=flipkart&logoColor=white)

Automated Price Tracking Telegram Bot is a Python project that tracks product prices on **Amazon** and **Flipkart**.
It stores products in a **MySQL database**, checks prices automatically, and sends **Telegram alerts** when the price falls below your target.

---

## 🚀 Features

✅ Track multiple products from Amazon & Flipkart

✅ Store & update prices in MySQL

✅ Automatic background checks every 30 minutes

✅ Instant Telegram alerts on price drops

✅ Easy-to-use bot commands

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

Copy `config.example.py` → `config.py` and add your credentials:

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

> ⚠️ **Note:** `config.py` is listed in `.gitignore` to keep your Token and Chat ID safe — it will never be pushed to GitHub.

---

## 🤖 Get Telegram Bot Token & Chat ID

1. Open Telegram → search `@BotFather`
2. Run `/newbot` and copy the generated **Bot Token**
3. Send a message to your new bot in Telegram
4. Run the test script:
   ```bash
   python test_bot.py
   ```
   → It will print your **Chat ID**
5. Add both values in `config.py`

---

## 🛠️ How It Works

1. Bot scrapes product price using ![Requests](https://img.shields.io/badge/Requests-2CA5E0?style=flat-square&logo=python&logoColor=white) + ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-43B02A?style=flat-square&logo=python&logoColor=white)
2. Data is stored in ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white) via `db.py`
3. A background ![APScheduler](https://img.shields.io/badge/APScheduler-FF6F00?style=flat-square&logo=clockify&logoColor=white) checks prices every **30 minutes**
4. If current price ≤ target, bot sends a ![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white) notification instantly

---

## 📌 Bot Commands

| Command | Description |
|---|---|
| `/track <url> <price>` | Start tracking a product at your target price |
| `/list` | Show all currently tracked products |
| `/clear` | Remove all tracked products and start fresh |

---

## 📚 Libraries Used

![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![APScheduler](https://img.shields.io/badge/APScheduler-FF6F00?style=for-the-badge&logo=clockify&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-43B02A?style=for-the-badge&logo=python&logoColor=white)
![MySQL Connector](https://img.shields.io/badge/mysql--connector--python-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

| Library | Purpose |
|---|---|
| `python-telegram-bot` | Telegram bot integration |
| `apscheduler` | Background task scheduling |
| `requests` | Fetch product HTML pages |
| `beautifulsoup4` | Parse and extract product details |
| `mysql-connector-python` | MySQL database operations |

---

## ✅ Run the Bot

```bash
# Step 1: Initialize the database
python init_db.py

# Step 2: Start the bot
python bot.py
```

### Example Usage in Telegram

```
/track https://www.amazon.in/dp/XXXX 50000
```
> Sends an immediate alert if the price is already below target, or saves the product and notifies you whenever it drops.

```
/list
```
> Shows all products currently being monitored.

```
/clear
```
> Clears all tracked products from the database to start a fresh search.

---

## 📖 Project Summary

The **Automated Price Tracking Telegram Bot** is a smart shopping assistant.
It combines **web scraping**, **MySQL**, **Telegram API**, and **APScheduler** to make sure you never miss a great deal.
Simple, effective, and fully automated.

---

## 👨‍💻 Developer

**Chaitanya Naik**

[![GitHub](https://img.shields.io/badge/GitHub-ChaitanyaNaik2026-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ChaitanyaNaik2026)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-naikchaitanya-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/naikchaitanya)

---

## ⚠️ Disclaimer

This project is intended for **educational purposes only**. Web scraping may violate the Terms of Service of Amazon and Flipkart. Use responsibly and at your own risk.

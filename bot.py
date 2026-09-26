import os
from flask import Flask
from threading import Thread
import telegram
from telegram.ext import ApplicationBuilder, CommandHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is active!", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

Thread(target=run_flask).start()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    welcome_text = (
        "👋 Welcome to My Trading Pocket Bot!\n\n"
        "Your bot is online and active 24/7."
    )
    await update.message.reply_text(welcome_text)

if __name__ == '__main__':
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.run_polling()

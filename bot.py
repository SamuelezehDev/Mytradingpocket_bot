import os
from flask import Flask
from threading import Thread
import telegram
from telegram.ext import ApplicationBuilder, CommandHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is active!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

Thread(target=run_flask).start()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Trading signal bot is running!")

if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

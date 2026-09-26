import os
import random
from flask import Flask
from threading import Thread
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is active!", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

Thread(target=run_flask).start()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Command handler for /start
async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("12 SEC 🟢 AUD/CAD OTC", callback_data='signal_12s')],
        [InlineKeyboardButton("8 SEC 🟢 AUD/CAD OTC", callback_data='signal_8s')],
        [InlineKeyboardButton("5 SEC 🟢 AUD/CAD OTC", callback_data='signal_5s')],
        [InlineKeyboardButton("Back", callback_data='back'), InlineKeyboardButton("Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select an option:", reply_markup=reply_markup)

# Handler for button clicks
async def button_click(update, context):
    query = update.callback_query
    await query.answer()

    if query.data in ['signal_12s', 'signal_8s', 'signal_5s']:
        timeframe = "5 SEC" if query.data == 'signal_5s' else ("8 SEC" if query.data == 'signal_8s' else "12 SEC")
        direction = random.choice(["CALL ⬆️", "PUT ⬇️"])
        
        signal_msg = (
            f"⚡ **SIGNAL GENERATED** ⚡\n\n"
            f"Asset: **AUD/CAD OTC**\n"
            f"Timeframe: **{timeframe}**\n"
            f"Action: **{direction}**"
        )
        
        # Re-attach menu buttons under signal output
        keyboard = [
            [InlineKeyboardButton("12 SEC 🟢 AUD/CAD OTC", callback_data='signal_12s')],
            [InlineKeyboardButton("8 SEC 🟢 AUD/CAD OTC", callback_data='signal_8s')],
            [InlineKeyboardButton("5 SEC 🟢 AUD/CAD OTC", callback_data='signal_5s')],
            [InlineKeyboardButton("Back", callback_data='back'), InlineKeyboardButton("Main Menu", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.reply_text(signal_msg, parse_mode='Markdown', reply_markup=reply_markup)

if __name__ == '__main__':
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CallbackQueryHandler(button_click))
    app_bot.run_polling()

import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# 1. DEFINE KEYBOARD LAYOUT
# Notice how 'Back' and 'Main Menu' are together in the last array row
MENU_KEYBOARD = [
    [KeyboardButton("12 SEC 🟢 AUD/CAD OTC")],
    [KeyboardButton("8 SEC 🟢 AUD/CAD OTC")],
    [KeyboardButton("5 SEC 🟢 AUD/CAD OTC")],
    [KeyboardButton("Back"), KeyboardButton("Main Menu")]  # Side-by-side row
]

# Create the markup object
REPLY_MARKUP = ReplyKeyboardMarkup(MENU_KEYBOARD, resize_keyboard=True)

# 2. COMMAND HANDLERS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the signal menu when /start is issued."""
    await update.message.reply_text(
        "Welcome! Select an option below:",
        reply_markup=REPLY_MARKUP
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles button presses from the custom keyboard."""
    text = update.message.text

    if text == "12 SEC 🟢 AUD/CAD OTC":
        await update.message.reply_text("⚡ 12 SEC Signal Generated!")
    elif text == "8 SEC 🟢 AUD/CAD OTC":
        await update.message.reply_text("⚡ 8 SEC Signal Generated!")
    elif text == "5 SEC 🟢 AUD/CAD OTC":
        await update.message.reply_text("⚡ 5 SEC Signal Generated!")
    elif text == "Back":
        await update.message.reply_text("Going back...", reply_markup=REPLY_MARKUP)
    elif text == "Main Menu":
        await update.message.reply_text("Main Menu loaded.", reply_markup=REPLY_MARKUP)
    else:
        await update.message.reply_text("Please select a valid option.")

# 3. MAIN APPLICATION SETUP
def main() -> None:
    # Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token from BotFather
    TOKEN = "YOUR_BOT_TOKEN_HERE"

    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    # Run Bot
    application.run_polling()

if __name__ == "__main__":
    main()

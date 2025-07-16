import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m your Godfather automation bot.")

def run_bot():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN not found.")
        return

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot started...")
    app.run_polling()

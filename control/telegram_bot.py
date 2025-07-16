import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from godfather import handle_instruction

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text("I am the Godfather. What do you want to automate?")

def run(update, context):
    prompt = ' '.join(context.args)
    response = handle_instruction(prompt)
    update.message.reply_text(response)

def fallback(update, context):
    update.message.reply_text("Use /run followed by what you want.\nExample: /run grow my GitHub")

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("run", run))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, fallback))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
 

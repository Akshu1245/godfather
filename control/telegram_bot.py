from telegram.ext import Updater, CommandHandler
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def start(update, context):
    update.message.reply_text("I am your Godfather. Send /run followed by an idea.")

def run_command(update, context):
    prompt = ' '.join(context.args)
    if not prompt:
        update.message.reply_text("Please provide a task, like:\n/run write a YouTube script about AI")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content.strip()
        update.message.reply_text(answer[:4000])  # Telegram limit
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("run", run_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

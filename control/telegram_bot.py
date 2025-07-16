import httpx
import os
import time
import openai

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

openai.api_key = OPENAI_KEY

def send_message(chat_id, text):
    httpx.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": text})

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    if offset:
        url += f"?offset={offset}"
    try:
        response = httpx.get(url).json()
        return response["result"]
    except Exception:
        return []

def run_bot():
    last_update_id = None
    print("Bot started...")
    while True:
        updates = get_updates(last_update_id)
        for update in updates:
            last_update_id = update["update_id"] + 1
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")
                if text.startswith("/start"):
                    send_message(chat_id, "Godfather ready. Use /run <idea>")
                elif text.startswith("/run"):
                    prompt = text.replace("/run", "").strip()
                    if not prompt:
                        send_message(chat_id, "Send like this:\n/run Write YouTube script for AI tool")
                    else:
                        try:
                            res = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=[{"role": "user", "content": prompt}]
                            )
                            msg = res.choices[0].message.content.strip()
                            send_message(chat_id, msg[:4000])
                        except Exception as e:
                            send_message(chat_id, f"OpenAI Error: {str(e)}")
        time.sleep(2)

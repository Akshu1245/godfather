def run_bot():
    last_update_id = None
    print("Bot started...")
    while True:
        updates = get_updates(last_update_id)
        if updates:
            print("Got updates:", updates)  # 👈 this will log all incoming messages
        for update in updates:
            last_update_id = update["update_id"] + 1
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")
                print(f"User said: {text}")  # 👈 log user input
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

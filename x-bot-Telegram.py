import requests



def get_updates(bot_token, offset=None):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    params = {"offset": offset}
    response = requests.get(url, params=params) 
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text)
        return None

def send_message(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Error:", response.text)

def main():
    bot_token = ""
    chat_id=""  # Replace with the actual chat ID . -1002xxxxxx

    # Join the group (if not already joined)
    join_url = f"https://api.telegram.org/bot{bot_token}/joinChat"
    join_params = {"chat_id": chat_id}
    requests.get(join_url, params=join_params)

    offset = None
    while True:
        updates = get_updates(bot_token, offset)
        if updates:
            for update in updates['result']:
                if 'message' in update:
                    message = update['message']
                    chat_id = message['chat']['id']
                    text = message['text']

                    if text.startswith('/start'):
                        send_message(bot_token, chat_id, "Hello!")
                    else:
                        send_message(bot_token, chat_id, f"You sent: {text}")
                offset = update['update_id'] + 1
if __name__ == "__main__":
    main()
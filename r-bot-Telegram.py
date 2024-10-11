#pip install requests

import requests

bot_token = ""
chat_id = ""  # Replace with the chat ID where you want to send the message
text = "Hello V89 bot  Python! "

url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"


response = requests.post(url)

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Error sending message:", response.text)
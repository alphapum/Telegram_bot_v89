# %% [markdown]
# ## Telegram bot Notification 

# %%
# !pip install pyTelegramBotAPI

# %%
import telebot



# %%
# Replace 'YOUR_BOT_TOKEN' with your actual token
bot_token = ""
bot = telebot.TeleBot(bot_token)



# %%
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help' , '?'])
def help_message(message):
    bot.send_message(message.chat.id, "I can help you with...")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)



# %%
bot.infinity_polling()



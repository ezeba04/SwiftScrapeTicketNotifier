import telebot

API_KEY = '...'
bot = telebot.TeleBot(API_KEY)

def save_chat_id(chat_id):
    with open('chat_ids.txt', 'a+') as f:
        f.seek(0)
        if str(chat_id) not in f.read():
            f.write(str(chat_id) + '\n')

@bot.message_handler(commands=['start'])
def greet(message):
    save_chat_id(message.chat.id)
    bot.reply_to(message, "if you want to run the bot, please say /get_id")

@bot.message_handler(commands=['get_id'])
def hello(message):
    save_chat_id(message.chat.id)
    bot.send_message(message.chat.id, "Hello!")
    bot.send_message(message.chat.id, message.chat.id)
    print(message.chat.id)
    


bot.polling()


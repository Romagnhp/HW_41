import telebot

from secret import TOKEN

bot = telebot.TeleBot(TOKEN,  parse_mode=None) # TOKEN - ето ключ, который дает доступ к сервисам Telegram

@bot.message_handler(commands=['start', 'help'])
def send_my_massege(message):
    bot.reply_to(message, 'Hi how are you doing')

# запуск БОТА через вызов метода infinity_polling 
bot.infinity_polling()


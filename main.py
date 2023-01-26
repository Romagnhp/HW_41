import requests # модуль для создания запроса на какой-нибудь сайт 

import bs4 # модуль для парсинга

import sqlalchemy # модуль для реализации ORM

# импорт файла с классом для создания полей БД
from models.User import MyColunms, ParentClass

# модуль для доступа к обьекту Session
from sqlalchemy.orm import Session

# import telebot # модуль для создания бота в телеграм 
# from telebot import types
# from secret import TOKEN 

# создание БД
myEngine = sqlalchemy.create_engine('sqlite:///Famous_Physiks.db')
myConection = myEngine.connect()
# удаление полей БД
ParentClass.metadata.drop_all(myEngine)
# создание полей БД
ParentClass.metadata.create_all(myEngine)



myRequest = requests.get('http://cnr2.kent.edu/~manley/physicists.html')

myParser = bs4.BeautifulSoup(myRequest.text, 'html.parser')

serch = myParser.table
parsingList = serch.find_all(string=True)

editParsingList = [ i for i in parsingList if not '\n' in i]

editParsingList.pop(0)

print(editParsingList)


with Session(myEngine) as db:

    for i in range(0, len(editParsingList),3):
    
        row_n = MyColunms(
                    name = editParsingList[i],
                    years = editParsingList[i+1], 
                    major_achievements = editParsingList[i+2] 
                )
        # добавление строки со значениями в таблицу БД
        db.add(row_n) 
        db.commit()





# bot = telebot.TeleBot(TOKEN,  parse_mode=None) # TOKEN - ето ключ, который дает доступ к сервисам Telegram

# def creature_buttons(id):
#     markup = types.ReplyKeyboardMarkup()
#     itembtn1 = types.KeyboardButton('a')
#     itembtn2 = types.KeyboardButton('v')
#     itembtn3 = types.KeyboardButton('d')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.send_message(id, "Select", reply_markup=markup)


# @bot.message_handler(commands=['start', 'help']) # обработчик событий
# def send_my_massege(message):
#     # bot.reply_to(message, 'Hi how are you doing')
#     creature_buttons(message.chat.id)
    
# @bot.message_handler(content_types=['text']) # обработчик событий
# def response_text(message):
#     if (message.text == 'a'):
#         bot.send_message(message.chat.id, "qwerty")
#     elif (message.text == 'v'):
#         bot.send_message(message.chat.id, "asdf")
#     elif(message.text =='d'):
#         bot.send_message(message.chat.id, "zxcv")
#     else:
#         bot.send_message(message.chat.id, message.text)
    

# # запуск БОТА через вызов метода infinity_polling 
# bot.infinity_polling()


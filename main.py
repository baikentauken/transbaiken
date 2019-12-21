import telebot
from telebot import types
import config
from googletrans import Translator
from gtts import gTTS




bot=telebot.TeleBot(config.token)#активируем бота
@bot.message_handler(commands=['start'])#реагируем на команду старт
def start(message):
          keyboard=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
          button1=types.KeyboardButton('korean')
          button2=types.KeyboardButton('arabic')
          button3=types.KeyboardButton('italian')
          button4=types.KeyboardButton('chinese')
          keyboard.add(button1,button2,button3,button4)
          bot.send_message(message.chat.id,'выбери язык, на который хочешь перевести', reply_markup = keyboard)
          bot.register_next_step_handler_by_chat_id(message.chat.id,answer)
@bot.message_handler(content_types=['text'])#реагирует
def answer(message):
          if message.text == 'chinese':
                    bot.send_message(message.chat.id,'Введи текст и я его переведу на китайский')
                    bot.register_next_step_handler_by_chat_id(message.chat.id, cn)
          elif message.text == 'korean':
                    bot.send_message(message.chat.id,'Введи текст и я его переведу на корейский')
                    bot.register_next_step_handler_by_chat_id(message.chat.id, korean)
          elif message.text == 'italian':
                    bot.send_message(message.chat.id,'Введи текст и я его переведу на итальянский')
                    bot.register_next_step_handler_by_chat_id(message.chat.id, italian)
          elif message.text == 'arabic':
                    bot.send_message(message.chat.id,'Введи текст и я его переведу на арабский')
                    bot.register_next_step_handler_by_chat_id(message.chat.id, ar)
def cn(message):
          text=message.text
          transalator=Translator()
          trans=transalator.translate(text,dest='zh-cn')
          speech=gTTS(trans.text,'zh-cn')
          speech.save('transalatedtext.mp3')
          audio=open('transalatedtext.mp3','rb')
          bot.send_audio(message.chat.id,audio)
          keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
          button1= types.KeyboardButton('Узнать инстаграм')
          keyboard.add(button1)
          bot.send_message(message.chat.id, 'Хочешь узнать мой инстаграм? Жми на кнопку', reply_markup=keyboard)
          url(message)
def korean(message):
          text=message.text
          transalator=Translator()
          trans=transalator.translate(text,dest='ko')
          speech=gTTS(trans.text,'ko')
          speech.save('transalatedtext.mp3')
          audio=open('transalatedtext.mp3','rb')
          bot.send_audio(message.chat.id,audio)
          keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
          button1= types.KeyboardButton('Узнать инстаграм')
          keyboard.add(button1)
          bot.send_message(message.chat.id, 'Хочешь узнать мой инстаграм? Жми на кнопку', reply_markup=keyboard)
          url(message)
def italian(message):
          text=message.text
          transalator=Translator()
          trans=transalator.translate(text,dest='it')
          speech=gTTS(trans.text,'it')
          speech.save('transalatedtext.mp3')
          audio=open('transalatedtext.mp3','rb')
          bot.send_audio(message.chat.id,audio)
          keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
          button1= types.KeyboardButton('Узнать инстаграм')
          keyboard.add(button1)
          bot.send_message(message.chat.id, 'Хочешь узнать мой инстаграм? Жми на кнопку', reply_markup=keyboard)
          url(message)
def ar(message):
          text=message.text
          transalator=Translator()
          trans=transalator.translate(text,dest='ar')
          speech=gTTS(trans.text,'ar')
          speech.save('transalatedtext.mp3')
          audio=open('transalatedtext.mp3','rb')
          bot.send_audio(message.chat.id,audio)
          keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
          button1= types.KeyboardButton('Узнать инстаграм')
          keyboard.add(button1)
          bot.send_message(message.chat.id, 'Хочешь узнать мой инстаграм? Жми на кнопку', reply_markup=keyboard)
          url(message)
def url(message):
          if message.text== 'Узнать инстаграм':
                    keyboard=types.InlineKeyboardMarkup()
                    button=types.InlineKeyboardButton(text='перейти в инстаграм создателя',url='https://www.instagram.com/baikentauken1/?hl=ru')
                    keyboard.add(button)
                    bot.send_message(message.chat.id,'привет это аккаунт создателя',reply_markup=keyboard)
                    

bot.polling(none_stop=True)



import telebot
from languages import dict as lng
from languages import dic
import os
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

choice = lng.keys()
global mes,tolang
a=''
choicestr=""
mes=''
tolang=''


for i in choice:
	choicestr+=i+"\n"


def trans():
	global mes
	global tolang
	print(mes+' this is mes')
	print(tolang+' this is tolang')
	print('function is called')
	translator = Translator()
	text_to_translate = translator.translate(mes, src='en',dest=tolang.strip())
	global text
	global speak
	text = text_to_translate.text
	speak = gTTS(text=text, lang=tolang, slow=False)
	speak.save("captured_voice.mp3")


dicstr=str(dic)
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot("5748030465:AAEK9fhnZcNqhvyqEYJMBS_1AzXjG4oRcbA")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "this is a translator bot use /avaliable_langs to know about avaliable languages\nuse /shortcut to know about shortcuts of language /set_mes to set message and language and the use /recive to recive message")


@bot.message_handler(commands=['avaliable_langs'])
def send_welcome(message):
	bot.reply_to(message, choicestr)


@bot.message_handler(commands=['shortcut'])
def send_welcome(message):
	bot.reply_to(message, dicstr)



@bot.message_handler(commands=['set_mes'])
def something(message):
	bot.reply_to(message,'enter the message and after that keep \'_to_\' to enter the language')
	

@bot.message_handler(func=lambda msg: msg.text is not None and not msg.text.startswith('/'))
def test(message1):
		global mes
		global tolang
		text=message1.text
		lis=text.split('_to_')
		mes=lis[0].strip()
		tolang=lis[1].strip()		


@bot.message_handler(commands=['recive'])
def send_welcome(message):
	trans()
	bot.reply_to(message, text)
	bot.send_audio(message.chat.id,audio=open('captured_voice.mp3', 'rb'))
	os.remove('captured_voice.mp3')



bot.polling()

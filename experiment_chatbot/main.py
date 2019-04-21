from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
from espeak import espeak
import os



r = sr.Recognizer()
r.energy_threshold = 2100
espeak.set_voice("en")
bot = ChatBot('Test')

bot.set_trainer(ListTrainer)

for _files in os.listdir('files'):
	chats = open("files/"+_files,'r').readlines()

	bot.train(chats)
print("You can ask me anything")
while True:
	with sr.Microphone() as source:
    		audio = r.listen(source)
	word = r.recognize_google(audio)
	print("You : ",word)
	d = bot.get_response(word)
	s = str(d)
	#print(type(s))
	espeak.synth(s)
	print("Bot : ",d)

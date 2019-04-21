#from espeak import espeak
import subprocess

espeak.set_voice("en")


while 1 :
	d = input("what you want")
	espeak.synth(d)
	if d == "bye":
		exit()

while espeak.is_playing:
	pass


import speech_recognition as sr
import pyttsx3
 
# Record Audio
r = sr.Recognizer()
r.dynamic_energy_threshold=0
#r.energy_threshold = 2100
with sr.Microphone() as source:
    r.pause_threshold=1
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
    engine = pyttsx3.init()
    engine.say(source)
    engine.runAndWait()
 
# Speech recognition using Google Speech Recognition
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

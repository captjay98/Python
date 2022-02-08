import speech_recognition as sr
import speech
import time
from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
    print(phrase)


response = speech.input("Say something, please.")
speech.say("You said " + response)


def callback(phrase, listener):
    if phrase == "goodbye":
        listener.stoplistening()
    speech.say(phrase)


listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)

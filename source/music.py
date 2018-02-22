#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import pygame as pg
from time import ctime
import time
from gtts import gTTS

i=0

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    file1 = str("audio" + str(i) + ".mp3")
    tts.save(file1)
    pg.mixer.init()
    pg.mixer.music.load(file1)
    pg.mixer.music.play()
    #os.system("mpg321 audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "play" in data:
        #speak("Starting the music playing task")
        file2 = "C://Users//H//Desktop//(webmusic.in)_Breathless - Copy.mp3"
        pg.mixer.init()
        pg.mixer.music.load(file2)
        pg.mixer.music.play()

    if "pause" in data:
        #speak("Pausing")
        if pg.mixer.music.get_busy():
            pg.mixer.music.pause()

    if "resume" in data:
        #speak("Resuming")
        if pg.mixer.music.pause():
            pg.mixer.music.unpause()

    if "stop" in data:
        #speak("Stopping")
        if pg.mixer.music.get_busy():
            pg.mixer.music.stop()

    if "rewind" in data:
        #speak("Rewinding")
        pg.mixer.music.rewind()

# initialization
time.sleep(2)
speak("Hi Frank, what can I do for you?")
while 1:
    i=i+1
    data = recordAudio()
    jarvis(data)

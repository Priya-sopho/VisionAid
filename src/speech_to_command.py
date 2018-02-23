#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
# Try following commands for now: "what time is it", "how are you"

import speech_recognition as sr
import pygame as pg
import webbrowser
from time import ctime
import time
import os
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

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Chhavi, I will show you where " + location + " is.")
        url = '"https://www.google.nl/maps/place/"+ location'
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        #os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


# initialization
time.sleep(2)
speak("Hi Chhavi, what can I do for you?")
while 1:
    i=i+1
    data = recordAudio()
    jarvis(data)

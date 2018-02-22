#Run the following commands to install required libraries
	#1.Speech recognition
	# pip install SpeechRecognition
	#2.Google Search
	# pip install beautifulsoup4
	# pip install google
	#3.GUI 
	# pip install pyautogui

"""
	Following keys to be used for keyboard interrupts
	1. Visit a URL- Space
	2. Exit - q
	3. Skip current result - esc
	4. Bookmark - b
	5. Access Bookmarks - 
	6. Access History - 
	7. Google Search - f
"""
import threading,time 
import msvcrt
from pynput import keyboard
import os
import webbrowser as web
import io,json
import datetime
import win32com.client as wincl
voice = wincl.Dispatch("SAPI.SpVoice")

class webBrowser:
	def __init__(self):
		self.say("Welcome to Web Browsing")
		self.url = ""
		#Lock
		self.lock = threading.Lock()  #Initially pause is on
		kb = threading.Thread(target=self.listenKeyboard)
		kb.start()
		
	def listenKeyboard(self):
		with keyboard.Listener(on_press=self.onPress) as listener:
			listener.join()

	def onPress(self,key):
		while msvcrt.kbhit():
			msvcrt.getch()
		try:
			if key.char == 'q':
				self.exit()
			if key.char == 'b':
				self.createBookmark()
			if key.char == 'f':
				self.googleSearch()
		except AttributeError:
			if key == keyboard.Key.space:
				self.visitUrl()


	def say(self,line):
		#os.system("say {0}".format(line))
		voice.Speak(line)

	def listen(self,chunk_size=2048,say = "Say Something"):
		import speech_recognition as sr  
		r = sr.Recognizer()  
		with sr.Microphone(chunk_size=chunk_size) as source:  
			print("Please wait. Calibrating microphone...") 
			self.say("Please wait. Calibrating microphone...") 
			r.adjust_for_ambient_noise(source, duration=3)  
			print say  
			self.say(say)
			audio = r.listen(source) 
			try:  
				text = r.recognize_google(audio)
				if(text!=None):
					return text
				else:
					listen(chunk_size)
			except sr.UnknownValueError:  
				self.say("Google could not understand audio")
				print("Google could not understand audio") 
				listen(chunk_size)
			except sr.RequestError as e:  
				print("Google error; {0}".format(e)) 
				listen(chunk_size) 

	def exit(self):
		self.say("Exiting now")
		while msvcrt.kbhit():
			msvcrt.getch()
		os._exit(1)

	def visitUrl(self):
		self.lock.acquire()
		self.say("Visiting chosen result")
		web.open(self.result.link)
		createHistory()
		self.lock.release()

	def googleSearch(self):
		from google import google as web
		self.lock.acquire()
		self.say("Enter keywords to search")
		keyWords = raw_input()
		results = web.search(keyWords,1)
		self.lock.release()

		for self.result in results:
			self.lock.acquire()
			print "Name: ",self.result.name
			self.say(self.result.name)
			print "Description: ",self.result.description
			self.say(self.result.description)
			self.lock.release()
			print "----------------"


	#Create bookmarks, Web browser must be open and active
	def createBookmark(self):
		b = {}
		b["name"] = self.result.name
		b["url"] = self.result.link
		b["datetime"] = str(datetime.datetime.now())
		with open('bookmarks.txt', 'a+') as f:
  			json.dump(b, f, ensure_ascii=False)

	#Bookmarks exported to a file "bookmarks"
	# def accessBookmarks(self):
	def createHistory():
		h = {}
		h["name"] = self.result.name
		h["url"] = self.result.link
		h["datetime"] = str(datetime.datetime.now())
		with open('history.txt', 'a+') as f:
  			json.dump(h, f, ensure_ascii=False)
		

  	def accessHistory(self):
  		pass
  	def accessBookmark(self):
  		pass
		



instance = webBrowser()




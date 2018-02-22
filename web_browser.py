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
	1. Pause/Resume- Space
	2. Exit - q
	3. Reading bookmark/History - r
	4. Add Bookmark - b
	5. Google Search - f
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
		voice.Speak("Welcome to Web Browsing")
		self.url = ""
		self.googleData = None
		self.buffer = ["Press f to google search", "Press r to listen bookmark or history"]
		#Pause 
		self.pause_key = 0 #Initially pause is off
		#Lock
		self.lock = threading.Lock()  
		kb = threading.Thread(target=self.listenKeyboard)
		sp = threading.Thread(target=self.say)
		google = threading.Thread(target=self.googleSearchSpeak)
		kb.start()
		sp.start()
		google.start()

		
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
			if key.char == 'r':
				self.read()
		except AttributeError:
			if key == keyboard.Key.space and self.pause_key == 0:
				self.lock.acquire()
				self.pause_key = 1
				voice.Speak('Pausing')
				self.lock.release()
			elif key == keyboard.Key.space:				
				self.lock.acquire()
				self.pause_key = 0
				voice.Speak('Resuming')
				self.lock.release()
				
				

	
	def say(self):
		#os.system("say {0}".format(line))
		while True:
			self.lock.acquire()
			if self.pause_key == 0 and len(self.buffer) > 0:
				print len(self.buffer)
				line = self.buffer.pop()
				if len(line)!= 0:
					print line
					voice.Speak(line)
			self.lock.release()
			
	def listen(self,chunk_size=2048,say = "Say Something"):
		import speech_recognition as sr  
		r = sr.Recognizer()  
		with sr.Microphone(chunk_size=chunk_size) as source:  
			print("Please wait. Calibrating microphone...") 
			#self.say("Please wait. Calibrating microphone...") 
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
		voice.Speak("Exiting Web Browser")
		while msvcrt.kbhit():
			msvcrt.getch()
		os._exit(1)

	# def visitUrl(self):
	# 	self.lock.acquire()
	# 	self.say("Visiting chosen result")
	# 	web.open(self.result.link)
	# 	createHistory()
	# 	self.lock.release()

	def googleSearch(self):
		from google import google as web
		#self.lock.acquire()
		voice.Speak("Enter keywords to search")
		keyWords = raw_input()
		data = {'name': keyWords,'link': 'google.com'}
		self.createHistory(data)
		self.googleData = web.search(keyWords,1)
		print "End searching"


	def googleSearchSpeak(self):
		while True:
			if self.googleData is not None:
				for self.result in self.googleData:
					print('*'*4+str(len(self.buffer))+'*'*4)
					if len(self.buffer) == 0:
						#print "Name: ",self.result.name.encode('utf-8','ignore')
						#self.lock.acquire()
						self.buffer.insert(0,'Title' + self.result.name.encode('utf-8'))
						self.buffer.insert(0,'Description')
						#self.lock.release()
						desc = self.result.description.encode('utf-8','ignore').splitlines()
						#print "Description: ",desc
						#self.lock.acquire()
						for d in desc:
							self.buffer.insert(0,d)
					else:
						while(len(self.buffer)):
							pass
				self.buffer.insert(0,'Search completed.')
				self.googleData = None
			
		
		

	#Create bookmarks, Web browser must be open and active
	def createBookmark(self):
		b = {}
		b["name"] = self.result.name.encode('utf-8')
		b["url"] = self.result.link.encode('utf-8')
		b["created at"] = str(datetime.datetime.now())
		with open('bookmarks.txt', 'a+') as f:
  			json.dump(b, f, ensure_ascii=False)
  			f.write('\n')

	#Bookmarks exported to a file "bookmarks"
	# def accessBookmarks(self):
	def createHistory(self,result):
		h = {}
		h["visited at"] = str(datetime.datetime.now())
		h["name"] = result['name']
		h["url"] = result['link']
		with open('history.txt', 'a+') as f:
  			json.dump(h, f, ensure_ascii=False)
  			f.write('\n')

	def read(self):
		voice.Speak('Press 1 for bookmark and 2 for history')
		ch = int(raw_input())
		if ch == 1:
			self.accessBookmark()
		elif ch == 2:
			self.accessHistory()
		else:
			self.say('Invalid Choice! Exiting Bookmark or History Reading Task')


  	def accessHistory(self):
  		if self.googleData is not None:
  			self.buffer.insert(0,'Continuing google search speaking task')
  		with open('history.txt') as json_file: 
  			for data in json_file:
  				self.buffer.append(data)
		self.buffer.append('History Content')
  		print "End History Loading"
  				
  	def accessBookmark(self):
  		if self.googleData is not None:
  			self.buffer.insert(0,'Continuing google search speaking task')
  		with open('bookmarks.txt') as json_file: 
  			for data in json_file:
  				self.buffer.append(data)
		self.buffer.append('Bookmarks Content')
  		print "End Bookmarks Loading"
  		



instance = webBrowser()




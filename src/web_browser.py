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
	1. Pause/play- Space
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
import speak

class webBrowser:
	def __init__(self):
		speak.say("Welcome to Web Browsing")
		self.url = ""
		self.googleData = None
		self.buffer = ["Press f to google search", "Press r to listen bookmark or history"]
		#Pause 
		self.pause_key = 0 #Initially pause is off
		#Lock
		self.lock = threading.Lock()  
		kb = threading.Thread(target=self.listenKeyboard)
		#sp = threading.Thread(target=self.say)
		google = threading.Thread(target=self.googleSearchSpeak)
		kb.start()
		#sp.start()
		google.start()
		self.say()
		
		
	def listenKeyboard(self):
		try:
			with keyboard.Listener(on_press=self.onPress) as listener:
				listener.join()
		except Exception as e:
			print(e)

	def onPress(self,key):
		while msvcrt.kbhit():
			msvcrt.getch()
		try:
			print('You pressed {0}'.format(key.char))
			if key.char == 'q':
				self.exit()
			if key.char == 'b':
				self.createBookmark()
			if key.char == 'f':
				self.googleSearch()
			if key.char == 'r':
				self.read()
		except AttributeError:
			if key == keyboard.Key.space:
				print('You pressed space')
				if self.pause_key == 0:
					self.lock.acquire()
					self.pause_key = 1
					speak.say('Pausing')
				else:
					speak.say('Resuming')
					self.pause_key = 0
					self.lock.release()
				
	
	
	def say(self):
		#os.system("say {0}".format(line))
		while True:
			if len(self.buffer):
				line = self.buffer.pop()
				while self.pause_key:
					pass
				if len(line):
					self.lock.acquire()
					speak.say(line)
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
		speak.say("Exiting Web Browser")
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
		speak.say("Enter keywords to search")
		keyWords = raw_input()
		data = {'name': keyWords,'link': 'google.com'}
		self.createHistory(data)
		self.googleData = web.search(keyWords,1)
		print "End loading search"


	def googleSearchSpeak(self):
		while True:
			if self.googleData is not None:
				for self.result in self.googleData:
					while (len(self.buffer) and self.pause_key):
						time.sleep(2)
					self.buffer.insert(0,'Title ' + self.result.name.encode('ascii','ignore').decode('ascii'))
					self.buffer.insert(0,'Description')
					desc = self.result.description.encode('ascii','ignore').decode('ascii').splitlines()
					for d in desc:
						self.buffer.insert(0,d.encode('ascii','ignore').decode('ascii'))
				self.buffer.insert(0,'Search completed.')
				self.googleData = None
				
		
		

	#Create bookmarks, Web browser must be open and active
	def createBookmark(self):
		b = {}
		b["name"] = self.result.name.encode('ascii','ignore').decode('ascii')
		b["url"] = self.result.link.encode('ascii','ignore').decode('ascii')
		b["created at"] = str(datetime.datetime.now())
		with open(os.path.join("browser",'bookmarks.txt'), 'a+') as f:
  			json.dump(b, f, ensure_ascii=False)
  			f.write('\n')
  			f.close()
  		speak.say('Bookmark added')

	#Bookmarks exported to a file "bookmarks"
	# def accessBookmarks(self):
	def createHistory(self,result):
		h = {}
		h["visited at"] = str(datetime.datetime.now())
		h["name"] = result['name']
		h["url"] = result['link']
		with open(os.path.join("browser",'history.txt'), 'a+') as f:
  			json.dump(h, f, ensure_ascii=False)
  			f.write('\n')
  			f.close()

	def read(self):
		speak.say('Press 1 for bookmark and 2 for history')
		ch = int(raw_input())
		if ch == 1:
			self.accessBookmark()
		elif ch == 2:
			self.accessHistory()
		else:
			speak.say('Invalid Choice! Exiting Bookmark or History Reading Task')


  	def accessHistory(self):
  		if self.googleData is not None:
  			self.buffer.insert(0,'Continuing google search speaking task')
  		with open(os.path.join("browser",'history.txt')) as json_file: 
  			for data in json_file:
  				self.buffer.append(data)
		self.buffer.append('History Content')
  		print "End History Loading"
  				
  	def accessBookmark(self):
  		if self.googleData is not None:
  			self.buffer.insert(0,'Continuing google search speaking task')
  		with open(os.path.join("browser",'bookmarks.txt')) as json_file: 
  			for data in json_file:
  				self.buffer.append(data)
		self.buffer.append('Bookmarks Content')
  		print "End Bookmarks Loading"
  		



instance = webBrowser()




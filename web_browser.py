#Run the following commands to install required libraries
	#1.Speech recognition
	# pip install SpeechRecognition
	#2.Google Search
	# pip install beautifulsoup4
	# pip install google
	# pip install pynput
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
# import msvcrt
from pynput import keyboard
import os
import webbrowser as web
import io,json
import datetime
import termios, fcntl, sys, os

class webBrowser:
	def __init__(self):
		print "Welcome to Web Browsing"
		self.say("Welcome to Web Browsing")
		self.lock = threading.Lock()
		self.onPress()
		kb = threading.Thread(target=self.listenKeyboard())
		kb.start()
		
	def listenKeyboard(self):
		with keyboard.Listener(on_press=self.onPress()) as listener:
			listener.join()

	def onPress(self):
		fd = sys.stdin.fileno()
		oldterm = termios.tcgetattr(fd)
		newattr = termios.tcgetattr(fd)
		newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
		termios.tcsetattr(fd, termios.TCSANOW, newattr)

		oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
		try:
			while (1):
				try:
					c = sys.stdin.read(1)
					print "Got character", repr(c)
					try:
						if c == 'q':
							self.exit()
						if c == 'b':
							self.createBookmark()
						if c == 'f':
							self.googleSearch()
						if c == ' ':
							self.visitUrl()
								
					except AttributeError:
						print "Attribute Error"
				except IOError: pass
		finally:
			termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
			fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

		


	def say(self,line):
		os.system("say {0}".format(line))

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
		sys.stdout.flush()
		termios.tcflush(sys.stdin, termios.TCIOFLUSH)
		os._exit(1)

	def createBookmark(self):
		b = {}
		b["name"] = self.result.name
		b["url"] = self.result.link
		b["datetime"] = str(datetime.datetime.now())
		with open('bookmarks.txt', 'a+') as f:
			json.dump(b, f, ensure_ascii=False)

	#Bookmarks exported to a file "bookmarks"
	# def accessBookmarks(self):
	def createHistory(self):
		print "history"
		h = {}
		h["name"] = self.result.name
		h["url"] = self.result.link
		h["datetime"] = str(datetime.datetime.now())
		with open('history.txt', 'a+') as f:
			json.dump(h, f, ensure_ascii=False)

	def visitUrl(self):
		self.lock.acquire()
		self.say("Visiting chosen result")
		web.open(self.result.link)
		self.createHistory()
		self.lock.release()

	def googleSearch(self):
		from google import google
		self.lock.acquire()
		print "Enter keywords to search"
		self.say("Enter keywords to search")
		keyWords = raw_input()
		results = google.search(keyWords,1)
		self.lock.release()

		for self.result in results:
			print "Name: ",self.result.name
			self.say(self.result.name.encode('utf-8'))
			description = self.result.description.encode('utf-8')
			print "Description: ",description
			self.say("Description: "+description)
			print "------------------------"
			time.sleep(3)

	
		

 # def accessBookmarks(self):
#def accessHistory(self):
		



instance = webBrowser()




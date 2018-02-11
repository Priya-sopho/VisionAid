#pip install PyPDF2
#pip install pypiwin32 or pywin32
#pip install num2words
# importing required modules
import PyPDF2
import win32com.client as wincl
import num2words as n2w
import os 
import re
import threading,time
voice = wincl.Dispatch("SAPI.SpVoice")
from pynput import keyboard 
import msvcrt


#Pdf file to listen
file = "C:\Users\Priya Rani\Desktop\Wedu\SOP.pdf" 

class pdfReader:
	task = ['Start','Pause','Resume','Exit','Rewind','Repeat','Skip current page','Jump on a page',
		'Search','Change speed']

	def __init__(self, file,password = ''):
			 
		# creating a pdf file object
		self.pdfFileObj = open(file, 'rb') 
			 
		# creating a pdf reader object
		self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)

		#decrypting password
		if password != '':
			self.pdfReader.decrypt(password)

		#line no.
		self._line = 0
		#page no.
		self._page = 0

		# creating a page object
		self.pageObj = self.pdfReader.getPage(self._page)
			
		# extracting text from page
		self.lines = self.pageObj.extractText().splitlines()
		
		#Pause button 
		self.lock = threading.Lock()  #Initially pause is on
		
		kb = threading.Thread(target=self.listenKeyboard)
		kb.start()
		# sp = threading.Thread(target=self.start)
		# sp.start()


	    
	def __del__(self):
		self.pdfFileObj.close()

	def on_press(self,key):
		#Clear the input flush
		while msvcrt.kbhit():
			msvcrt.getch()
			
		try:
			if key.char == 'q':
				self.exit()
			if key.char == 'j':
			    self.jump()
			elif key.char == 'f':
			    self.search()
			elif key.char == 'r':
			    self.repeat() 
		        
		except AttributeError:
			if (key == keyboard.Key.space) and self.lock.locked():
			    self.lock.release()
			    #self.resume()
			elif key == keyboard.Key.space:
				self.lock.acquire()
				self.pause()
			elif(key == keyboard.Key.up):
			    self.change_speed(1)
			elif(key == keyboard.Key.down):
			    self.change_speed(-1)
			elif(key == keyboard.Key.right):
			    self.skip()
			elif(key == keyboard.Key.left):
			    self.rewind()
			elif(key == keyboard.Key.esc):
			    self.exit()

	def listenKeyboard(self):
	    # Collect events until released
	    with keyboard.Listener(on_press=self.on_press) as listener:
	        listener.join()

	def  findText(self,s):
		pages = []
		s = re.compile(s.lower())
		for i in range(self.pdfReader.getNumPages()):
			content = self.pdfReader.getPage(i).extractText().lower()
			if s.search(content) is not None:
				if i not in pages:
					pages.append(i)
		
		return pages


	def menu(self):
		voice.Speak('What do you want to do?')
		for i in range(len(self.task)):
			voice.Speak(n2w.num2words(i+1,to='ordinal')+self.task[i])
		response = int(raw_input())
		if response < len(self.task):
			voice.Speak(self.task[response-1])
		self.action(response)


	
	"""
	 Start the pdf reading task.
	"""
	def start(self):
		try:
			
			#Number of pages in pdf file
			self.total_pages = self.pdfReader.numPages
			if self.total_pages>1:
				page = 'pages.'
			else:
				page = 'page.'

			voice.Speak('There are '+ n2w.num2words(self.total_pages,to='cardinal') + page)
			self.resume()
		except :
			voice.Speak('Some Error')
			return
			

	"""
	  Pause pdf reading task
	"""
	def pause(self):
		voice.Speak('Pausing')
		
		

	"""
	 Resume pdf task
	"""

	def resume(self):
		#Wait until pause is not false
		try:
			if(self._page >= self.total_pages):
				voice.Speak('We reached the end of file')
				self.exit()
			
			#if on first line of page,then tell page number
			if self._line == 0:
				self.lock.acquire()
				voice.Speak(n2w.num2words(self._page+1, to='ordinal') + 'page') 
				self.lock.release()
			
			# creating a page object
			self.pageObj = self.pdfReader.getPage(self._page)
			
			# extracting text from page
			self.lines = self.pageObj.extractText().splitlines()
			if len(self.lines) == 0:
				voice.Speak('Unable to detect the content')
			while self._line < len(self.lines):
				self.lock.acquire(True)
				voice.Speak(self.lines[self._line])
				self._line += 1		
				self.lock.release()
			self._page += 1
			self._line = 0
			self.resume()

		except:
			voice.Speak("Some error")
			return
		
	"""
	 Exit pdf Reading Task
	"""
	def exit(self):		
		voice.Speak('Exiting pdf reading task')
		#Clear the input flush
		while msvcrt.kbhit():
			msvcrt.getch()
		os._exit(1)
	

	"""
	  Repeat the last line
	"""	
	def repeat(self):
		self.lock.acquire()
		self._line -= 1
		if(self._line<0):
			self._line = 0
			self._page -= 1
			if(self._page < 0):
				self._page = 0
			#if on first line of page,then tell page number
			if self._line == 0:
				voice.Speak(n2w.num2words(self._page+1, to='ordinal') + 'page') 
			
			# creating a page object
			self.pageObj = self.pdfReader.getPage(self._page)
			
			# extracting text from page
			self.lines = self.pageObj.extractText().splitlines()
			if len(self.lines) == 0:
				voice.Speak('Unable to detect the content')
		self.lock.release()
			
	
	"""
	 Move 10 lines back
	"""
	def rewind(self):
		self.lock.acquire()
		self._line -= 10
		if(self._line<0):
			self._line = 0
			self._page -= 1
			if(self._page < 0):
				self._page = 0
			#if on first line of page,then tell page number
			if self._line == 0:
				voice.Speak(n2w.num2words(self._page+1, to='ordinal') + 'page') 
			
			# creating a page object
			self.pageObj = self.pdfReader.getPage(self._page)
			
			# extracting text from page
			self.lines = self.pageObj.extractText().splitlines()
			if len(self.lines) == 0:
				voice.Speak('Unable to detect the content')
		self.lock.release()
	

	"""
	 Skip current and move to next page
	"""
	def skip(self):
		self.lock.acquire()
		voice.Speak('Moving to next page')
		self._page += 1
		self._line = 0
		if(self._page >= self.total_pages):
			voice.Speak('We reached the end of file')
			self.exit()

		#if on first line of page,then tell page number
		if self._line == 0:
			voice.Speak(n2w.num2words(self._page+1, to='ordinal') + 'page') 
		
		# creating a page object
		self.pageObj = self.pdfReader.getPage(self._page)
		
		# extracting text from page
		self.lines = self.pageObj.extractText().splitlines()
		if len(self.lines) == 0:
			voice.Speak('Unable to detect the content')
		self.lock.release()
		
	

	"""
	 Jump on a specific page
	"""		
	def jump(self):
		#Clear the input flush
		while msvcrt.kbhit():
			msvcrt.getch()
		self.lock.acquire()
		voice.Speak('Tell me the page number to jump on?')
		self._page = int(raw_input())-1
		if(self._page < 0):
			self._page = 0
		if(self._page > self.total_pages):
			self._page = self.total_pages -1
		if(self._page >= self.total_pages):
			voice.Speak('We reached the end of file')
			self.exit()
		self._line = 0
		#if on first line of page,then tell page number
		if self._line == 0:
			voice.Speak(n2w.num2words(self._page+1, to='ordinal') + 'page') 
		
		# creating a page object
		self.pageObj = self.pdfReader.getPage(self._page)
		
		# extracting text from page
		self.lines = self.pageObj.extractText().splitlines()
		if len(self.lines) == 0:
			voice.Speak('Unable to detect the content')
		self.lock.release()
		
	

	"""
	 Search for a specific word in pdf file
	"""
	def search(self):
		#Clear the input flush
		while msvcrt.kbhit():
			msvcrt.getch()
		self.lock.acquire()
		voice.Speak('What you want to search?')
		r = raw_input()
		pages = self.findText(r)
		if len(pages) == 0:
			voice.Speak(r+' not found!!')
		else :	
			if len(pages)>1:
				page = 'pages.'
			else:
				page = 'page.'
			voice.Speak(r+ ' found in '+ n2w.num2words(len(pages), to='cardinal') + page)
			for p in pages:
				voice.Speak('Found at page number'+ n2w.num2words(p+1,to='cardinal'))
		self.lock.release()
		
		
	"""
	 Change the rate of speaking up key increase the speed, down key decrease the speed
	"""
	def change_speed(self,r):
		voice.Rate += r
	
#Callback for speech recognizing	
def Task(phrase):
	phrase.lower()
	if phrase == 'start':
		start()
	elif phrase == 'pause':
		pause()
	elif phrase == 'resume':
		resume()
	elif phrase == 'exit':
		exit()
	elif phrase == 'rewind':
		rewind()
	elif phrase == 'repeat':
		repeat()
	elif phrase == 'skip':
		skip()
	elif phrase == 'jump':
		jump()
	elif phrase == 'search':
		search()
	elif phrase == 'change speed':
		change_speed()
	else:
		voice.Speak('Sorry! Unable to recognize your action')
	resume()
	
#start()
reader = pdfReader(file)
reader.start()		

		
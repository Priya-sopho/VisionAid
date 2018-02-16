#pip install newsapi-python
import win32com.client as wincl
import os 
import threading
from pynput import keyboard 
import msvcrt
voice = wincl.Dispatch("SAPI.SpVoice")

"""
 Available categories 
  business, entertainment, general, health ,science, sports, technology
"""

categories = ['general','business','sports','science','technology','health','entertainment']
class news:

	def __init__(self):
		from newsapi import NewsApiClient
		self.newsapi = NewsApiClient(api_key='ae88bd8bd9d248cdbfba80e514599b60')

		self.category_code = 0 #Initialized with general category
        self.article = 0  #Intialized with 1st article

		#Lock
		self.lock = threading.Lock()  #Initially pause is on
		
		#Pause button
		self.pause_key = 0

		kb = threading.Thread(target=self.listenKeyboard)
		kb.start()
		
		
	"""
	 Return top 20 head lines for a particular category
	"""
	def headlines(self,keyword):
		top_headlines = self.newsapi.get_top_headlines(category=keyword,language='en',country='in')
		return top_headlines['articles']

	"""
	 Keyboard listening callback function
	"""
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
			if (key == keyboard.Key.space) and self.pause_key:
				self.pause_key = 0
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

	"""
	 Listen to keyboard keys
	"""
	def listenKeyboard(self):
	    # Collect events until released
	    with keyboard.Listener(on_press=self.on_press) as listener:
	        listener.join()

	"""
	 Speak the text
	"""
	def speak(self,text):
		self.lock.acquire()
		if(len(text) == 0):
			voice.Speak('None')
		else:	
		voice.Speak(text)
		self.lock.release()

	"""
	  Pause task
	"""
	def pause(self):
		self.pause_key = 1
		voice.Speak('Pausing')
		
		
	"""
	 Resume news listening task
	"""
	def resume(self):
		#Wait until pause is not false
		try:
			#if on first article of category,then tell category
			if self.article == 0:
				speak(categories[self.category_code]+'news')
			# creating a page object
			self.pageObj = self.pdfReader.getPage(self._page)
			
			# extracting text from page
			self.lines = self.pageObj.extractText().splitlines()
			if len(self.lines) == 0:
				voice.Speak('Unable to detect the content')
			while self._line < len(self.lines):
				self.lock.acquire()
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
			# creating a page object
			self.pageObj = self.pdfReader.getPage(self._page)
			
			# extracting text from page
			self.lines = self.pageObj.extractText().splitlines()
			
			self._line = len(self.lines) - 10
			if(self._line < 0):
				self._line = 0
			#if on first line of page,then tell page number
			if self._line == 0:
				voice.Speak(n2w.num2words(self._page+1, to='ordinal') + 'page') 
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
	 Change the rate of speaking up key increase the speed, down key decrease the speed
	"""
	def change_speed(self,r):
		voice.Rate += r

	"""
	 Reading news for user
	"""
	def news_reader(self):
		self.speak('Welcome to news listening task')
		


def main():
	News = news()
	News.news_reader()
	#print(News.headlines('entertainment'))
	#print(News.business())
	"""
	data = News.government()
	data = data['articles']
	for article in data:
		title = article['title'].encode('ascii','ignore')
		url = article['url'].encode('ascii','ignore')
		desc = article['description'].encode('ascii','ignore')
		sense.Speak('Title'+title)
		sense.Speak('Desciption'+desc)
		sense.Speak('Wanna Listen complete news (yes or no)')
		i = raw_input()
		if(i == 'y'):
			#browse
			pass
		elif(i != 'n'): #if pressed anything else
			os._exit(1)	
	"""

if __name__ == '__main__':
	main()
#pip install newsapi-python
import speak
import os 
import threading
from pynput import keyboard 
import msvcrt

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
		self.articles = self.headlines(categories[self.category_code])

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
			print('You pressed {0}'.format(key.char))
			if key.char == 'q':
				self.exit()
			elif key.char == 'r':
			    self.repeat() 
		        
		except AttributeError:
			print('You pressed {0}'.format(key))
			if (key == keyboard.Key.space) and self.pause_key:
				self.pause_key = 0
				self.lock.release()
				    #self.resume()
			elif key == keyboard.Key.space:
				self.lock.acquire()
				self.pause()
			elif(key == keyboard.Key.up):
			    speak.change_speed(1)
			elif(key == keyboard.Key.down):
			    speak.change_speed(-1)
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
			speak.say('None')
		else:	
			speak.say(text)
		self.lock.release()

	"""
	  Pause task
	"""
	def pause(self):
		self.pause_key = 1
		speak.say('Pausing')
		
		
	"""
	 Resume news listening task
	"""
	def resume(self):
		#Wait until pause is not false
		try:
			# Get articles 
			self.articles = self.headlines(categories[self.category_code])
			
			while self.article < len(self.articles):
				#if on first article of category,then tell category
				if self.article == 0:
					self.speak(categories[self.category_code]+' news')			
				a = self.article
				if(self.article == a):
					self.speak('Title '+self.articles[self.article]['title'].encode('ascii','ignore').decode('ascii'))
				if(self.article == a):
					self.speak('Desciption '+self.articles[self.article]['description'].encode('ascii','ignore').decode('ascii'))
				self.article += 1
			self.category_code = (self.category_code+1)%7
			#self.resume()

		except:
			speak.say("Some error")
			return
		
	"""
	 Exit pdf Reading Task
	"""
	def exit(self):		
		speak.say('Exiting news speaking task')
		#Clear the input flush
		while msvcrt.kbhit():
			msvcrt.getch()
		os._exit(1)
		

	"""
	  Repeat the last line
	"""	
	def repeat(self):
		self.lock.acquire()
		speak.say('Repeating')
		self.article -= 1
		if(self.article < 0):
			self.article = 0
		self.lock.release()
			
	
	"""
	 Move 10 lines back
	"""
	def rewind(self):
		self.lock.acquire()
		speak.say('Rewinding')
		self.article -= 10
		if(self.article<0):
			self.article = 0
			self.category_code = (self.category_code-1+7)%7
		self.lock.release()
	

	"""
	 Skip current and move to next page
	"""
	def skip(self):
		self.lock.acquire()
		speak.say('Moving to next Category')
		self.article = 0
		self.category_code = (self.category_code+1)%7
		# Get articles 
		self.articles = self.headlines(categories[self.category_code])
		self.lock.release()
	
	"""
	 Reading news for user
	"""
	def news_reader(self):
		self.speak('Welcome to news listening task')
		self.resume()
		


def main():
	News = news()
	News.news_reader()

if __name__ == '__main__':
	main()

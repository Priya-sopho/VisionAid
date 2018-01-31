#pip install PyPDF2
#pip install pypiwin32 or pywin32
#pip install num2words
# importing required modules
import PyPDF2
import win32com.client as wincl
import num2words as n2w
import os 
import re
sense = wincl.Dispatch("SAPI.SpVoice")

#Pdf file to listen
file = 'C:\Users\Priya Rani\Desktop\Wedu\SOP.pdf' 

class wordReader:
	#line no.
	_line = 0
	#page no.
	_page = 0
	task = ['Start','Pause','Resume','Exit','Rewind','Repeat','Skip current page','Jump on a page',
		'Search','Change speed']

	def __init__(self, file):
		 
		# creating a pdf file object
		self.pdfFileObj = open(file, 'rb') 
			 
		# creating a pdf reader object
		self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)
			 
		#Number of pages in pdf file
		self.total_pages = self.pdfReader.numPages
		if self.total_pages>1:
			page = 'pages.'
		else:
			page = 'page.'

		sense.Speak('There are '+ n2w.num2words(self.total_pages,to='cardinal') + page)

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
		sense.Speak('What do you want to do?')
		for i in range(len(self.task)):
			sense.Speak(n2w.num2words(i+1,to='ordinal')+self.task[i])
		response = int(raw_input())
		if response < len(self.task):
			sense.Speak(self.task[response-1])
		self.action(response)


	
	def start(self):
		try:
			#global _page,_line
			if(self._page > self.total_pages):
				sense.speak('We reached the end of file')
				return 
			sense.Speak(n2w.num2words(self._page+1, to='ordinal') + 'page') 
			
			# creating a page object
			pageObj = self.pdfReader.getPage(self._page)
			
			# extracting text from page
			lines = pageObj.extractText().splitlines()
			while self._line < len(lines):
				sense.Speak(lines[self._line])
				self._line += 1		
			self._page += 1
			self._line = 0
		except KeyboardInterrupt:
			sense.Speak('Pausing..')
			response = int(raw_input())
			if response < len(self.task):
				sense.Speak(self.task[response-1])
			self.action(response)
			

	def pause(self):
		self.menu()

	def resume(self):
		
		# creating a page object
		pageObj = self.pdfReader.getPage(self._page)
		
		# extracting text from page
		lines = pageObj.extractText().splitlines()
		while self._line < len(lines):
			sense.Speak(lines[self._line])
			self._line += 1		
		self._page += 1
		self._line = 0

	def exit(self):		
		# closing the pdf file object
		self.pdfFileObj.close()
		sense.Speak('Exiting pdf reading task')
		os._exit(1)
		
	def repeat(self):
		
		self._line -= 1
		if(self._line<0):
			self._line = 0
			self._page -= 1
		if(self._page < 0):
			self._page = 0
		self.resume()

	def rewind(self):
		self._line -= 10
		if(self._line<0):
			self._line = 0
			self._page -= 0
		if(self._page < 0):
			self._page = 0
		self.resume()	


	def skip(self):
		sense.Speak('Moving to next page')
		self._page += 1
		self._line = 0
		self.start()

		
	def jump(self):
		sense.Speak('Tell me the page number to jump on?')
		self._page = int(raw_input())-1
		if(self._page < 0):
			self._page = 0
		if(self._page > self.total_pages):
			self._page = self.total_pages -1
		self.start()
		
	def search(self):
		sense.Speak('What you want to search?')
		r = raw_input()
		pages = self.findText(r)
		if len(pages) == 0:
			sense.Speak(r+' not found!!')
		else :	
			if len(pages)>1:
				page = 'pages.'
			else:
				page = 'page.'
			sense.Speak(r+ ' found in '+ n2w.num2words(len(pages), to='cardinal') + page)
		self.resume()	

	def change_speed(self):
		sense.Speak('Enter the rate change')
		r = int(raw_input())
		sense.Rate += r
		sense.Speak('Changed rate by a factor of '+ n2w.num2words(r, to='cardinal'))
		self.resume()
    

	def action(self,choice):
		try:
			if choice == 1:
				self.start()
			elif choice == 2:
				self.pause()
			elif choice == 3:
				self.resume()
			elif choice == 4:
				self.exit()
			elif choice == 5:
				self.rewind()
			elif choice == 6:
				self.repeat()
			elif choice == 7:
				self.skip()
			elif choice == 8:
				self.jump()
			elif choice == 9:
				self.search()
			elif choice == 10:
				self.change_speed()
			else:
				sense.Speak('Wrong Input!!')
				self.menu()
		except KeyboardInterrupt:
			sense.Speak('Pausing..')
			response = int(raw_input())
			if response < len(self.task):
				sense.Speak(self.task[response-1])
			self.action(response)

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
		sense.Speak('Sorry! Unable to recognize your action')
	resume()
	
#start()
reader = wordReader(file)
reader.start()		

		

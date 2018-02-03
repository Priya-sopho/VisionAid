#pip install python-docx
#pip install pypiwin32 or pywin32
#pip install num2words
# importing required modules
from docx import Document
import win32com.client as wincl
import num2words as n2w
import os 
import re
sense = wincl.Dispatch("SAPI.SpVoice")

#Pdf file to listen
file = 'C:\Users\Priya Rani\Desktop\Wedu\LDP.docx' 

class wordReader:
	#line no.
	_line = 0
	#para no.
	_para = 0
	task = ['Start','Pause','Resume','Exit','Rewind','Repeat','Skip current para','Jump on a para',
		'Search','Change speed']

	def __init__(self, file):
		 
		# creating a file object
		self.FileObj = open(file, 'rb') 
			 
		# creating a document object
		self.document = Document(self.FileObj)

		self.paragraphs = self.document.paragraphs
	
		self.paragraphs = [p for p in self.paragraphs if len(p.text) != 0]		 
		#Number of paras in doc file
		self.total_paras = len(self.paragraphs)
		if self.total_paras>1:
			para = 'paragraphs.'
		else:
			para = 'paragraph.'

		sense.Speak('There are '+ n2w.num2words(self.total_paras,to='cardinal') + para)

	def __del__(self):
	  	self.FileObj.close()

	def  findText(self,s):
		paras = []
		s = re.compile(s,re.I)
		i = 1
		for para in self.paragraphs:
			content = para.text
			#print(content)
			if s.search(content) is not None:
				if i not in paras:
					paras.append(i)
			i += 1		
		return paras


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
			if(self._para >= self.total_paras):
				sense.speak('We reached the end of the doc file')
				return 
			sense.Speak(n2w.num2words(self._para+1, to='ordinal') + 'para') 
			
			# creating a para object
			paraObj = self.paragraphs[self._para]
			
			# extracting text from para
			lines = paraObj.text.splitlines()
			while self._line < len(lines):
				sense.Speak(lines[self._line])
				self._line += 1		
			self._para += 1
			self._line = 0
			self.start()
		except KeyboardInterrupt:
			sense.Speak('Pausing..')
			response = int(raw_input())
			if response < len(self.task):
				sense.Speak(self.task[response-1])
			self.action(response)
			

	def pause(self):
		self.menu()

	def resume(self):
		
		if(self._para >= self.total_paras):
				sense.speak('We reached the end of the doc file')
				return 
		
		# creating a para object
		paraObj = self.paragraphs[self._para]
		
		# extracting text from para
		lines = paraObj.text.splitlines()
		while self._line < len(lines):
			sense.Speak(lines[self._line])
			self._line += 1		
		self._para += 1
		self._line = 0
		self.start() #begin with next para

	def exit(self):		
		sense.Speak('Exiting word document reading task')
		os._exit(1)
		
	def repeat(self):
		
		self._line -= 1
		if(self._line<0):
			self._line = 0
			self._para -= 1
		if(self._para < 0):
			self._para = 0
		self.resume()

	def rewind(self):
		self._line -= 10
		if(self._line<0):
			self._line = 0
			self._para -= 1
		if(self._para < 0):
			self._para = 0
		self.resume()	


	def skip(self):
		sense.Speak('Moving to next paragraph')
		self._para += 1
		self._line = 0
		self.start()

		
	def jump(self):
		sense.Speak('Tell me the para number to jump on?')
		self._para = int(raw_input())-1
		if(self._para < 0):
			self._para = 0
		if(self._para > self.total_paras):
			self._para = self.total_paras -1
		self.start()
		
	def search(self):
		sense.Speak('What you want to search?')
		r = raw_input()
		paras = self.findText(r)
		if len(paras) == 0:
			sense.Speak(r+' not found!!')
		else :	
			if len(paras)>1:
				para = 'paragraphs.'
			else:
				para = 'paragraph.'
			sense.Speak(r+ ' found in '+ n2w.num2words(len(paras), to='cardinal') + para)
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

		

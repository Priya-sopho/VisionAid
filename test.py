#pip install PyPDF2
#pip install pypiwin32 or pywin32
#pip install num2words
# importing required modules
import PyPDF2
import win32com.client as wincl
import num2words as n2w
import os 
sense = wincl.Dispatch("SAPI.SpVoice")

#line no.
_line = 0
#page no.
_page = 0
		
#Pdf file to listen
file = 'C:\Users\Priya Rani\Desktop\Wedu\SOP.pdf' 
	 
# creating a pdf file object
pdfFileObj = open(file, 'rb') 
	 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	 
#Number of pages in pdf file
total_pages = pdfReader.numPages
if total_pages>1:
	page = 'pages.'
else:
	page = 'page.'

task = ['Start','Pause','Resume','Exit','Rewind','Repeat','Skip current page','Jump on a page',
'Search','Change speed']

sense.Speak('There are '+ n2w.num2words(total_pages,to='cardinal') + page)


def menu():
	sense.Speak('What do you want to do?')
	for i in range(len(task)):
		sense.Speak(n2w.num2words(i+1,to='ordinal')+task[i])

	response = int(raw_input())
	sense.Speak(task[response-1])
	action(response)

def start():
	global _page,_line
	sense.Speak(n2w.num2words(_page+1, to='ordinal') + 'page') 
	
	# creating a page object
	pageObj = pdfReader.getPage(_page)
	
	# extracting text from page
	lines = pageObj.extractText().splitlines()
	while _line < len(lines):
		sense.Speak(lines[_line])
		_line += 1		
	_page += 1
	_line = 0

def pause():
	menu()

def resume():
	global _page,_line
	
	# creating a page object
	pageObj = pdfReader.getPage(_page)
	
	# extracting text from page
	lines = pageObj.extractText().splitlines()
	while _line < len(lines):
		sense.Speak(lines[_line])
		_line += 1		
	_page += 1
	_line = 0

def exit():		
	# closing the pdf file object
	pdfFileObj.close()
	sense.Speak('Exiting pdf reading task')
	os._exit(1)
	
def repeat():
	global _line,_page
	_line -= 1
	if(_line<0):
		_line = 0
		_page -= 0
	if(_page < 0):
		_page = 0
	resume()

def rewind():
	global _line,_page
	_line -= 10
	if(_line<0):
		_line = 0
		_page -= 0
	if(_page < 0):
		_page = 0
	resume()	
	

def jump():
	global _page,_line
	sense.Speak('Tell me the page number to jump on?')
	_page = int(raw_input())-1
	if(_page < 0):
		_page = 0
	if(_page > total_pages):
		_page = total_pages -1
	start()

def action(choice):
	try:
		if choice == 1:
			start()
		elif choice == 2:
			pause()
		elif choice == 3:
			resume()
		elif choice == 4:
			exit()
		elif choice == 5:
			rewind()
		elif choice == 6:
			jump()
	except KeyboardInterrupt:
		sense.Speak('Pausing..')
		menu()
			
	
menu()		
		

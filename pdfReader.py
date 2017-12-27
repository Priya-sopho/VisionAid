#pip install PyPDF2
#pip install pypiwin32 or pywin32
#pip install num2words
#pip install speech
# importing required modules
import PyPDF2
import speech
#import win32com.client as wincl
import num2words as n2w
import os 
#speak = wincl.Dispatch("SAPI.SpVoice")

def callback(phrase, listener):
	speech.say('You said '+phrase)
	phrase = phrase.lower()
	if phrase == "exit" :
		speech.say('Exiting pdf file reading task')
		os._exit(1)
	if phrase == "pause" :
		speech.say('What do you want to do?')
		#Menu
		speech.say(n2w.num2words(1, to='ordinal') + 'Exit')
		speech.say(n2w.num2words(2, to='ordinal') + 'Resume') 
		listener = speech.listenforanything(callback)

		
#Pdf file to listen
file = 'C:\Users\Priya Rani\Desktop\Wedu\SOP.pdf' 
 
# creating a pdf file object
pdfFileObj = open(file, 'rb') 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
#Number of pages in pdf file
n = pdfReader.numPages
if n>1:
	page = 'pages.'
else:
	page = 'page.'


response = speech.input("Say something, please.")
speech.say("You said " + response)

   

speech.say('There are '+ n2w.num2words(n,to='cardinal') + page)
listener = speech.listenforanything(callback)
while listener.islistening():
	for i in range(n):
		speech.say(n2w.num2words(i+1, to='ordinal') + 'page') 
		# creating a page object
		pageObj = pdfReader.getPage(i)
		listener = speech.listenforanything(callback)
		# extracting text from page
		lines = pageObj.extractText().splitlines()
		for each_line in lines:
			speech.say(each_line)
			listener = speech.listenforanything(callback)


# closing the pdf file object
pdfFileObj.close()
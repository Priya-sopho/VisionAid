#pip install PyPDF2
#pip install pypiwin32 or pywin32
#pip install num2words
# importing required modules
import PyPDF2
import win32com.client as wincl
import num2words as n2w
speak = wincl.Dispatch("SAPI.SpVoice")

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
	
speak.Speak('There are '+ n2w.num2words(n,to='cardinal') + page)

for i in range(n):
	p = n2w.num2words(i+1, to='ordinal')
	speak.Speak(p + 'page') 
	# creating a page object
	pageObj = pdfReader.getPage(i)
	 
	# extracting text from page
	text = pageObj.extractText()
	speak.Speak(text)

# closing the pdf file object
pdfFileObj.close()
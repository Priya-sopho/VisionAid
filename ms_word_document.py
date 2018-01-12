import docx
from docx.shared import Pt

# to get the whole document text for read operation
def getFullText():
	global doc
	fulltext = []
	for para in doc.paragraphs:
		fulltext.append(para.text)
	return '\n'.join(fulltext)

# to save the doc as a word document file
def saveAsDoc():
	global doc
	global filename
	doc.save(filename)

# Enter the text to be added
def enterText():
	text = raw_input("Enter the text : ")
	return text

# adding new paragraph at the end of the document 
def addNewPara():
	global doc
	text = enterText()
	doc.add_paragraph(text)
	saveAsDoc()

# add a new paragraph with bold text
def AddBoldText():
	global doc
	text = enterText()
	para = doc.add_paragraph()
	para.add_run(text).bold = True
	saveAsDoc()

# add a new paragraph with italic text
def AddItalicText():
	global doc
	text = enterText()
	para = doc.add_paragraph()
	para.add_run(text).italic = True
	saveAsDoc()

# add a new paragraph with underlined text
def AddUnderline():
	global doc
	text = enterText()
	para = doc.add_paragraph()
	para.add_run(text).underline = True
	saveAsDoc()

# to change the document's font name and font size
def changeDocFont(fontName, Size):
	global doc
	style = doc.styles['Normal']
	font = style.font
	font.name = fontName
	font.size = Pt(Size)
	font.bold = None
	font.italic = None
	font.underline = None

# to add a heading to the document
def addHeading():
	global doc
	text = enterText()
	doc.add_heading(text)
	saveAsDoc()


choice = int(raw_input("To open a new Word document - Enter 1" + '\n' + "To open an existing Word document - Enter 2 : "))
filename=""
if choice == 1 :
	doc = docx.Document()
	filename = raw_input("Give the name of the new file: ")
	if ".docx" not in filename:
		filename = filename + ".docx"
elif choice == 2:
	filename = raw_input("Enter the name of existing document: ")
	if ".docx" not in filename:
		filename = filename + ".docx"
		doc = docx.Document(filename)
saveAsDoc()
Flag = True
flag2 = True
while Flag == True:
	print ('1. To read the file' + '\n'
			'2. To write a new paragraph on the file' + '\n'
			'3. To add a new formatted text' + '\n'
			'4. To change the font style and font name of the document' +'\n'
			'5. To add a Heading')
	ch = int(raw_input())
	if ch == 1:
		print(getFullText())
	elif ch == 2:
		addNewPara()
	elif ch == 3:
		while flag2 == True:
			print('Enter your choice: bold, italic or underline')
			new_format = raw_input().upper()
			if new_format == 'BOLD':
				AddBoldText()
			elif new_format == 'ITALIC':
				AddItalicText()
			elif new_format == 'UNDERLINE':
				AddUnderline()
			Continue = raw_input("Do You want to add formatted text? y or n: ").upper()
			if Continue == 'N' or Continue == 'NO':
				flag2 = False
	elif ch == 4:
		name, size = raw_input("Enter the font name and font size(space seperated):").split(' ')
		size = int(size)
		changeDocFont(name, size)
	elif ch == 5:
		addHeading()
	another_operation = raw_input("Do You want to perform another operation? y or n: ").upper()
	if another_operation == 'N' or another_operation == 'No':
		Flag = False

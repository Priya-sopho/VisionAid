from __future__ import print_function
import docx
from docx.shared import Pt
from docx.shared import Inches
from docx.enum.style import WD_STYLE_TYPE


class docEditor(object):
	"""docstring for docEditor"""
	def __init__(self, docName, filename, paraName = None):
		super(docEditor, self).__init__()
		self.doc = docName
		if '.docx' not in filename:
			filename = filename + '.docx'
		self.filename = filename
		if (paraName != None):
			self.para = self.doc.paragraphs[-1]
		else:
			self.para = None
		
# to get the whole document text for read operation
	def getFullText(self):
		fulltext = []
		for paras in self.doc.paragraphs:
			fulltext.append(paras.text)
		return '\n'.join(fulltext)

# to save the doc as a word document file
	def saveAsDoc(self):
		self.doc.save(self.filename)

# Enter the text to be added
	def enterText(self):
		# text = raw_input("Enter the text : ")
		print("Enter the text: ")
		lines = []
		while True:
			line = raw_input()
			if line:
				lines.append(line)
			else:
				break
		text = '\n'.join(lines)
		return text

# adding new paragraph at the end of the document 
	def addNewPara(self):
		text = self.enterText()
		self.para = self.doc.add_paragraph(text)
		self.saveAsDoc()
		# return para
# to set the paragraph object
	def setPara(self, paragraph):
		self.para = paragraph

# add formatted text in the running paragraph
	def formattedtext(self,formats):
		types = formats.split(' ')
		lineBreak = raw_input("Do u want to enter formatted text on a new line? (Y or N): ").upper()
		run = self.para.add_run()
		style = self.para.style
		font  = style.font
		if lineBreak == 'Y' or lineBreak == 'YES':
			run.add_break()
		if 'BOLD' or 'B' in types:
			font.bold = not font.bold
			run.bold = font.bold
		if 'ITALIC' or 'I' in types:
			font.italic = not font.italic
			run.italic = font.italic
		if 'UNDERLINE' or 'U' in types:
			font.underline = not font.underline
			run.underline = font.underline
		text = self.enterText()
		run.add_text(text)
		self.saveAsDoc()

# to make a new table 
	def makeTable(self):
		row_count = int(raw_input("Enter the following" + '\n' + 'Rows: '))
		col_count = int(raw_input("Columns: "))
		table = self.doc.add_table(row_count,col_count)
		table.style.name = 'TableGrid'
		print("Enter the values in the table row by row: ")
		for row in table.rows:
			for cell in row.cells:
				cell.text = raw_input()	
			print('\n')	
		print('\n')
		for row in table.rows:
			for cell in row.cells:
				print(cell.text , end = ' ')
			print('\n')
		print('\n')
		self.saveAsDoc()

# to change the document's font name and font size
	def changeDocFont(self,fontName, Size):
		style = self.doc.styles['Normal']
		font = style.font
		font.name = fontName
		font.size = Pt(Size)

# to add a heading to the document
	def addHeading(self):
		l = int(raw_input("Enter the heading level: "))
		text = self.enterText()
		self.doc.add_heading(text, level = l)
		self.saveAsDoc()

# to add a picture to the doc file
	def addPicture(self):
		pic_name = raw_input("Enter the name of the Picture (with extension i.e. .png or .jpeg): ")
		pic_width = float(raw_input("Enter the picture width in inches: "))
		pic = self.doc.add_picture(pic_name, width = Inches(pic_width))
		self.saveAsDoc()



# the working menu
choice = int(raw_input("To open a new Word document - Enter 1" + '\n' + "To open an existing Word document - Enter 2 : "))
filename=""
if choice == 1 :
	docName = docx.Document()
	filename = raw_input("Give the name of the new file: ")
	if ".docx" not in filename:
		filename = filename + ".docx"
	document = docEditor(docName,filename)
elif choice == 2:
	filename = raw_input("Enter the name of existing document: ")
	if ".docx" not in filename:
		filename = filename + ".docx"
		docName = docx.Document(filename)
	document = docEditor(docName,filename,True)
document.saveAsDoc()
Flag = True
while Flag == True:
	print ('1. To read the document' + '\n' +
			'2. To add a Heading' + '\n' +
			'3. To write a new paragraph on the document' + '\n' +
			'4. To add a new formatted text' +'\n' +
			'5. To change the font style and font name of the document' + '\n'
			'6. To add a new Table and then display it' + '\n'
			'7. To add Picture to the document ')
	ch = int(raw_input("Enter your choice number: "))
	flag2 = True
	if ch == 1:
		print(document.getFullText())    # to display the text
	elif ch == 2:
		document.addHeading()
	elif ch == 3:
		document.addNewPara()
		# document.setPara(para)
	elif ch == 4:
		while flag2 == True:
			new_format = ''
			print('Enter your choice: bold(B), italic(I) or underline(U) (seperated by spaces): ')
			new_format = raw_input().upper()
			document.formattedtext(new_format)
			Continue = raw_input("Do You want to add more formatted text? y or n: ").upper()
			if Continue == 'N' or Continue == 'NO':
				flag2 = False
	elif ch == 5:
		name, size = raw_input("Enter the font name and font size(space seperated):").split(' ')
		size = int(size)
		document.changeDocFont(name, size)
	elif ch == 6:
		document.makeTable()
	elif ch == 7:
		document.addPicture()
	another_operation = raw_input("Do You want to perform another operation? y or n: ").upper()
	if another_operation == 'N' or another_operation == 'No':
		Flag = False

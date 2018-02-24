import os
import threading
import speak
import msvcrt
from pynput import keyboard

def exit(self):		
	speak.say('Exiting tasks')
	#Clear the input flush
	while msvcrt.kbhit():
		msvcrt.getch()
	os._exit(1)

def init():
	Flag = True
	while Flag:
		speak.say('Do you want to listen to tasks? Press S to listen: ')
		choice = raw_input().upper()
		if choice == 'S':
			speak.say("Press" + "\n"
						"G - To Open Google " + '\n'
						"P - To read the PDF file " + '\n'
						"C - To create/edit a Word file" + '\n'
						"R - To read a Word file" + '\n'
						"M - To play Music" + '\n'
						"F - To work with files and directories" + '\n'
						"N - To get latest news "+ "\n"
						"L - Logout" )
		speak.say("Press the task choice key: ")
		ch = raw_input().upper()
		if ch == 'G':
			try:
				os.system('python web_browser.py')
			except:
				speak.say("Error in opening Google!")
		elif ch == 'P':
			try:
				os.system('python pdfReader.py')
			except:
				speak.say("Error in opening and reading a PDF file!")
		elif ch == 'C':
			try:
				os.system('python ms_word_document.py')
			except:
				speak.say("Error in creating or editing the word file!")
		elif ch == 'R':
			try:
				os.system('python wordReader.py') 
			except:
				speak.say("Error in reading the word file!")
		elif ch == 'M':
			try:
				os.system('python music.py')
			except:
				speak.say("Error in playing Music!")
		elif ch == 'F':
			try:
				os.system('python file_exploration.py')
			except:
				speak.say("Error in opening and working with files!")
		elif ch == 'N':
			try:
				os.system('python news.py')
			except:
				speak.say("Error in getting news!")
		elif ch == 'L':
			try:
				speak.say("Logging Out")
				os._exit(1)
			except:
				speak.say("Unable to logout")
		else:
			speak.say("Invalid Choice!")
		
print('Plugin your earphone')
speak.say('Face Recognition Login')
try:
	os.system('python Login_via_face.py')
	speak.say("Starting VisionAid for Windows!")
	speak.say("You can perform any of the listed task!")
	init()

except:
	speak.say("Unable to login")


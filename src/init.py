import os
import threading
import win32com.client as wincl
import msvcrt
from pynput import keyboard
voice = wincl.Dispatch("SAPI.SpVoice")

def exit(self):		
	voice.Speak('Exiting tasks')
	#Clear the input flush
	while msvcrt.kbhit():
		msvcrt.getch()
	os._exit(1)

def init():
	Flag = True
	while Flag:
		voice.Speak('Do you want to listen to tasks? Press S to listen: ')
		choice = raw_input().upper()
		if choice == 'S':
			voice.Speak("Press" + "\n"
						"G - To Open Google " + '\n'
						"P - To read the PDF file " + '\n'
						"C - To create/edit a Word file" + '\n'
						"R - To read a Word file" + '\n'
						"M - To play Music" + '\n'
						"F - To work with files and directories" + '\n'
						"N - To get latest news "+ "\n"
						"L - Logout" )
		voice.Speak("Press the task choice key: ")
		ch = raw_input().upper()
		if ch == 'G':
			try:
				os.system('python web_browser.py')
			except:
				voice.Speak("Error in opening Google!")
		elif ch == 'P':
			try:
				os.system('python pdfReader.py')
			except:
				voice.Speak("Error in opening and reading a PDF file!")
		elif ch == 'C':
			try:
				os.system('python ms_word_document.py')
			except:
				voice.Speak("Error in creating or editing the word file!")
		elif ch == 'R':
			try:
				os.system('python wordReader.py') 
			except:
				voice.Speak("Error in reading the word file!")
		elif ch == 'M':
			try:
				os.system('python music.py')
			except:
				voice.Speak("Error in playing Music!")
		elif ch == 'F':
			try:
				os.system('python file_exploration.py')
			except:
				voice.Speak("Error in opening and working with files!")
		elif ch == 'N':
			try:
				os.system('python news.py')
			except:
				voice.Speak("Error in getting news!")
		elif ch == 'L':
			try:
				voice.Speak("Logging Out")
				os._exit(1)
			except:
				voice.Speak("Unable to logout")
		else:
			voice.Speak("Invalid Choice!")
		
os.system('python Login_via_face.py')
voice.Speak("Starting VisionAid for Windows!")
voice.Speak("You can perform any of the listed task!")
while True:
	init()

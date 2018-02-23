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
	#Lock
	lock = threading.Lock()  #Initially pause is on		
	#Pause button
	pause_key = 0
	kb = threading.Thread(target=self.listenKeyboard)
	kb.start()
	# voice.Speak()
	Flag = True
	while Flag:
		voice.Speak('Do you want to listen to tasks? Press S to listen: ')
		choice = raw_input().upper()
		if choice == 'S':
			voice.Speak("Press" + "\n"
						"G - To Open Google " + '\n'
						"R - To read the PDF file " + '\n'
						"C - To create/edit a Word file" + '\n'
						"J - To read a Word file" + '\n'
						"M - To play Music" + '\n'
						"F - To work with files and directories" + '\n'
						"N - To get latest news " )
		voice.Speak("Press the task choice key: ")
		ch = raw_input().upper()
		if ch == 'G':
			lock.acquire()
			try:
				import web_browser.py
			except:
				voice.Speak("Error in opening Google!")
			lock.release()
		elif ch == 'R':
			lock.acquire()
			try:
				import pdfReader.py
			except:
				voice.Speak("Error in opening and reading a PDF file!")
			lock.release()
		elif ch == 'C':
			lock.acquire()
			try:
				import ms_word_document.py
			except:
				voice.Speak("Error in creating or editing the word file!")
			lock.release()
		elif ch == 'J':
			lock.acquire()
			try:
				import wordReader.py
			except:
				voice.Speak("Error in reading the word file!")
			lock.release()
		elif ch == 'M':
			lock.acquire()
			try:
				import music.py
			except:
				voice.Speak("Error in playing Music!")
			lock.release()
		elif ch == 'F':
			lock.acquire()
			try:
				import file_exploration.py
			except:
				voice.Speak("Error in opening and working with files!")
			lock.release()
		elif ch == 'N':
			lock.acquire()
			try:
				import news.py
			except:
				voice.Speak("Error in getting news!")
			lock.release()
		else:
			voice.Speak("Invalid Choice!")
		voice.Speak("Any more task? (yes or No)")
		more_task = raw_input().upper()
		if more_task == 'N' or more_task == 'NO':
			Flag = False
			exit()

import Login_via_face.py
voice.Speak("Starting VisionAid for Windows!")
voice.Speak("You can perform any of the listed task!")
while True:
	init()

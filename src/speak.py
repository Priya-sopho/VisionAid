import win32com.client as wincl
voice = wincl.Dispatch("SAPI.SpVoice")

def say(text):
	print(text)
	voice.Speak(text)

def change_speed(r):
	voice.Rate += r

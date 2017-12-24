#function to listen to voice commands and then return a corresponding string 
def listen(chunk_size=2048):
	import speech_recognition as sr
	# obtain audio from the microphone  
	r = sr.Recognizer()  
	with sr.Microphone(chunk_size=chunk_size) as source:  
		print("Please wait. Calibrating microphone...")  
		# listen for 3 seconds and create the ambient noise energy level  
		r.adjust_for_ambient_noise(source, duration=3)  
		#Instead of printing "SAY OUT LOUD"
		print("Say something!")  
		audio = r.listen(source)
		# recognize speech using Google  
		try:  
			text = r.recognize_google(audio)
			if(text!=None):
				return text
			else:
				listen()
		except sr.UnknownValueError:  
			print("Google could not understand audio") 
			listen()
		except sr.RequestError as e:  
			print("Google error; {0}".format(e)) 
			listen() 

def webBrowser():
	from splinter import Browser 
	browser = Browser()


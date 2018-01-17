#pip install pygame
#pip install pypiwin32 or pywin32


#importing required modules

import pygame as pg
import win32com.client as wincl
import num2words as n2w
import os
sense=wincl.Dispatch("SAPI.SpVoice")

music_file = "C:\\Users\\H\\Music\\English Songs\\Cut - Copy.mp3"
volume=0.8

class musicPlayer:
    task = ['Play', 'Pause', 'Stop', 'Rewind', 'Unpause', 'Queue', 'Set Volume']

    def __init__(self):
        # set up the mixer
        freq = 44100 # audio CD quality
        bitsize = -16 # unsigned 16 bit
        channels = 2 # 1 is mono, 2 is stereo
        buffer = 2048 # number of samples (experiment to get best sound)

        #initializes the pygame mixer (player) with the given arguments
        pg.mixer.init(freq, bitsize, channels, buffer)



    def play_music(music_file, volume=0.8):
        try:
            pg.mixer.music.load(music_file)
            sense.Speak('Music file loaded!')

        except pg.error:
            sense.Speak('File not found!')
            return
        pg.mixer.music.play()



    def menu(self):
        sense.Speak('What do you want to do?')
        for i in range(len(self.task)):
            sense.Speak(n2w.num2words(i+1,to='ordinal')+self.task[i])
        response = int(raw_input())
        if response < len(self.task):
            sense.Speak(self.task[response-1])
        self.action(response)


    def pause(self):
        pg.mixer.music.pause()
        sense.Speak('Music paused!');



    def resume(self):
        pg.mixer.music.unpause()
        sense.Speak('Music Resumed!');


    def exit(self):
        pg.mixer.music.stop()
        sense.Speak('Exiting music playing task')
        os._exit(1)



    def rewind(self):
        pg.mixer.music.rewind()
        sense.Speak('Music rewinded!')



#    def queueNext(self):
#        self.index = (self.index + 1) % len(self.filenames)
#        curFile = self.filenames[self.index]
#        pygame.mixer.music.queue(getPath(music, curFile))



    def setVolume(self):
        volume = min(volume,1.0)
        volume = max(volume,0.0)
        pg.mixer.music.set_volume(volume)



    def action(self,choice):
         try:
             if choice==1:
                 self.play_music()
             elif choice==2:
                 self.pause()
             elif choice==3:
                 self.resume()
             elif choice==4:
                 self.exit()
             elif choice==5:
                 self.rewind()
             elif choice==6:
                 self.queueNext()
             elif choice==7:
                 self.setVolume()
             else:
                 sense.Speak('Wrong Input!')
                 self.menu()



     def Task(phrase):
         phrase.lower()
         if phrase == 'play':
             play_music()
         elif phrase == 'pause':
             pause()
         elif phrase == 'resume':
             resume()
         elif phrase == 'exit':
             exit()
         elif phrase == 'rewind':
             rewind()
         elif phrase == 'play next':
             queueNext()
         elif phrase == 'set volume':
             setVolume()
         else
             sense.Speak('Sorry! Unable to recognize your action')
         resume()


play_music(music_file,volume)

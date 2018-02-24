import pygame as pg
import time,datetime
import os
import json
import speak

"""
    MusicDirectory : music/
    ToDo:
    1. Custom Playlist
    2. Order playlist by number of plays
    3. Shuffle Playlist
    4. Keyboard Interrupts
    5. Play from a position
"""
relDir = "music"

class music:
    def __init__(self):
        freq = 48000 # audio DVD quality
        bitsize = -16 # unsigned 16 bit
        channels = 2
        buffer = 10240 
        pg.mixer.init(freq, bitsize, channels, buffer)
        self.q = pg.mixer.music

    def play(self,file,pos = None):

        file = relDir+"/"+file
        try:
            self.q.load(file)
            print("Music file {} loaded!".format(file))
        except pg.error:
            print("File {} not found! ({})".format(file, pg.get_error()))
            return

        try:
            self.q.set_pos(pos)
        except:
            print "Unable to set position"

        self.q.play()
        print "Playing now at: ",datetime.datetime.now().time()
        while self.q.get_busy():
            pass
        print "Playing ended at: ",datetime.datetime.now().time()

    def pauseResume(self):
        if self.q.get_busy():
            self.q.pause()
        elif self.q.pause():
            self.q.unpause()

    def setVolume(self, volume = 0.8):
        self.q.set_volume(volume)

    def rewind():
        self.q.rewind()

    def stop():
        self.q.stop()

class playlist:
    def __init__(self):
        self.autoPlaylist = {}
        try:
            with open('playlist.json') as handle:
                self.autoPlaylist = json.loads(handle.read())
        except :
            pass
        #Create customised playlist
        # self.myPlaylist = {}

    def createPlaylist(self, auto = True):
        if(auto):
            for filename in os.listdir(relDir):
                if filename.endswith(".mp3"):
                    file = filename
                    if(file not in self.autoPlaylist):
                        self.autoPlaylist[file] = 0
        with open('playlist.json', 'w+') as f:
            json.dump(self.autoPlaylist, f, ensure_ascii=False)

    # Add functionality for shuffle and sort by number of plays
    def playPlaylist(self):
        speak.say("Press y to play the song")
        for file in self.autoPlaylist:
            f = file[0:len(file)-4]
            speak.say("Do you want to listen {0}".format(f))
            r = raw_input()
            if r=='y':
                m = music()
                m.play(file)
            else:
                pass


l = playlist()
l.createPlaylist()
l.playPlaylist()
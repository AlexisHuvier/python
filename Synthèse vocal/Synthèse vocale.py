from gtts import gTTS
from time import sleep
import pyglet, os
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

phrase=input()

tts=gTTS(text=phrase, lang='fr')
tts.save("temp.mp3")

music = pyglet.media.load("temp.mp3", streaming=False)
music.play()

sleep(music.duration) #prevent from killing
os.remove("temp.mp3") #remove temperory file

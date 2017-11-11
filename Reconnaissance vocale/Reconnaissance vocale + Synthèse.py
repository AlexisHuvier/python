import speech_recognition as sr
from gtts import gTTS
from time import sleep
import pyglet, os
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True
 
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    
try:
    tts=gTTS(text=r.recognize_google(audio, language='fr-FR', show_all=False), lang='fr')
    tts.save("temp.mp3")
    music = pyglet.media.load("temp.mp3", streaming=False)
    music.play()
    sleep(music.duration) #prevent from killing
    os.remove("temp.mp3") #remove temperory file    
except LookupError:
    print('Cannot understand audio!')


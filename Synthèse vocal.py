from gtts import gTTS
import pygame, os, time

tts = gTTS(text="Bonjour, je suis un robot",lang="fr")
tts.save("test.mp3")
pygame.mixer.init()
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
pygame.mixer.music.stop()
time.sleep(2)
os.remove("test.mp3")

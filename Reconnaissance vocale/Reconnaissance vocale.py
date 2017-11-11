import speech_recognition as sr
 
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    
try:
    print(r.recognize_google(audio, language='fr-FR', show_all=False))    
except LookupError:
    print('Cannot understand audio!')


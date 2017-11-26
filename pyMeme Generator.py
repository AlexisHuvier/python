import urllib.request, webbrowser


meme = ["tanguy","buzz","doge","facepalm", "philosoraptor", "saltbae"]
while(True):
    print("#===== pyMeme Generator =====#")
    print("# Choix du meme de base :    #")
    print("#  1. Tanguy                 #")
    print("#  2. Buzz et Woody          #")
    print("#  3. Doge                   #")
    print("#  4. Facepalm               #")
    print("#  5. Raptor qui pense       #")
    print("#  6. Salt Bae               #")
    print("#============================#")
    print("")
    try:
        photo = int(input("Nombre correspondant au même : "))
        if(photo < 1 or photo > 6):
            0/0
    except:
        print("")
        print("ERREUR : Votre nombre n'en est pas un ou ne correspond pas à un meme")
        print("")
    else:
        break

print("")
phrase1 = input("Phrase 1 du meme : ")
phrase2 = input("Phrase 2 du meme : ")
phrase1 = phrase1.replace("_","__")
phrase1 = phrase1.replace(" ","_")
phrase1 = phrase1.replace("-","--")
phrase1 = phrase1.replace("weLoveMemes","we_love_memes")
phrase1 = phrase1.replace("?","~q")
phrase1 = phrase1.replace("%","~p")
phrase1 = phrase1.replace("#","~h")
phrase1 = phrase1.replace("/","~s")
phrase1 = phrase1.replace("\"","\'\'")
phrase2 = phrase2.replace("_","__")
phrase2 = phrase2.replace(" ","_")
phrase2 = phrase2.replace("-","--")
phrase2 = phrase2.replace("weLoveMemes","we_love_memes")
phrase2 = phrase2.replace("?","~q")
phrase2 = phrase2.replace("%","~p")
phrase2 = phrase2.replace("#","~h")
phrase2 = phrase2.replace("/","~s")
phrase2 = phrase2.replace("\"","\'\'")
webbrowser.open("http://memegen.link/"+meme[photo-1]+"/"+phrase1+"/"+phrase2+".jpg")
print("")
input("By LavaPower")

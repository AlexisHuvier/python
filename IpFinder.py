from re import findall
from requests import get

lang = input("Code de votre langue (ex : fr pour Francais) : ")
print("")
ConecLer = get('https://check.torproject.org/?lang='+lang).text
ip = findall('<strong>(.*?)</strong></p>', ConecLer)
text = findall('<p>(.*?) <strong>', ConecLer)
text2 = findall('<h1 class="off"> (.*?) </h1>', ConecLer)
for i in text:
    print(i)
for i in ip:
    print("\tIP: " + str(i))

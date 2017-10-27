from calendar import weekday as WD 
import calendar as C

def mise_en_forme(date): return '%04d/%02d/%02d' % (date.year,date.month,date.day)

def jour(date):
    jours='Lundi Mardi Mercredi Jeudi Vendredi Samedi Dimanche'.split(' ')
    a,m,j=[int(i) for i in date.split('/')]
    return jours[WD(a,m,j)]
    
def inv(d): return '/'.join(reversed(d.split('/')))    

def Paques(annee):  
    g , b , c = annee%19 , annee+(annee//4) , annee//100
    c4 , e =c//4 , (8*c+13)//25
    h=(19*g+c-c4-e+15)%30
    k , p , q = h//28 , (h+1)//13 , (21-g)//11
    i=(k*p*q-1)*k+h
    j1=(b+i+2+c4)-c
    j2=j1%7
    r=28+i-j2
    return ((4,r-31) if r>31 else (3,r))

fetes=["Jour de l'an", "Le 1er mai", "Le 8 mai", 'Le 14 Juillet', 
       "L'Assomption","La Toussaint", "Le 11 novembre", u"Le jour de NoÃ«l", 
       u"Le lundi de PÃ¢ques","L'Ascension", u"Le lundi de PentecÃ´te"]

dates=['01/01', '05/01', '05/08','07/14','08/15','11/01','11/11','12/25']

annee=int(input(u'\nSaisir une annÃ©e (aaaa) : '))
(m,j)=Paques(annee)                                    # Dimanche de PÃ¢cuqes
date=C.datetime.date(annee,m,j)
paques=mise_en_forme(date+C.datetime.timedelta( 1))    # Lundi de PÃ¢cuqes
ascension=mise_en_forme(date+C.datetime.timedelta(39)) # 39 jours aprÃ¨s PÃ¢ques
pentecote=mise_en_forme(date+C.datetime.timedelta(50)) # 50 jours aprÃ¨s PÃ¢ques
dates=['%4d/%s' % (annee,d) for d in dates]+[paques,ascension,pentecote]

resultat=sorted(zip(dates,fetes))

print (u"\nVoici les 11 jours de fÃªtes lÃ©gales en France de l'annÃ©e "+ str(annee)+" :\n")
for (d,f) in resultat:
    print (str(jour(d))+" "+str(inv(d))+" : "+f)
input()

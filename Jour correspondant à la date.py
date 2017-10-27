def jour(date):
    jours=['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi']
    code_mois=[0,3,3,6,1,4,6,2,5,0,3,5]
    j,m,a=date.split('/')
    j=int(j)
    m=int(m)
    a=int(a)-1900
    eps=1 if (a%400==0 or (a%4==0 and a%100!=0)) else 0
    r=(j+code_mois[m-1]+(a+a//4)-int(m<=2)*eps)%7
    return jours[r]

date=input("Entrez la date (JJ/MM/AAAA) : ")
print(date,' : ',jour(date))
input()


def Double(liste):
    listeFinal=[]
    for i in liste:
        if i in listeFinal:
            pass
        else:
            listeFinal.append(i)
    return listeFinal

def Mini(liste):
    minV=1000000
    for i in liste:
        if minV>i:
            minV=i
    return(minV)

def Range(liste):
    listefinal=[]
    while len(liste)!=0:
        minV=Mini(liste)
        liste.remove(minV)
        listefinal.append(minV)
    return(listefinal)
    

liste = [1,1,2,3,2,5,4,10,6,10.2,3,4,2,1]
print("La liste est : "+str(liste))
print("")
print("La liste sans double est : "+str(Double(liste)))
liste=Double(liste)
print("")
print("La liste triée est : "+str(Range(liste)))
input()

def Double(liste):
    listeFinal=[]
    for i in liste:
        if i in listeFinal:
            pass
        else:
            listeFinal.append(i)
    return listeFinal

liste = [1,1,2,3,2,5,4,3,4,2,1]
print("La liste est : "+str(liste))
print("")
print("La liste sans double est : "+str(Double(liste)))
input()

def Grand(liste):
    maxValue=0
    for i in liste:
        if maxValue <i:
            maxValue=i
    return maxValue

liste = [2,5,10,3,5, -100, 10.1]
print("La liste est : "+str(liste))
print("")
print("Le plus grand est : " + str(Grand(liste)))
input()

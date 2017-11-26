def pi(etape):
    I = 1
    result = 4/1
    for y in range(etape):
        z=4/(I+2)
        if(y%2 == 0):
            z=-z
        result += z
        I+=2
    return result

print(pi(int(input("Entrez la précision : "))))

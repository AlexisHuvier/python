def persistance(base,multi):
    strbase=str(base)
    base=1
    for i in strbase:
        base=base*int(i)
    multi+=1
    return(base,multi)

try:
    base=int(input("Entrez un nombre :"))
    if base < 0:
        base=-base
except:
    print("\n"+str(base)+" n'est pas un nombre.")
    input()
else:
    if len(str(base))==1:
        print("\n"+str(base)+" a une persistance multiplicative de 0")
        input()
    else:
        multi=0
        nombre=base
        while len(str(base))!=1:
            base, multi=persistance(base,multi)
        print("\n"+str(nombre)+" a une persistance multiplicative de "+str(multi))
        input()
    
        

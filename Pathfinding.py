################################################################################
#                                                                              #
#               Mise en evidence de l'algorithme A star graphiquement          #
#                                                                              #
################################################################################

from tkinter import *
from math import sqrt

class Noeud():
    """Chaque case du jeu est représentée par un objet noeud qui contient :
         - sa position dans la grille
         - son cout G : distance entre elle et son ascendant + cout G de son
           ascendant
         - son cout H : distance entre elle et le noeud final
         - son cout F : somme de G et H"""
    def __init__(self,x,y):
        self.colonne = x
        self.ligne = y
        self.coutF = 0
        self.coutG = 0
        self.coutH = 0
        self.parent = self
    
def Initialisation(event):
    """Création de la matrice(tabGrille) en fonction de la résolution
       Mise en place de la grille
       Mise en place de la case départ et finale et création de leur noeud
       associé"""
    global tabGrille,noeudDepart,noeudFinal,listeFermee,\
        listeOuverte,echelle,resolution,caseDepart,caseArrivee,\
        tabCasesChemin,tabCasesListeOuverte,tabCasesListeFermee

    grilleJeu.delete(ALL)
    tabGrille = []
    resolution = int(400 / echelle)
    for i in range(resolution):
        tabGrille.append([[]]*resolution)
    for ligne in range(resolution):
        for colonne in range(resolution):
            tabGrille[ligne][colonne] = 0
    for i in range(resolution):
        grilleJeu.create_line(i*echelle,0,i*echelle,400,fill='white')
    for i in range(resolution):
        grilleJeu.create_line(1,i*echelle,400,i*echelle,fill='white')

    noeudDepart = Noeud(0,0)
    caseDepart = grilleJeu.create_rectangle(noeudDepart.colonne*echelle,
                        noeudDepart.ligne*echelle,(noeudDepart.colonne*echelle)
                        +echelle,(noeudDepart.ligne*echelle)+echelle,
                        outline='white',fill='blue')
    noeudFinal = Noeud(resolution-1,resolution-1)
    caseArrivee = grilleJeu.create_rectangle(noeudFinal.colonne*echelle,
                        noeudFinal.ligne*echelle,(noeudFinal.colonne*echelle)
                        +echelle,(noeudFinal.ligne*echelle)+echelle,
                        outline='white',fill='green')
    listeFermee = []
    listeOuverte =  []
    tabCasesChemin = []
    tabCasesListeOuverte = []
    tabCasesListeFermee = []
    
##### Fonctions de l'algorithme ------------------------------------------------   
def Algorithme(event):
    """Boucle while principale :
        - on met le meilleur noeud de la liste ouverte dans la liste fermée
          et on appelle la fonction qui va chercher ses voisins
        - lorsque le meilleur noeud correspond au noeud final on sort de la
          boucle pour afficher le chemin
        - si le noeud final n'est pas atteint et si la liste des noeud à
          explorer est vide : il n'y a pas de solution"""
    global listeOuverte,listeFermee,noeudCourant,text,tabCasesListeOuverte,\
           tabCasesListeFermee,intervalTemps

    EffaceChemin('l')
    intervalTemps  = 250
    tabCasesListeOuverte = []
    tabCasesListeFermee = []
    listeOuverte = []
    listeFermee = []

    ###Initialistion du noeudCourant avec le noeud de départ
    noeudCourant = noeudDepart
    noeudCourant.coutH = Distance(noeudCourant,noeudFinal)
    noeudCourant.coutF = noeudCourant.coutH
    ###On le met dans la liste ouverte
    listeOuverte.append(noeudCourant)
      
    while (not(noeudCourant.ligne == noeudFinal.ligne and \
               noeudCourant.colonne == noeudFinal.colonne)\
           and listeOuverte != []):
        ### On choisi le meilleur noeud ce sera le noeud courant
        noeudCourant = MeilleurNoeud()
        AjouterListeFermee(noeudCourant)
        
        ##### petite animation ###
        ### création d'un carré correspondant au noeud courant en marron
        caseCourant = grilleJeu.create_rectangle(noeudCourant.colonne*echelle,
                                noeudCourant.ligne*echelle,(noeudCourant.colonne*echelle)+echelle,
                                (noeudCourant.ligne*echelle)+echelle,fill='maroon')
        fen.update()
        ### on passe le noeud courant précédent en gris
        fen.after(intervalTemps,CasesListeFermee())
        ### on ajoute l'actuel noeud courant à la liste des carrés les représentant 
        tabCasesListeFermee.append(caseCourant)
        grilleJeu.lift(caseDepart) 
        #########################

        ### On va chercher les voisins du noeud courant
        fen.after(intervalTemps,AjouterCasesAdjacentes(noeudCourant))

    ### on a atteint le noeud final        
    if noeudCourant.ligne == noeudFinal.ligne and noeudCourant.colonne == noeudFinal.colonne :
        RemonterListe()
    ### On a pas atteint le noeud final et il n'y a plus de noeud à explorer 
    elif listeOuverte == []:
        ### simple animation 
        text = menu.create_text(115,5,text="--- PAS DE SOLUTION ---",anchor=NW,font="Century 10 normal bold",fill='red')
        for i in range(2):
            fen.update()
            fen.after(250,Clignotement('hidden'))
            fen.update()
            fen.after(250,Clignotement('normal'))
        fen.update()
        fen.after(1000,Clignotement('hidden'))

def MeilleurNoeud():
    """Fonction qui renvoie le meilleur noeud de la liste ouverte en fonction
    de son cout en F"""
    cout = 5000000
    noeud = None
    for n in listeOuverte:
        if n.coutF < cout:
            cout = n.coutF
            noeud = n
    return noeud

def AjouterListeFermee(noeud):
    """Ajoute un noeud à la liste fermée et le supprime de la liste ouverte"""
    global listeOuverte,listeFermee

    listeFermee.append(noeud)
    listeOuverte.remove(noeud)

def AjouterCasesAdjacentes(noeudCourant):
    """Fonction qui cherche tous les voisins possibles au noeud courant passé
    en parametre."""
    global listeOuverte,listeFermee

    if choixDirections == 'huitPoints':
        ### les 8 déplacements possibles dans la matrice
        deplacements = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    elif choixDirections == 'quatrePoints':
        deplacements = [(-1,0),(0,1),(1,0),(0,-1)]        
    
    for direction in deplacements:
        coordSuivante = (noeudCourant.ligne + direction[0],
                         noeudCourant.colonne + direction[1])
        ###On vérifie qu'on sort pas de la matrice
        if coordSuivante[0] >= 0 and coordSuivante[0] <= len(tabGrille)-1 and\
        coordSuivante[1] >= 0 and coordSuivante[1] <= len(tabGrille[0])-1:
            ###On vérifie que le voisin n'est pas un obstacle (mur=2, vide=0)
            if tabGrille[coordSuivante[0]][coordSuivante[1]] == 0:
                ###On crée un objet noeud au coordonnée du voisin
                noeudTemp = Noeud(coordSuivante[1],coordSuivante[0])
                ###Le noeud courant sera son parent
                noeudTemp.parent = noeudCourant
                ###On s'assure que ce voisin ne fait pas deja parti de la liste fermée 
                if not DejaPresentDansListe(noeudTemp,listeFermee):
                    ###On calcule ses couts
                    noeudTemp.coutG = noeudTemp.parent.coutG + Distance(noeudTemp,noeudTemp.parent)
                    noeudTemp.coutH = Distance(noeudTemp,noeudFinal)
                    noeudTemp.coutF = noeudTemp.coutG + noeudTemp.coutH

                    n = DejaPresentDansListe(noeudTemp,listeOuverte)
                    ###Si ce voisin est deja présent dans la liste ouverte
                    if n != False:
                        ###On compare son cout G avec celui de la liste ouverte(n)
                        if noeudTemp.coutG < n.coutG:
                            ###Si il est inférieur on remplace les couts et le parent de n par ceux du voisin récemment trouvé
                            n.parent = noeudCourant
                            n.coutG = noeudTemp.coutG
                            n.coutH = noeudTemp.coutH
                            n.coutF = noeudTemp.coutF
                        ###Dans le cas contraire on ne change rien...

                    ###Ce voisin n'est pas déja présent dans le liste ouverte
                    ###donc on l'y ajoute
                    else:
                        listeOuverte.append(noeudTemp)
                        ###animation
                        fen.after(intervalTemps ,CasesListeOuverte(noeudTemp))
                        fen.update()                                                

def Distance(noeud1,noeud2):
    """Calcule des distances entre 2 noeuds suivant l'heuristique choisie"""
    a =  noeud2.ligne - noeud1.ligne
    b =  noeud2.colonne - noeud1.colonne
    if choixHeuristique == 'racineDistEucli':
        return sqrt((a*a) + (b*b))
    elif choixHeuristique == 'distanceEucli':
        return ((a*a) + (b*b))
    elif choixHeuristique == "distManhattan":
        return (abs(a)+abs(b))

def DejaPresentDansListe(noeud,liste):
    """Fonction qui cherche si un noeud est deja présent dans un liste"""
    for n in liste:
        if n.ligne == noeud.ligne and n.colonne == noeud.colonne:
            return n
    return False

### Fonctions d'animation -------------------------------------------------------    
def Clignotement(etat):
    """Fonction qui passe un texte d'un etat à un autre suivant son argument"""
    global text

    menu.itemconfigure(text,state=etat)

def CasesListeOuverte(n):
    """Dessin d'un carré pour tous les noeuds ajoutés à la liste ouverte"""
    tabCasesListeOuverte.append(grilleJeu.create_rectangle(n.colonne*echelle,
                                n.ligne*echelle,(n.colonne*echelle)+echelle,
                                (n.ligne*echelle)+echelle,fill='orange'))

def CasesListeFermee():
    """Passe le dernier élément de la liste des carrés représentants les noeuds
    de la liste ferméé en gris"""
    if tabCasesListeFermee!=[]:
        grilleJeu.itemconfigure(tabCasesListeFermee[-1],fill='SteelBlue')
        fen.update()
        
def RemonterListe():
    """Le but est atteint, cette fonction remonte le chemin d'ascendant en
    ascendant en partant du dernier noeud courant choisi"""
    global tabCasesChemin
    
    chemin = []
    tabCasesChemin = []
    n = listeFermee[-1]
    chemin.append(n)
    n = n.parent
    while n.parent != n:
        chemin.append(n)
        ### dans la foulée on crée des carrés pour chaque noeud appartenant au chemin gagnant
        tabCasesChemin.append(grilleJeu.create_rectangle(n.colonne*echelle,
                            n.ligne*echelle,(n.colonne*echelle)+echelle,
                            (n.ligne*echelle)+echelle,fill='red'))
        n = n.parent
    chemin.append(n)
    grilleJeu.lift(caseDepart)
    grilleJeu.lift(caseArrivee)

def EffaceChemin(event):
    """Efface toutes les cases correspondants au chemin gagnant à
       la liste ouverte et à la liste fermée"""
    if tabCasesChemin:
        for caseRouge in tabCasesChemin:
            grilleJeu.delete(caseRouge)
    if tabCasesListeOuverte:
        for caseOrange in tabCasesListeOuverte:
            grilleJeu.delete(caseOrange)
    if tabCasesListeFermee:
        for caseGrise in tabCasesListeFermee:
            grilleJeu.delete(caseGrise)

### Interface utilisateur ------------------------------------------------------
def Menu():
    """Création du menu"""
    global textRacineDistEucli,textDistEucli,textDistManhattan,textQuatrePtsCardinaux,textHuitPtsCardinaux
    
    menu.delete(ALL)
    menu.create_text(10,10,text="Menu",anchor=NW,font="Century 10 normal bold",fill='maroon')
    menu.create_text(10,25,text="T : Trouver Chemin ",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_text(10,40,text="L : Effacer Chemin",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_text(10,55,text="E : Tout Effacer ",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_text(10,80,text="-  : Baisser la Resolution",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_text(10,95,text="+ : Monter la Resolution",anchor=NW,font="Century 10 normal bold",fill='white')    
    menu.create_text(210,25,text="M : Ajouter Mur ",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_rectangle(355,28,365,38,outline='white',fill='black')
    menu.create_text(210,40,text="Clic Droit : Effacer Mur",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_text(210,65,text="D : Deplacer Depart",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_rectangle(355,68,365,78,outline='white',fill='blue')
    menu.create_text(210,80,text="A : Deplacer Arrivee",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_rectangle(355,83,365,93,outline='white',fill='green')
    menu.create_text(210,105,text="Directions",anchor=NW,font="Century 10 normal bold",fill='white')
    textQuatrePtsCardinaux = menu.create_text(210,120,text="4 : 4 points cardinaux",anchor=NW,font="Century 10 normal bold",fill='white')
    textHuitPtsCardinaux = menu.create_text(210,135,text="8 : 8 points cardinaux",anchor=NW,font="Century 10 normal bold",fill='red')
    menu.create_text(10,115,text="<- : Ralentir",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_text(10,130,text="-> : Accelerer",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_text(10,155,text="Noeuds liste ouverte",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_rectangle(160,158,170,168,outline='white',fill='orange')
    menu.create_text(10,170,text="Noeuds liste fermee",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_rectangle(160,173,170,183,outline='white',fill='steelblue')
    menu.create_text(10,185,text="Noeud courant",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_rectangle(160,188,170,198,outline='white',fill='maroon')
    menu.create_text(10,200,text="Chemin solution",anchor=NW,font="Century 10 normal bold",fill='white')
    menu.create_rectangle(160,203,170,213,outline='white',fill='red')    
    menu.create_text(210,155,text="Choix de l'heuristique",anchor=NW,font="Century 10 normal bold",fill='white')
    textRacineDistEucli = menu.create_text(210,170,text="1 : Racine Dist Euclidienne",anchor=NW,font="Century 10 normal bold",fill='red')
    textDistEucli = menu.create_text(210,185,text="2 : Distance Euclidienne",anchor=NW,font="Century 10 normal bold",fill='white')
    textDistManhattan = menu.create_text(210,200,text="3 : Distance Manhattan",anchor=NW,font="Century 10 normal bold",fill='white')    

def Position(event):
    """Positionne un mur, la case départ ou la case d'arrivée aux coordonnées de la souris"""
    global tabGrille,noeudDepart,noeudFinal

    EffaceChemin('l')
    if event.x > 0 and event.x < 400 and event.y > 0 and event.y < 400:
        indice_colonne = int(event.x / echelle)
        indice_ligne = int(event.y / echelle)
        if mode == 'mur':
            if (indice_colonne == noeudDepart.colonne and indice_ligne == noeudDepart.ligne) or\
               (indice_colonne == noeudFinal.colonne and indice_ligne == noeudFinal.ligne):
                return
            else:
                grilleJeu.create_rectangle(indice_colonne*echelle,indice_ligne*echelle,
                                           (indice_colonne*echelle)+echelle,
                                           (indice_ligne*echelle)+echelle,outline='white',fill='black')
                tabGrille[indice_ligne][indice_colonne] = 2

        if mode == 'depart':
            if tabGrille[indice_ligne][indice_colonne] == 0:
                grilleJeu.coords(caseDepart,indice_colonne*echelle,indice_ligne*echelle,
                                 (indice_colonne*echelle)+echelle,(indice_ligne*echelle)+echelle)
                grilleJeu.lift(caseDepart)
                noeudDepart = Noeud(indice_colonne,indice_ligne)

        if mode == 'arrivee':
            if tabGrille[indice_ligne][indice_colonne] != 2:
                grilleJeu.coords(caseArrivee,indice_colonne*echelle,indice_ligne*echelle,
                                 (indice_colonne*echelle)+echelle,(indice_ligne*echelle)+echelle)
                grilleJeu.lift(caseArrivee)
                noeudFinal = Noeud(indice_colonne,indice_ligne)

def EffacerMur(event):
    """Efface un mur"""
    global tabGrille
        
    EffaceChemin('l')
    if event.x > 0 and event.x < 400 and event.y > 0 and event.y < 400:
        indice_colonne = int(event.x / echelle)
        indice_ligne = int(event.y / echelle)
        if (indice_colonne == noeudDepart.colonne and indice_ligne == noeudDepart.colonne) or\
                (indice_colonne == noeudFinal.colonne and indice_ligne == noeudFinal.colonne):
            return
        else:
            grilleJeu.create_rectangle(indice_colonne*echelle,indice_ligne*echelle,
                                       (indice_colonne*echelle)+echelle,
                                       (indice_ligne*echelle)+echelle,outline='white',fill='wheat')
            tabGrille[indice_ligne][indice_colonne] = 0
    
def BougeDepart(event):
    """Passe la souris en mode déplacement de la case départ"""
    global mode

    EffaceChemin('l')
    mode = 'depart'

def BougeArrivee(event):
    """Passe la souris en mode déplacement de la case arrivée"""
    global mode

    EffaceChemin('l')
    mode = 'arrivee'
    
def Mur(event):
    """Passe la souris en mode création d'un mur"""
    global mode

    mode = 'mur'
    
def EchellePlus(event):
    """Baisse la résolution"""
    global indice,echelle

    indice += 1
    if indice > len(tableauEchelle)-1:
        indice = len(tableauEchelle)-1
    echelle = tableauEchelle[indice]
    Initialisation('e')

def EchelleMoins(event):
    """Agrandit la résolution"""
    global indice,echelle

    indice -= 1
    if indice < 0:
        indice = 0
    echelle = tableauEchelle[indice]
    Initialisation('e')

def Ralentir(event):
    """Ralentit la cadence"""
    global intervalTemps

    intervalTemps += 25
        
def Accelerer(event):
    """Accelère la cadence"""
    global intervalTemps

    intervalTemps -= 25

def ChoixHeuristique1(event):
    global choixHeuristique

    choixHeuristique = 'racineDistEucli'
    menu.itemconfigure(textRacineDistEucli,fill='red')
    menu.itemconfigure(textDistEucli,fill='white')    
    menu.itemconfigure(textDistManhattan,fill='white')
    
def ChoixHeuristique2(event):
    global choixHeuristique

    choixHeuristique = 'distanceEucli'
    menu.itemconfigure(textDistEucli,fill='red')
    menu.itemconfigure(textRacineDistEucli,fill='white')
    menu.itemconfigure(textDistManhattan,fill='white')
    
def ChoixHeuristique3(event):
    global choixHeuristique

    choixHeuristique = 'distManhattan'
    menu.itemconfigure(textDistManhattan,fill='red')
    menu.itemconfigure(textDistEucli,fill='white')
    menu.itemconfigure(textRacineDistEucli,fill='white')    

def ChoixQuatrePtsCardinaux(event):
    global choixDirections

    choixDirections = 'quatrePoints'
    menu.itemconfigure(textQuatrePtsCardinaux,fill='red')
    menu.itemconfigure(textHuitPtsCardinaux,fill='white')

def ChoixHuitPtsCardinaux(event):
    global choixDirections

    choixDirections = 'huitPoints'
    menu.itemconfigure(textQuatrePtsCardinaux,fill='white')
    menu.itemconfigure(textHuitPtsCardinaux,fill='red')

### ----------------------------------------------------------------------------    
fen = Tk()
fen.title("Algorithme A*")
fen.resizable(0,0)
tabGrille = []
grilleJeu = Canvas(fen,width=400,height=400,bg='wheat')
grilleJeu.grid(row=0,column=0)
menu = Canvas(fen,width=400,height=220,bg='DarkCyan')
menu.grid(row=1,column=0)
Menu()
grilleJeu.bind('<Button-1>',Position)
grilleJeu.bind("<B1-Motion>",Position)
grilleJeu.bind('<Button-3>',EffacerMur)
grilleJeu.bind("<B3-Motion>",EffacerMur)
fen.bind("t",Algorithme)
fen.bind('e',Initialisation)
fen.bind('l',EffaceChemin)
fen.bind('-',EchellePlus)
fen.bind('+',EchelleMoins)
mode = 'mur'
fen.bind('m',Mur)
fen.bind('d',BougeDepart)
fen.bind('a',BougeArrivee)
fen.bind('<Left>',Ralentir)
fen.bind('<Right>',Accelerer)
fen.bind('1',ChoixHeuristique1)
fen.bind('2',ChoixHeuristique2)
fen.bind('3',ChoixHeuristique3)
fen.bind('4',ChoixQuatrePtsCardinaux)
fen.bind('8',ChoixHuitPtsCardinaux)
tableauEchelle = [5,10,16,20,25,40]
indice = 1
choixHeuristique = 'racineDistEucli'
choixDirections = 'huitPoints'
echelle = tableauEchelle[indice]
Initialisation('e')
fen.mainloop()

from random import *

"""Deroulement : comment l'ia fonctionne
Donc on a deux listes :
grid : la ou on joue
available : places libres dans la liste

Qu'on soit d'accord, les croix et les ronds sont des strings.("X" et "O")
Ca veut dire que l'ia va choisir un entier entre 1 et 8 dans la liste available.
Si l'entier est présent dans la liste disponible
alors il place sa croix/rond
Pour éviter les conflits, chaque place choisi par l'ia et le joueur sera supprimé
de la liste disponible grâce à la méthode del()
"""

grille = [0,1,2,3,4,5,6,7,8]
disponible = [0,1,2,3,4,5,6,7,8]

Humain = None #Defini dans le main
Ai = None #Defini dans le main

tour = 0

while disponible != []:
        
    """Au tour du joueur"""

    #print(morpionnage(grille))
        
    #print(available)

    #print(morpionnage(grille))

    Choix_Joueur = int(input("Choisissez une place disponible : "))
        
    if Choix_Joueur in grille:
        #print("Il est la le frère.")
        grille[Choix_Joueur] = Humain
        #print(morpionnage(grille))
        del(disponible[Choix_Joueur-tour])
        #print(disponible)
        #print("Tour = ", tour)
        
        tour += 1


    """Au tour de l'IA"""


    #print(morpionnage(grille))

    Choix_ia = choice(disponible)
    #print("L'ia a choisi : ",Choix_ia)
    if Choix_ia in disponible:
        grille[Choix_ia-tour] = Ai
        del(disponible[Choix_ia-tour])

    tour += 1
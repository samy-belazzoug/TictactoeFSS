"""Formation de la grille"""

#Création de la grille
grille = [0,1,2,3,4,5,6,7,8]

def grille(liste:list):
    """Formatte la liste grille afin d'avoir 
    le morpion affiché dans le terminal."""
    print(
    f"{liste[6]} | {liste[7]} | {liste[8]}" "\n"
    "---------" "\n"
    f"{liste[3]} | {liste[4]} | {liste[5]}" "\n"
    "---------" "\n"
    f"{liste[0]} | {liste[1]} | {liste[2]}" "\n"
    )
import sys
from tkinter import messagebox

# PROJET 136 : MATRICE ARITHMETIQUE avec le terminal
matrice_1 = []
matrice_2 = []

# ---------------- Programme principal ----------------
def creer_matrice(n, m):
    matrice = []
    for i in range(n):
        ligne = []
        for j in range(m):
            valeur = int(input(f"Entrez l'élément ({i+1},{j+1}) : "))
            ligne.append(valeur)
        matrice.append(ligne)
    return matrice

def afficher_matrice(matrice):
    print("Matrice créée par les valeurs de l'utilisateur:")
    print("[")
    for ligne in matrice:
        print("[" + " ".join(map(str, ligne)) + "]")
    print("]")

def somme_deux_matrice(matrice_1, matrice_2):
    somme = []
    for i in range(len(matrice_1)):
        ligne = []
        for j in range(len(matrice_1[i])):
            ligne.append(matrice_1[i][j] + matrice_2[i][j])
        somme.append(ligne)
    return somme

def difference_deux_matrices(matrice_1, matrice_2):
    difference = []
    for i in range(len(matrice_1)):
        ligne = []
        for j in range(len(matrice_1[i])):
            ligne.append(matrice_1[i][j] - matrice_2[i][j])
        difference.append(ligne)
    return difference

def multiplication_deux_matrices(matrice_1, matrice_2):
    produit = []
    for i in range(len(matrice_1)):
        ligne = []
        for j in range(len(matrice_2[0])):
            somme = 0
            for k in range(len(matrice_1[0])):
                somme += matrice_1[i][k] * matrice_2[k][j]
            ligne.append(somme)
        produit.append(ligne)
    return produit

def inverser_matrice_gui():
    try:
        if len(entries) != 2 or len(entries[0]) != 2:
            messagebox.showerror("Erreur", "Uniquement pour une matrice 2x2")
            return

        matrice = [[float(e.get()) for e in ligne] for ligne in entries]

        inverse = inverse_matrice_2x2(matrice)

        resultat = "[\n"
        for ligne in inverse:
            resultat += " [" + " ".join(f"{x:.2f}" for x in ligne) + "]\n"
        resultat += "]"

        label_resultat.config(text=resultat)

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


#---------------- Exécuteur ----------------
input("Création de la matrice arithmétique.\n")
print("Combien de matrices doit elles etre créées ?")
num_matrices = int(input("Entrez le nombre de matrices à créer : "))
for k in range(num_matrices):
    print(f"\nCréation de la matrice {k+1}:")
    n = int(input("Entrez le nombre de lignes (n) : "))
    m = int(input("Entrez le nombre de colonnes (m) : "))
    matrice = creer_matrice(n, m)
    afficher_matrice(matrice)
    if k == 0:
        matrice_1 = matrice
    else:
        matrice_2 = matrice

somme_matrice = somme_deux_matrice(matrice_1, matrice_2)
print("La somme des deux matrices est :")
afficher_matrice(somme_matrice)

difference_matrice = difference_deux_matrices(matrice_1, matrice_2)
print("La différence des deux matrices est :")
afficher_matrice(difference_matrice)

produit_matrice = multiplication_deux_matrices(matrice_1, matrice_2)
print("Le produit des deux matrices est :")
afficher_matrice(produit_matrice)

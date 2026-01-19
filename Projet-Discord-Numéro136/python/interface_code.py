# Dans une interface graphique
import tkinter as tk
from tkinter import messagebox

# ---------------- FONCTIONS ----------------

def creer_champs():
    global entries
    try:
        n = int(entry_n.get())
        m = int(entry_m.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des entiers valides")
        return

    for widget in frame_matrice.winfo_children():
        widget.destroy()

    entries = []

    for i in range(n):
        ligne = []
        for j in range(m):
            e = tk.Entry(frame_matrice, width=5)
            e.grid(row=i, column=j, padx=5, pady=5)
            ligne.append(e)
        entries.append(ligne)

def afficher_matrice():
    try:
        matrice = []
        for ligne in entries:
            matrice.append([int(e.get()) for e in ligne])
    except ValueError:
        messagebox.showerror("Erreur", "Toutes les valeurs doivent être des entiers")
        return

    resultat = "[\n"
    for ligne in matrice:
        resultat += " [" + " ".join(map(str, ligne)) + "]\n"
    resultat += "]"

    label_resultat.config(text=resultat)

#---------------- INTERFACE ----------------

fenetre = tk.Tk()
fenetre.title("Création et affichage d'une matrice")

# Dimensions
tk.Label(fenetre, text="Nombre de lignes (n):").grid(row=0, column=0)
entry_n = tk.Entry(fenetre, width=5)
entry_n.grid(row=0, column=1)

tk.Label(fenetre, text="Nombre de colonnes (m):").grid(row=1, column=0)
entry_m = tk.Entry(fenetre, width=5)
entry_m.grid(row=1, column=1)

tk.Button(fenetre, text="Créer la matrice", command=creer_champs)\
    .grid(row=2, column=0, columnspan=2, pady=10)

# Zone de saisie matrice
frame_matrice = tk.Frame(fenetre)
frame_matrice.grid(row=3, column=0, columnspan=2)

# Bouton afficher
tk.Button(fenetre, text="Afficher la matrice", command=afficher_matrice)\
    .grid(row=4, column=0, columnspan=2, pady=10)

# Résultat
label_resultat = tk.Label(fenetre, text="", font=("Courier", 12), justify="left")
label_resultat.grid(row=5, column=0, columnspan=2)

fenetre.mainloop()

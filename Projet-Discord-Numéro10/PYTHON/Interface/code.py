import tkinter as tk
from tkinter import messagebox

taches = []

# -------- Fonctions --------
def ajouter_tache():
    tache = entry_tache.get()
    if tache:
        taches.append(tache)
        listbox.insert(tk.END, tache)
        entry_tache.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche")

def supprimer_tache():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        taches.pop(index)
    except:
        messagebox.showwarning("Erreur", "Sélectionnez une tâche à supprimer")

def modifier_tache():
    try:
        index = listbox.curselection()[0]
        nouvelle_tache = entry_tache.get()
        if nouvelle_tache:
            taches[index] = nouvelle_tache
            listbox.delete(index)
            listbox.insert(index, nouvelle_tache)
            entry_tache.delete(0, tk.END)
        else:
            messagebox.showwarning("Attention", "Entrez une nouvelle description")
    except:
        messagebox.showwarning("Erreur", "Sélectionnez une tâche à modifier")

# -------- Interface --------
fenetre = tk.Tk()
fenetre.title("To-Do List")
fenetre.geometry("400x400")

label = tk.Label(fenetre, text="To-Do List", font=("Arial", 16))
label.pack(pady=10)

entry_tache = tk.Entry(fenetre, width=40)
entry_tache.pack(pady=5)

btn_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_tache)
btn_ajouter.pack(pady=5)

btn_modifier = tk.Button(fenetre, text="Modifier", command=modifier_tache)
btn_modifier.pack(pady=5)

btn_supprimer = tk.Button(fenetre, text="Supprimer", command=supprimer_tache)
btn_supprimer.pack(pady=5)

listbox = tk.Listbox(fenetre, width=50)
listbox.pack(pady=10)

fenetre.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from core.generator import generate_password
from core.database import save_to_vault, load_vault

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("SafeVault - Gestionnaire de Mots de Passe")
        self.root.geometry("700x500")
        self.root.configure(bg="#2c3e50")

        self.setup_ui()

    def setup_ui(self):
        # --- TITRE ---
        header = tk.Label(self.root, text="MON COFFRE-FORT", font=("Arial", 18, "bold"), 
                          bg="#2c3e50", fg="#ecf0f1", pady=20)
        header.pack()

        # --- ZONE DE SAISIE ---
        input_frame = tk.LabelFrame(self.root, text=" Ajouter une entrée ", bg="#2c3e50", 
                                    fg="#3498db", padx=10, pady=10)
        input_frame.pack(pady=10, padx=20, fill="x")

        # Configuration des colonnes pour alignement
        tk.Label(input_frame, text="Site:", bg="#2c3e50", fg="white").grid(row=0, column=0, sticky="w")
        self.entry_site = tk.Entry(input_frame, width=25)
        self.entry_site.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Utilisateur:", bg="#2c3e50", fg="white").grid(row=0, column=2, sticky="w")
        self.entry_user = tk.Entry(input_frame, width=25)
        self.entry_user.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Mot de passe:", bg="#2c3e50", fg="white").grid(row=1, column=0, sticky="w")
        self.entry_pass = tk.Entry(input_frame, width=25, show="*")
        self.entry_pass.grid(row=1, column=1, padx=5, pady=5)

        # Bouton Générer
        self.btn_gen = tk.Button(input_frame, text="Générer", bg="#f39c12", fg="white", 
                                 command=self.fill_generated_password)
        self.btn_gen.grid(row=1, column=2, padx=5, pady=5)

        # Bouton Enregistrer
        self.btn_save = tk.Button(input_frame, text="Enregistrer", bg="#27ae60", fg="white", 
                                  command=self.save_entry, width=15)
        self.btn_save.grid(row=1, column=3, padx=5, pady=5)

        # --- TABLEAU D'AFFICHAGE ---
        self.setup_table()

    def setup_table(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#ecf0f1", fieldbackground="#ecf0f1", foreground="black")

        columns = ("site", "user", "pass")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("site", text="Site / Application")
        self.tree.heading("user", text="Identifiant")
        self.tree.heading("pass", text="Mot de Passe")
        
        self.tree.pack(pady=20, padx=20, fill="both", expand=True)

    def fill_generated_password(self):
        """Génère un mot de passe et l'insère dans le champ."""
        pw = generate_password()
        self.entry_pass.delete(0, tk.END)
        self.entry_pass.insert(0, pw)

    def save_entry(self):
        """Sauvegarde les données dans le fichier et met à jour l'affichage."""
        site = self.entry_site.get()
        user = self.entry_user.get()
        password = self.entry_pass.get()

        if site and user and password:
            # 1. Sauvegarde réelle dans le fichier via le core
            new_entry = {"site": site, "user": user, "password": password}
            save_to_vault(new_entry)
            
            # 2. Mise à jour visuelle dans le tableau
            self.tree.insert("", "end", values=(site, user, "••••••••"))
            
            # 3. Nettoyage des champs
            self.entry_site.delete(0, tk.END)
            self.entry_user.delete(0, tk.END)
            self.entry_pass.delete(0, tk.END)
            messagebox.showinfo("Succès", "Entrée sauvegardée dans le coffre !")
        else:
            messagebox.showwarning("Champs vides", "Veuillez remplir toutes les informations.")
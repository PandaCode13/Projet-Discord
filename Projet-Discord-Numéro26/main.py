import sys
import tkinter as tk
from ui.main_window import MainWindow

def main():
    # Initialisation de la fenêtre racine Tkinter
    root = tk.Tk()
    
    # On instancie notre classe MainWindow (qu'on va créer dans /ui)
    app = MainWindow(root)
    
    # Lancement de la boucle principale
    print("Démarrage du Password Manager...")
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nFermeture de l'application.")
        sys.exit(0)
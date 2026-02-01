import os

# Dossier racine du projet
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chemin vers le fichier de données (le coffre-fort)
VAULT_PATH = os.path.join(BASE_DIR, "data", "vault.db")

# Paramètres de sécurité (ne pas changer une fois la base créée)
SALT_SIZE = 16  # Taille du sel pour le hachage
ITERATIONS = 100_000  # Nombre d'itérations pour PBKDF2 (plus c'est haut, plus c'est lent/sûr)

# Créer le dossier data s'il n'existe pas
if not os.path.exists(os.path.join(BASE_DIR, "data")):
    os.makedirs(os.path.join(BASE_DIR, "data"))
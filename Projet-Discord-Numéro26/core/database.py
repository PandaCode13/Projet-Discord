import json
import os
from config import VAULT_PATH

def save_to_vault(new_data):
    """Sauvegarde une nouvelle entrée dans le fichier JSON."""
    data = load_vault()
    data.append(new_data)
    
    with open(VAULT_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_vault():
    """Charge les données depuis le fichier vault.db (JSON)."""
    if not os.path.exists(VAULT_PATH):
        return []
        
    try:
        with open(VAULT_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
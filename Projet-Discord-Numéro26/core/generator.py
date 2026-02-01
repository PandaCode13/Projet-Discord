import secrets
import string

def generate_password(length=16, use_symbols=True, use_numbers=True):
    """Génère un mot de passe robuste et aléatoire."""
    
    # On commence avec les lettres minuscules et majuscules
    characters = string.ascii_letters 
    
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_-+=<>?"

    # On s'assure que le mot de passe est généré de manière sécurisée
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password
taches = []

def AddTache():
    tache = input("Ajouter la tache: ")
    taches.append(tache)
    print(f"Taches : {tache} est ajouté dans la liste")

def ViewListTache():
    if not taches: 
        print("Vous n'avez pas de tâches enregistrés")
    else: 
        print("Les taches sont: ")
        for index, tache in enumerate(taches):
            print(f"Tache #{index}. {tache}")

def DeleteListTache():
    ViewListTache()
    try: 
        tacheSupprimé = int(input("Sélectionné la tâche que vous voulez supprimer:"))
        if tacheSupprimé >= 0 and tacheSupprimé < len(taches):
            taches.pop(tacheSupprimé)
            print(f"Tache {tacheSupprimé} est définitivement supprimé")
        else : 
            print(f"Tache {tacheSupprimé} n'existe pas")
    except:
        print("Erreur")

def marcarComoConcluida():
    listarTarefa()
    try:
        indiceTarefa = int(input("Selecione o número da tarefa que deseja marcar como concluída: "))
        if 0 <= indiceTarefa < len(tarefas):
            tarefas[indiceTarefa] += " (Concluída)"
            print(f"Tarefa #{indiceTarefa} marcada como concluída")
        else:
            print("Índice de tarefa inválido")
    except ValueError:
        print("Por favor, insira um número válido.")

print("To Do List Application")
while True : 
    print("\n")
    print("Bonjour Mr ou Mme. Veuillez sélectionnez une des optitons pour gérer votre todo list:")
    print("-----------------------------")
    print("1. Ajouter une tache")
    print("2. Supprimer une tache")
    print("3. Lister tous les taches")
    print("4. Modifier une tache")
    print("5. Quittez")
    
    choix = input("Entrez le numéro :")

    if choix == "1" :
        AddTache()
    elif choix == "2":
        DeleteListTache()
    elif choix == "3":
        ViewListTache()
    elif choix == "5":
        print("Au revoir")
        break;
    else : 
        print("Option invalidée")
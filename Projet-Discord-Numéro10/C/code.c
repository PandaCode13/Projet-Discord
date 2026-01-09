#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TACHES 100
#define MAX_LEN 100

char taches[MAX_TACHES][MAX_LEN];
int nbTaches = 0;

/* Supprimer le \n ajouté par fgets */
void enleverRetourLigne(char *str) {
    str[strcspn(str, "\n")] = '\0';
}

/* Ajouter une tâche */
void AddTache() {
    if (nbTaches >= MAX_TACHES) {
        printf("Liste pleine !\n");
        return;
    }

    printf("Ajouter la tache : ");
    fgets(taches[nbTaches], MAX_LEN, stdin);
    enleverRetourLigne(taches[nbTaches]);

    printf("Tache : \"%s\" est ajoutee dans la liste\n", taches[nbTaches]);
    nbTaches++;
}

/* Afficher la liste */
void ViewListTache() {
    if (nbTaches == 0) {
        printf("Vous n'avez pas de taches enregistrees\n");
        return;
    }

    printf("Les taches sont :\n");
    for (int i = 0; i < nbTaches; i++) {
        printf("Tache #%d : %s\n", i, taches[i]);
    }
}

/* Supprimer une tâche */
void DeleteListTache() {
    ViewListTache();

    if (nbTaches == 0) return;

    char buffer[10];
    int index;

    printf("Selectionnez la tache a supprimer : ");
    fgets(buffer, sizeof(buffer), stdin);
    index = atoi(buffer);

    if (index >= 0 && index < nbTaches) {
        for (int i = index; i < nbTaches - 1; i++) {
            strcpy(taches[i], taches[i + 1]);
        }
        nbTaches--;
        printf("Tache #%d supprimee avec succes\n", index);
    } else {
        printf("Tache inexistante\n");
    }
}

/* Modifier une tâche */
void EditTache() {
    ViewListTache();

    if (nbTaches == 0) return;

    char buffer[10];
    int index;

    printf("Selectionnez le numero de la tache a modifier : ");
    fgets(buffer, sizeof(buffer), stdin);
    index = atoi(buffer);

    if (index >= 0 && index < nbTaches) {
        printf("Inserez votre modification : ");
        fgets(taches[index], MAX_LEN, stdin);
        enleverRetourLigne(taches[index]);

        printf("Tache #%d modifiee avec succes\n", index);
    } else {
        printf("Indice invalide\n");
    }
}

/* Programme principal */
int main() {
    char choix[10];

    printf("To Do List Application\n");

    while (1) {
        printf("\n---------------------------------\n");
        printf("1. Ajouter une tache\n");
        printf("2. Supprimer une tache\n");
        printf("3. Lister les taches\n");
        printf("4. Modifier une tache\n");
        printf("5. Quitter\n");
        printf("Entrez le numero : ");

        fgets(choix, sizeof(choix), stdin);

        switch (choix[0]) {
            case '1': AddTache(); break;
            case '2': DeleteListTache(); break;
            case '3': ViewListTache(); break;
            case '4': EditTache(); break;
            case '5':
                printf("Au revoir\n");
                return 0;
            default:
                printf("Option invalide\n");
        }
    }
}

let taches = [];
let selectIndex = null;

const input = document.getElementById("taskInput");
const list = document.getElementById("taskList");

document.getElementById("addBtn").addEventListener("click", ajouterTache);
document.getElementById("editBtn").addEventListener("click", modifierTache);
document.getElementById("deleteBtn").addEventListener("click", supprimerTache);

function afficherTaches() {
    list.innerHTML="";
    taches.forEach((tache, index) => {
        const li = document.createElement("li");
        li.textContent = tache;

        li.onclick = () => {
            selectIndex = index;
            input.value = tache;
        };

        list.appendChild(li);
    });
}

function ajouterTache() {
    if(input.value.trim === "") {
        alert("veuillez une tache")
        return;
    }

    taches.push(input.value);
    input.value = "";
    afficherTaches();
}

function modifierTache() {
    if (selectIndex === null) {
        alert("selectionnez une tache");
        return;
    }

     if(input.value.trim === "") {
        alert("veuillez une tache")
        return;
    }

    taches[selectIndex] = input.value;
    selectIndex = null;
    input.value = "";
    afficherTaches();
}

function supprimerTache() {
    if (selectIndex === null) {
        alert("selectionnez une tache");
        return;
    }

    taches.splice(selectIndex, 1);
    selectIndex = null;
    afficherTaches();
}
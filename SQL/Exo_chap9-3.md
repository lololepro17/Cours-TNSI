# Exercice 3 : Création de la table Emprunt

On souhaite créer la table **Emprunt** à partir des informations fournies par la base de données bibliothèque. Cette table permettra de suivre les livres empruntés par les usagers.

Un employé propose le schéma relationnel suivant :  

**Emprunt**[Nom (string), Prénom (string), Auteur (string), Titre (string), DateEmprunt (date), EnRetard (booléen)]

---

## 1. Clé primaire proposée par l’employé

La clé primaire semble être composée des attributs suivants :  

- **Nom** et **Prénom**.  

**Problème :** Ce choix n'est pas judicieux, car deux personnes peuvent avoir le même nom et prénom. De plus, un même utilisateur peut emprunter plusieurs livres, ce qui provoquerait des doublons.

---

## 2. Proposition d'amélioration

Pour autoriser l’emprunt de plusieurs livres sans modifier en profondeur la relation **Emprunt**, on peut ajouter un **identifiant unique d’emprunt (`id_emprunt`)** comme clé primaire.  

**Nouvelle relation :**  
**Emprunt**[id_emprunt (int, clé primaire), Nom (string), Prénom (string), Auteur (string), Titre (string), DateEmprunt (date), EnRetard (booléen)]

Cela permet de garantir l’unicité des enregistrements, même si un utilisateur emprunte plusieurs livres.

---

## 3. Cas pratique avec Jean Dupont

### a) Attribut permettant de savoir si le livre est en retard

L’attribut **EnRetard** (booléen) permet de savoir si le livre n’a pas été rendu dans les temps.  

- Pour Jean Dupont : **EnRetard = TRUE**.

---

### b) Modification pour ajouter les contacts

M. Dupont se plaint de ne pas avoir été contacté par téléphone ou e-mail.  
Pour répondre à ce besoin, il faut modifier la relation pour inclure ces informations, tout en respectant le fait qu'elles ne sont pas obligatoires.

**Nouvelle relation :**  
**Emprunt**[id_emprunt (int, clé primaire), Nom (string), Prénom (string), Auteur (string), Titre (string), DateEmprunt (date), EnRetard (booléen), Téléphone (char(10), nullable), Email (string, nullable)]

---

### c) Schéma relationnel plus concis

Pour simplifier encore plus la relation et éviter des malentendus, on peut regrouper les informations utilisateur dans une table séparée, en utilisant une relation entre **Client** et **Emprunt**.

1. **Client**[id_client (int, clé primaire), Nom (string), Prénom (string), Téléphone (char(10), nullable), Email (string, nullable)]  
2. **Emprunt**[id_emprunt (int, clé primaire), id_client (int, clé étrangère), Auteur (string), Titre (string), DateEmprunt (date), EnRetard (booléen)]

Cela permet de centraliser les informations personnelles et de réduire les redondances.

---

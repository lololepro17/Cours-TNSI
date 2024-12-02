# Exercice 2 : Création de la table Client

On souhaite créer la table **Client** à partir des informations fournies par la base de données bibliothèque.

Monsieur Jean Dupont habite **5 grande rue, 25000 Besançon**. Son téléphone est le **03 81 01 02 03** et son mail est **<j.dupont@libertysurf.com>**. En tant qu'habitant de la ville de Besançon, il bénéficie d’un tarif préférentiel pour son adhésion.

---

## 1. Schéma relationnel de la table Client

Le schéma relationnel de la table **Client** est sa :  

| **Attribut**          | **Type**         | **Description**                           |
|------------------------|------------------|-------------------------------------------|
| `id_client`           | INT             | Identifiant unique du client (clé primaire). |
| `nom`                 | STR             | Nom du client.                            |
| `prenom`              | STR             | Prénom du client.                         |
| `adresse`             | STR             | Adresse complète du client.               |
| `ville`               | STR             | Ville du client.                          |
| `code_postal`         | INT             | Code postal du client.                    |
| `telephone`           | STR             | Numéro de téléphone du client.            |
| `email`               | STR             | Adresse e-mail du client (peut être Null).|
| `tarif_preferentiel`  | BOOLEAN         | Indique si le client bénéficie d’un tarif préférentiel. |

**Clé primaire :** `id_client`.

---

## 2. Degré de la relation Client

Le degré de la relation **Client** correspond au nombre d’attributs dans la table.  
**Degré : 8**.

---

## 3. Clé primaire de la relation Client

La clé primaire de la relation est **`id_client`**, un identifiant unique permettant de différencier les clients, même si certains peuvent avoir des noms identiques.

---

## 4. Représentation de la table Client

Voici une représentation de la table **Client** avec trois occurrences, dont une sans e-mail :  

| id_client | nom        | prenom    | adresse              | ville      | code_postal | telephone   | email                  | tarif_preferentiel |
|-----------|------------|-----------|----------------------|------------|-------------|-------------|------------------------|--------------------|
| 1         | Dupont     | Jean      | 5 grande rue         | Besançon   | 25000       | 0381010203  | <j.dupont@libertysurf.com> | TRUE              |
| 2         | Martin     | Claire    | 12 rue des Lilas     | Dijon      | 21000       | 0380123456  | <claire.martin@mail.com>  | FALSE             |
| 3         | Petit      | Marc      | 9 rue de l'Église    | Belfort    | 90000       | 0381123456  | Null                   | FALSE             |

# Exercice : Gestion des réservations dans une compagnie d'hôtels

Le modèle Entités/Associations pour gérer les réservations dans une compagnie d’hôtels est structuré en plusieurs entités liées entre elles par des associations. Nous allons détailler le schéma relationnel et analyser le cas de la suppression d'un client.

---

## 1. Schéma relationnel de la base de données "compagne d’hôtels"

### Table `Client`

| **Attribut**       | **Type**           | **Description**                               |
|--------------------|--------------------|-----------------------------------------------|
| `id_client`        | INT                | Identifiant unique du client (clé primaire)   |
| `Nom`              | STRING             | Nom du client                                 |
| `Prénom`           | STRING             | Prénom du client                              |
| `Adresse`          | STRING             | Adresse du client                             |
| `Téléphone`        | STRING             | Numéro de téléphone du client (nullable)      |
| `Email`            | STRING             | E-mail du client (nullable)                   |

---

### Table `Réservation`

| **Attribut**       | **Type**           | **Description**                               |
|--------------------|--------------------|-----------------------------------------------|
| `id_réservation`   | INT                | Identifiant unique de la réservation (clé primaire) |
| `id_client`        | INT                | Référence à l'identifiant du client (clé étrangère) |
| `id_chambre`       | INT                | Référence à l'identifiant de la chambre réservée (clé étrangère) |
| `DateRéservation`  | DATE               | Date de la réservation                        |
| `DateDébut`        | DATE               | Date de début du séjour                       |
| `DateFin`          | DATE               | Date de fin du séjour                         |

---

### Table `Chambre`

| **Attribut**       | **Type**           | **Description**                               |
|--------------------|--------------------|-----------------------------------------------|
| `id_chambre`       | INT                | Identifiant unique de la chambre (clé primaire) |
| `numéro`           | STRING             | Numéro de la chambre                          |
| `type`             | STRING             | Type de chambre (simple, double, suite, etc.) |
| `disponibilité`    | BOOLEAN            | Indique si la chambre est disponible (TRUE/FALSE) |

---

## 2. Suppression du client "Jean Dupont"

Lorsqu'un employé essaie de supprimer le client "Jean Dupont" en saisissant "Jean DuponD" (avec un "D" à la place du "T"), l'action sera refusée pour la raison suivante :

### Explication

Le modèle relationnel repose sur des identifiants uniques, comme l’**id_client** dans la table **Client**, pour assurer que chaque client soit distinct dans la base de données. La recherche pour la suppression d’un client ne peut pas être réalisée sur des noms et prénoms partiels ou incorrects, car ces attributs (comme "Nom" et "Prénom") peuvent contenir des variations orthographiques, des fautes de frappe ou des homonymes.

Dans ce cas précis, la recherche sur le nom "Jean DuponD" ne correspond pas exactement à "Jean Dupont" en raison de la différence dans l'orthographe. Comme cette action concerne une suppression, la base de données peut être configurée pour ne pas autoriser des suppressions basées sur des informations non uniques ou incorrectes. Cela garantit qu’un client valide n'est pas accidentellement supprimé à cause d’une petite erreur de saisie.

### Solution

Pour effectuer cette suppression, l'employé devrait soit saisir l'identifiant unique du client (**id_client**) qui est garanti d’être unique, soit corriger l'orthographe du nom et du prénom en s'assurant qu'ils correspondent exactement à l’enregistrement dans la base de données.

---

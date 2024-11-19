
# Résolution des exercices de modélisation

## Exercice 1

### Modifier le schéma pour

1. Un véhicule peut être couvert par plusieurs contrats.
2. Associer à chaque véhicule impliqué dans un accident un pourcentage de responsabilité.

```mermaid
erDiagram
    VEHICULE {
        string numero
        string marque
        string modele
    }
    CONTRAT {
        string idContrat
        string type
        date debut
        date fin
    }
    ACCIDENT {
        string idAccident
        date dateAccident
    }
    VEHICULE ||--o{ CONTRAT : "Couvert"
    VEHICULE ||--o{ ACCIDENT : "Impliqué"
    ACCIDENT {
        float pourcentageResponsabilite
    }
```

---

## Exercice 2

### Modifier le schéma pour préciser qu’un service traite un dossier si un de ses employés est en charge

```mermaid
erDiagram
    SERVICE {
        string idService
        string nomService
    }
    EMPLOYE {
        string idEmploye
        string nomEmploye
    }
    DOSSIER {
        string idDossier
        string description
    }
    SERVICE ||--o{ EMPLOYE : "Emploie"
    EMPLOYE ||--o{ DOSSIER : "Traite"
```

---

## Exercice 3

### Représenter

1. La réservation d’un ouvrage par un emprunteur.
2. L’historique des emprunts d’ouvrages.

```mermaid
erDiagram
    EMPRUNTEUR {
        string idEmprunteur
        string nom
    }
    OUVRAGE {
        string idOuvrage
        string titre
    }
    RESERVATION {
        date dateReservation
    }
    EMPRUNT {
        date dateEmprunt
        date dateRetour
    }
    EMPRUNTEUR ||--o{ RESERVATION : "Réserve"
    RESERVATION ||--o{ OUVRAGE : "Sur"
    EMPRUNTEUR ||--o{ EMPRUNT : "Effectue"
    EMPRUNT ||--o{ OUVRAGE : "Sur"
```

---

## Exercice 4

### Représenter une plateforme vidéo proposant des films en location ou achat

```mermaid
erDiagram
    MEMBRE {
        string idMembre
        string nom
        string adresse
        string telephone
    }
    FILM {
        string idFilm
        string titre
        string realisateur
        string acteurVedette
        string genre
    }
    VENTE {
        string typeVente
        date dateTransaction
    }
    MEMBRE ||--o{ VENTE : "Effectue"
    VENTE ||--o{ FILM : "Sur"
```

---

## Exercice 5

### Représenter les patients, visites, prescriptions dans un hôpital

```mermaid
erDiagram
    PATIENT {
        string idPatient
        string nom
        string prenom
        string adresse
    }
    SERVICE {
        string idService
        string nom
        string localisation
        string specialite
    }
    MEDECIN {
        string idMedecin
        string nom
        string prenom
    }
    VISITE {
        date dateVisite
    }
    PRESCRIPTION {
        string nomMedicament
        string posologie
    }
    PATIENT ||--o{ VISITE : "Effectue"
    VISITE ||--o{ MEDECIN : "Chez"
    VISITE ||--o{ PRESCRIPTION : "Donne lieu"
    MEDECIN ||--o{ SERVICE : "Appartient"
```

---

## Exercice 6

### Représenter le fonctionnement d’une entreprise de distribution

```mermaid
erDiagram
    VEHICULE {
        string idVehicule
        int capacite
        string conducteur
    }
    TOURNEE {
        string idTournee
        date dateTournee
        float longueur
    }
    COLIS {
        string idColis
        float poids
    }
    DESTINATAIRE {
        string idDestinataire
        string nom
        string adresse
    }
    VEHICULE ||--o{ TOURNEE : "Effectue"
    TOURNEE ||--o{ COLIS : "Emporte"
    COLIS ||--o{ DESTINATAIRE : "Pour"
```

---

## Exercice 7

### Représenter une société de formation

```mermaid
erDiagram
    SEMINAIRE {
        string idSeminaire
        string theme
        float tarif
    }
    SESSION {
        string idSession
        date dateSession
        int maxParticipants
    }
    ENTREPRISE {
        string idEntreprise
        string nom
        string adresse
    }
    EMPLOYE {
        string idEmploye
        string nom
    }
    ENTREPRISE ||--o{ EMPLOYE : "Emploie"
    EMPLOYE ||--o{ SESSION : "Participe"
    SESSION ||--o{ SEMINAIRE : "Se rapporte"
```

---

## Exercice 8

### Normaliser le schéma

**Schéma initial :**

- Table : **DEPARTEMENT**
  - Attributs : Entreprise, Adresse, Responsable, Téléphone.

**Dépendances fonctionnelles :**

1. **Entreprise → Adresse, Responsable**
2. **Responsable → Téléphone**

#### **Étapes de normalisation :**

1. **1NF (Première forme normale)** : Pas de groupes de valeurs multiples.
   - Les données sont déjà atomiques.

2. **2NF (Deuxième forme normale)** : Suppression des dépendances partielles.
   - Diviser la table en deux :
     - **Entreprise(Entreprise, Adresse, Responsable)**
     - **Responsable(Responsable, Téléphone)**

3. **3NF (Troisième forme normale)** : Suppression des dépendances transitives.
   - Chaque attribut dépend directement de la clé primaire.

**Schéma final :**

- **Table Entreprise** : Clé primaire : `Entreprise`.
  - Attributs : Adresse, Responsable.
- **Table Responsable** : Clé primaire : `Responsable`.
  - Attributs : Téléphone.

---

## Exercice 9

### Construire le schéma des tables correspondant au concept

**Structure administrative donnée :**

1. **Entités principales :**
   - **Département** : ID_Departement (clé primaire), Nom, Responsable.
   - **Employé** : ID_Employé (clé primaire), Nom, ID_Departement (clé étrangère).
   - **Projet** : ID_Projet (clé primaire), Nom.

2. **Relations :**
   - Un département a plusieurs employés.
   - Un employé peut participer à plusieurs projets.

**Schéma relationnel :**

- **Table Département** :
  - Attributs : ID_Departement (PK), Nom, Responsable.

- **Table Employé** :
  - Attributs : ID_Employé (PK), Nom, ID_Departement (FK).

- **Table Projet** :
  - Attributs : ID_Projet (PK), Nom.

- **Table Participation** :
  - Attributs : ID_Employé (FK), ID_Projet (FK).

```mermaid
erDiagram
    DEPARTEMENT {
        string idDepartement PK
        string nom
        string responsable
    }
    EMPLOYE {
        string idEmploye PK
        string nom
        string idDepartement FK
    }
    PROJET {
        string idProjet PK
        string nom
    }
    PARTICIPATION {
        string idEmploye FK
        string idProjet FK
    }
    DEPARTEMENT ||--o{ EMPLOYE : "Possède"
    EMPLOYE ||--o{ PARTICIPATION : "Participe"
    PROJET ||--o{ PARTICIPATION : "A"
```

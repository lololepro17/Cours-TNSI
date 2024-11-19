
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

1. **1NF :** Suppression des groupes de valeurs multiples.
2. **2NF :** Élimination des dépendances partielles.
3. **3NF :** Élimination des dépendances transitives.

---

## Exercice 9

### Construire le schéma des tables correspondant au concept

1. Définir chaque entité avec clé primaire.
2. Relier les entités via des clés étrangères selon les associations décrites.

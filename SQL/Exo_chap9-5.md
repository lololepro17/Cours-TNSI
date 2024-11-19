### 1. Modèle relationnel de l’association *Prescrire* entre les entités

L'association *Prescrire* relie deux entités principales dans un cabinet médical : **Médecin** et **Médicament**. Dans le modèle relationnel, cela se traduit par une table d'association **Prescrire** qui contient des références (clés étrangères) vers les entités **Médecin** et **Médicament**.

#### Table `Médecin`

| **Attribut**       | **Type**           | **Description**                                |
|--------------------|--------------------|------------------------------------------------|
| `id_medecin`       | INT                | Identifiant unique du médecin (clé primaire)   |
| `Nom`              | STRING             | Nom du médecin                                 |
| `Prénom`           | STRING             | Prénom du médecin                              |
| `Spécialité`       | STRING             | Spécialité du médecin                          |

---

#### Table `Médicament`

| **Attribut**       | **Type**           | **Description**                                |
|--------------------|--------------------|------------------------------------------------|
| `id_médicament`    | INT                | Identifiant unique du médicament (clé primaire)|
| `Nom`              | STRING             | Nom du médicament                              |
| `Dosage`           | STRING             | Dosage du médicament                           |

---

#### Table `Prescrire`

| **Attribut**       | **Type**           | **Description**                                |
|--------------------|--------------------|------------------------------------------------|
| `id_prescription`  | INT                | Identifiant unique de la prescription (clé primaire) |
| `id_medecin`       | INT                | Référence à l'identifiant du médecin (clé étrangère) |
| `id_médicament`    | INT                | Référence à l'identifiant du médicament (clé étrangère) |
| `Date_prescription`| DATE               | Date de la prescription                        |

---

### 2. Anomalies dans la relation *Consultation*

#### Données de la table `Consultation`

| **Numero** | **Matricule** | **Numero_SS**         | **Médicament** | **Date_consult** |
|------------|---------------|-----------------------|----------------|------------------|
| 1          | 123           |                       |                | 21/11/2019       |
| 2          | 123           | 182086926825812       | Aspirine       | 13/03/2019       |

#### Anomalies constatées :

1. **Absence de numéro de sécurité sociale dans la première ligne** :
   - Le numéro de sécurité sociale est vide pour la première ligne. Cela semble être une anomalie, car le numéro de sécurité sociale devrait être présent pour chaque patient.

2. **Matricule du médecin** :
   - Le matricule du médecin est identique dans les deux lignes (123). Il est important de vérifier que chaque consultation est correctement associée au médecin concerné et que le matricule est bien unique.

3. **Données manquantes pour le médicament dans la première consultation** :
   - La colonne "Médicament" est vide dans la première consultation, ce qui pourrait signifier qu'aucun médicament n'a été prescrit. Il faut clarifier si cela est une exception ou s'il y a un problème dans les données.

4. **Format inconsistant des dates** :
   - Les dates semblent cohérentes, mais il est important de vérifier si le format des dates est uniforme dans toute la base de données.

#### Correction suggérée :

- Compléter le numéro de sécurité sociale manquant pour la première ligne.
- Vérifier la validité du matricule du médecin et s'assurer qu'il est unique.
- S'assurer qu'une prescription de médicament est associée à chaque consultation, ou justifier les cas où il n'y en a pas.

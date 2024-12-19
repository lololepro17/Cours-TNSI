import sqlite3
import pandas as pd

# Chemin vers votre fichier CSV et le fichier SQLite
csv_file = "accidentsVelo.csv"  # Remplacez par le chemin de votre fichier CSV
db_file = "accidentsVelo.sqlite3"  # Nom du fichier SQLite

# Charger le fichier CSV avec pandas
    df = pd.read_csv(csv_file, sep=",")  # Ajustez le séparateur si nécessaire (par exemple, ";" au lieu de ",")
    print(f"CSV chargé avec {len(df)} lignes et {len(df.columns)} colonnes.")
except Exception as e:
    print(f"Erreur lors du chargement du fichier CSV : {e}")
    exit()

# Connexion à SQLite (fichier .sqlite3)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Création de la table en fonction des colonnes du CSV
columns = ", ".join([f"{col} TEXT" for col in df.columns])  # Par défaut, toutes les colonnes sont TEXT
create_table_query = f"CREATE TABLE IF NOT EXISTS accidents ({columns});"
try:
    cursor.execute(create_table_query)
    print(f"Table 'accidents' créée dans {db_file}.")
except Exception as e:
    print(f"Erreur lors de la création de la table : {e}")
    conn.close()
    exit()

# Insertion des données du CSV dans la table SQLite
try:
    df.to_sql("accidents", conn, if_exists="append", index=False)
    print(f"Données insérées dans la table 'accidents' dans {db_file}.")
except Exception as e:
    print(f"Erreur lors de l'insertion des données : {e}")
    conn.close()
    exit()

# Vérification des données insérées
try:
    cursor.execute("SELECT * FROM accidents LIMIT 5;")
    rows = cursor.fetchall()
    print("Exemple de données insérées :")
    for row in rows:
        print(row)
except Exception as e:
    print(f"Erreur lors de la lecture des données : {e}")

# Fermeture de la connexion
conn.close()
print(f"Base SQLite enregistrée avec succès dans {db_file}.")

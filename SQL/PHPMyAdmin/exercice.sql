-- Requêtes SQL pour la base de données `monde`

-- Instructions et gestion de la base de données
USE monde;

-- Affichage du schéma des tables
-- Pourquoi y a-t-il deux attributs signalés comme clé primaire ?
-- "CodePays" et "Langue" sont nécessaires pour éviter des doublons.
DESCRIBE Pays;
DESCRIBE LanguePays;

-- Lecture des tables
SELECT * FROM Pays;

-- Requêtes simples sur les données des pays

-- Afficher le nom, le code et le continent des pays
SELECT Nom, Code, Continent FROM Pays;

-- Afficher le nom, le code et renommer le chef de l'état
-- Utilisation de "AS" pour renommer une colonne dans les résultats.
SELECT Nom, Code, ChefEtat AS TeteExecutif FROM Pays;

-- Trouver les pays où le français est une langue officielle
-- On filtre les données en fonction de la langue.
SELECT CodePays FROM LanguePays WHERE Langue = 'Français';

-- Filtrer les pays selon l'espérance de vie
SELECT * FROM Pays WHERE EspeVie BETWEEN 78 AND 80;
SELECT Nom FROM Pays WHERE Continent = 'Afrique' AND EspeVie < 50;

-- Espérance de vie et population par continent
SELECT EspeVie, Nom, Population FROM Pays 
WHERE (Continent = 'Asie' OR Continent = 'Europe') AND EspeVie > 80;

-- Gouvernance monarchique
SELECT * FROM Pays WHERE TypeGouvernance LIKE '%monarch%';

-- Tri des pays d'Océanie par espérance de vie décroissante
SELECT Nom FROM Pays WHERE Continent = 'Océanie' ORDER BY EspeVie DESC;

-- Modifications et ajouts de données

-- Mise à jour du chef d'état pour la France et ses collectivités
UPDATE Pays SET ChefEtat = 'Emmanuel Macron' WHERE TypeGouvernance LIKE '%France%';

-- Ajout d'une nouvelle langue
INSERT INTO LanguePays (CodePays, Langue, Officielle, PourcentageParlants) 
VALUES ('FRA', 'langue de bois', 0, 43.1);

-- Vérification des langues parlées en France
SELECT Langue FROM LanguePays WHERE CodePays = 'FRA';

-- Suppression de la langue ajoutée
DELETE FROM LanguePays WHERE Langue = 'langue de bois';

-- Requêtes avec jointures

SELECT Ville.Nom AS NomVille, Ville.CodePays 
FROM Ville 
INNER JOIN Pays ON Ville.Nom = Pays.Nom;

-- Afficher le nom des villes avec leur pays
SELECT Ville.Nom AS NomVille, Pays.Nom AS NomPays 
FROM Ville 
INNER JOIN Pays ON Pays.Code = Ville.CodePays;

-- Villes en Amérique du Sud triées par nom
SELECT Ville.Nom AS NomVille, Pays.Nom AS NomPays 
FROM Ville 
INNER JOIN Pays ON Pays.Code = Ville.CodePays 
WHERE Pays.Continent = 'Amérique du Sud' 
ORDER BY Ville.Nom ASC;

-- Villes dans des pays où Elisabeth II est chef d'état
SELECT Ville.Nom AS NomVille, Pays.Nom AS NomPays 
FROM Ville 
INNER JOIN Pays ON Pays.Code = Ville.CodePays 
WHERE Pays.ChefEtat = 'Elisabeth II';

-- Langues officielles des pays d'Amérique du Sud
SELECT Pays.Nom AS NomPays, LanguePays.Langue AS LangueOfficielle 
FROM Pays 
INNER JOIN LanguePays ON Pays.Code = LanguePays.CodePays 
WHERE Pays.Continent = 'Amérique du Sud' 
ORDER BY Pays.Nom ASC;

-- Villes des pays francophones
SELECT Ville.Nom AS NomVille, Pays.Nom AS NomPays 
FROM Ville 
INNER JOIN Pays ON Pays.Code = Ville.CodePays 
INNER JOIN LanguePays ON Pays.Code = LanguePays.CodePays 
WHERE LanguePays.Langue = 'Français';

-- Comptages et statistiques

-- Nombre total de villes
SELECT COUNT(*) AS NombreVilles FROM Ville;

-- Nombre de pays en Océanie
SELECT COUNT(*) AS NombrePaysOceanie FROM Pays WHERE Continent = 'Océanie';

-- Nombre de langues officielles différentes
SELECT COUNT(DISTINCT Langue) AS NombreLanguesOfficielles 
FROM LanguePays 
WHERE Officielle = 1;

-- Pays avec la plus grande espérance de vie
SELECT Nom AS Pays, EspeVie AS EsperanceDeVie
FROM Pays
WHERE EspeVie = (SELECT MAX(EspeVie) FROM Pays);

-- Pays d'Asie avec la plus petite espérance de vie
SELECT Nom AS Pays, EspeVie AS EsperanceDeVie
FROM Pays
WHERE Continent = 'Asie' AND EspeVie = (SELECT MIN(EspeVie) FROM Pays WHERE Continent = 'Asie');

-- Pays d'Asie avec la plus petite espérance de vie
SELECT Nom AS Pays, EspeVie AS EsperanceDeVie 
FROM Pays 
WHERE Continent = 'Asie' 
ORDER BY EspeVie ASC 
LIMIT 1;

-- Codes de pays selon les langues parlées

-- Codes des pays où l'on parle français
SELECT DISTINCT CodePays FROM LanguePays WHERE Langue = 'Français';

-- Codes des pays où l'on parle anglais
SELECT DISTINCT CodePays FROM LanguePays WHERE Langue = 'Anglais';

-- Codes des pays où l'on parle français ou anglais
SELECT DISTINCT CodePays FROM LanguePays WHERE Langue = 'Français' OR Langue = 'Anglais';

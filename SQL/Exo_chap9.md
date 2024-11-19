# Exercice 1

## Énoncé

Dans la base de données d’un magasin, on considère l’association suivante :

| Entité       | Attributs                             |
|--------------|---------------------------------------|
| **Article**  | NumArticle (clé primaire), Désignation, Prix |
| **Commande** | NumCommande (clé primaire), DateCommande      |
| **Contenir** | Quantité                              |

---

## 1. Décrire l’association avec le détail des entités mises en relation

L'association **Contenir** relie :  
- L'entité **Article**, qui représente les articles vendus, identifiés par leur **NumArticle**.  
- L'entité **Commande**, qui représente les commandes passées par les clients, identifiées par leur **NumCommande**.  
- **Contenir** décrit la relation entre ces deux entités et précise la quantité d’un article commandé pour une commande donnée.

### Schéma relationnel
- **Article** (*NumArticle*, Désignation, Prix)  
- **Commande** (*NumCommande*, DateCommande)  
- **Contenir** (*NumArticle, NumCommande*, Quantité)  

*(Les deux clés primaires des entités sont utilisées comme clé primaire de la relation "Contenir".)*  

---

## 2. Où pourrait-on déplacer l’attribut "Quantité" dans le schéma ? Quel est l’intérêt de le laisser dans l’association "Contenir" ?

- **Déplacer "Quantité"** : On pourrait déplacer **Quantité** directement dans la table **Commande**, mais cela entraînerait une redondance si plusieurs articles sont commandés dans une même commande.  
- **Intérêt de laisser "Quantité" dans "Contenir"** : Cela permet d'associer une quantité spécifique à chaque article pour une commande donnée. Ainsi, une commande peut inclure plusieurs articles avec des quantités différentes.  

---

## 3. Décrire avec les cardinalités les deux sens de l’association

1. **Commande → Contenir → Article**  
   - Une commande peut contenir plusieurs articles → Cardinalité = (1,n).  
2. **Article → Contenir → Commande**  
   - Un article peut apparaître dans plusieurs commandes → Cardinalité = (0,n).  

### Schéma UML

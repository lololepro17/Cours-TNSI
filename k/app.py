def k_plus_proches_voisins(table, cible, k) :
    """Renvoie la liste des $k$ plus proches voisins de la cible"""

    def distance_cible(donnee) :
        """ renvoie la distance entre la donnée et la cible"""
        # Assuming Euclidean distance for this example
        return sum((d - c) ** 2 for d, c in zip(donnee, cible)) ** 0.5

    # On trie la table de manière croissante en utilisant la distance comme critère.
    table_triee = sorted(table, key = distance_cible)

    # gestion de la liste des k plus proches voisins
    proches_voisins = []  # initialisation vide
    for i in range(k) :
        proches_voisins.append(table_triee[i])  # On ajoute les $k$ premières valeurs

    return proches_voisins  # On renvoie la liste des $k$ plus proches voisins.
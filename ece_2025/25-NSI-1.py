def voisins_entrants(adj, x):
    '''Renvoie la liste des voisins entrants de x dans le graphe orienté adj.'''
    voisins = []
    for i in range(len(adj)):
        if adj [i] and x in adj[i]:
            voisins.append(i)
    if x < 0 or x >= len(adj):
        raise ValueError("Le sommet x est hors des limites du graphe.")
    return voisins

#print(voisins_entrants([[1, 2], [2], [0], [0]], 0))

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += str(compte) + chiffre
            compte = 1
            chiffre = s[i]
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre
    return resultat

print(nombre_suivant('1211'))

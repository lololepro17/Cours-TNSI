def max_et_indice(tab:list[int]):  
    '''
    Renvoie le maximum de tab et son indice
    '''
    if not tab:
        raise ValueError("La liste ne peut pas être vide.")
    max_value = tab[0]
    for i in range(len(tab)):
        if tab[i] > max_value:
            max_value = tab[i]
            indice = i
    return max_value, indice

# print( max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))




def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = [] 

    for x in tab:
        if x < 1 or x >n or x in vus: 
            return False
        vus.append(x) 
    return True

# print(est_un_ordre([1, 6, 2, 8, 3, 7])) # False

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre), "ordre n'est pas un ordre de gènes"
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < n - 1: 
        # l'écart n'est pas 1
        if ordre[i + 1] - ordre[i]  not in [-1, 1]:
            nb = nb + 1
        i = i + 1
    if ordre[-1] != n: # le dernier n'est pas n 
        nb = nb + 1
    return nb

#print( nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))

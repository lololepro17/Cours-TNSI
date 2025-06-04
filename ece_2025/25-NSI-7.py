def nbr_occurrences(chaine:str, lettre:str) -> int:
    """""Compte le nombre d'occurence d'un caractere dans une chaine."""
    caractere = {}
    for c in chaine:
        if c in caractere:
            caractere[c] += 1
        else:
            caractere[c] = 1
    return caractere.get(lettre,0)


# print(nbr_occurrences("Hello World !", "o")) # 2



def fusion(tab1,tab2):
    '''Fusionne deux tableaux triés et renvoie
    le nouveau tableau trié.'''
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2: 
        if tab1[i1] < tab2[i2]:
            tab12[i] = tab1[i1]
            i1 += 1
        else:
            tab12[i] = tab2[i2]
            i2 += 1
        i += 1
    while i1 < n1:
        tab12[i] = tab1[i1] 
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        tab12[i] = tab2[i2] 
        i2 = i2 + 1
        i = i + 1
    return tab12

print(fusion([1, 3, 5], [2, 4, 6])) # [1, 2, 3, 4, 5, 6]
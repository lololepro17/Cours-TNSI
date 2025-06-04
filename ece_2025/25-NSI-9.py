def multiplication(a, b):
    """
    a : entier
    b : entier
    La fonction renvoie le produit de a et b
    """
    if b == 0:
        return 0
    else:
        return a + multiplication(a, b - 1)











def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = fin/2 + debut // 2
        m = int(m)
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

print(dichotomie([1, 2, 3, 4, 5], 3))  # True
print(dichotomie([1, 2, 3, 4, 5], 6))  # False
print(multiplication(3, 4))  # 12





















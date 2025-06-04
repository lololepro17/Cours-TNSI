def maximum_tableau(tab:list) -> int:
    '''Renvoie le maximum d'un tableau de nombres entiers.'''
    assert len(tab) > 0, "Le tableau ne doit pas être vide."
    max_val = tab[0]
    for i in range(len(tab)):
        if tab[i] > max_val:
            max_val = tab[i]
    return max_val
# print(maximum_tableau([1, 2, 3, 4, 5]))


class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch 
    est bien parenthésée"""
    p = Pile()
    for c in ch:
        if c == "(": 
            p.empiler(c)
        elif c == ")": 
            if p.est_vide():
                return False
            else:
                p.depiler()
    return True if p.est_vide() else False
print(bon_parenthesage("((()))"))  # True
print(bon_parenthesage("(()"))  # False 



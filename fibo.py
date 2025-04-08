def rendu_glouton(somme, pieces):
    def rendu_glouton(P, s):
        ''' 
        In : une liste P d'entiers triée par ordre décroissant et un entier s
        Out: liste de pièces de P dont la somme vaut s renvoyée par l'algo glouton
        '''
        rendu = []
        for piece in P:
            while s >= piece:
                s -= piece
                rendu.append(piece)
        return rendu


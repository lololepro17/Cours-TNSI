def analyse_complexite(code: str) -> str:
    """
    Analyse la complexité algorithmique d'un code Python
    Args:
        code (str): Code Python sous forme de chaîne de caractères
    Returns:
        str: Estimation de la complexité
    """
    # Compteurs pour différentes structures
    boucles_imbriquees = 0
    max_boucles_imbriquees = 0
    boucles_courantes = 0
    
    # Analyse ligne par ligne
    lignes = code.split('\n')
    for ligne in lignes:
        ligne = ligne.strip()
        
        # Détection des boucles
        if 'for' in ligne or 'while' in ligne:
            boucles_courantes += 1
            max_boucles_imbriquees = max(max_boucles_imbriquees, boucles_courantes)
        
        # Détection des fins de blocs
        elif ligne.startswith('}') or (ligne.strip() == '' and boucles_courantes > 0):
            boucles_courantes = max(0, boucles_courantes - 1)
    
    # Détermination de la complexité
    if max_boucles_imbriquees == 0:
        return "O(1) - Complexité constante"
    elif max_boucles_imbriquees == 1:
        return "O(n) - Complexité linéaire"
    elif max_boucles_imbriquees == 2:
        return "O(n²) - Complexité quadratique"
    elif max_boucles_imbriquees > 2:
        return f"O(n^{max_boucles_imbriquees}) - Complexité polynomiale"

# Exemple d'utilisation
if __name__ == "__main__":
    code_exemple = """
    def exemple():
        for i in range(n):
            for j in range(n):
                for g in range(n)
                print(i, j)
    """
    
    print(analyse_complexite(code_exemple))
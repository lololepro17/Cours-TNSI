def tri_selection(liste: list) -> list:
    n = len(liste)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j
        liste[i], liste[indice_min] = liste[indice_min], liste[i]
    return liste

liste_test = [64, 25, 12, 22, 11]
resultat = tri_selection(liste_test.copy())
assert resultat == [11, 12, 22, 25, 64], f"Erreur: attendu [11, 12, 22, 25, 64] obtenu {resultat}"

assert tri_selection([]) == [], "Erreur: la liste vide doit retourner une liste vide."

liste_triee = [1, 2, 3, 4, 5]
assert tri_selection(liste_triee.copy()) == [1, 2, 3, 4, 5], "Erreur: la liste déjà triée est incorrecte."

liste_doublons = [3, 1, 2, 1]
assert tri_selection(liste_doublons.copy()) == [1, 1, 2, 3], "Erreur: le tri des doublons est incorrect."

liste_negatifs = [3, -2, 7, -5, 0]
assert tri_selection(liste_negatifs.copy()) == [-5, -2, 0, 3, 7], "Erreur: le tri des nombres négatifs est incorrect."

print("Tous les tests sont passés avec succès!")

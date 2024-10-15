import turtle as t
import random


def tracer(longueur: int, épaisseur: int = 5, couleur: str = "blue"):
    """Dessine un trait d'une certaine longueur, épaisseur et couleur avec turtle."""
    assert isinstance(longueur, (int, float)), "La longueur doit être un nombre."
    t.pensize(épaisseur)  # Définit l'épaisseur du trait
    t.color(couleur)  # Définit la couleur du trait
    t.forward(longueur)  # Avance d'une longueur spécifiée


def trace_lsysteme(mot: str, angle: int = 90, échelle: int = 1):
    """Trace un dessin correspondant aux instructions dans 'mot' selon un angle et une échelle donnés."""
    longueur = 10 * échelle
    t.width(0.2)
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    for instruction in mot:
        if instruction in "AB":
            tracer(longueur)
        elif instruction == "g":
            t.left(angle)
        elif instruction == "d":
            t.right(angle)

    t.hideturtle()
    t.done()


def remplacer_1(mot: str, lettre: str, motif: str) -> str:
    """Remplace toutes les occurrences de 'lettre' par 'motif' dans la chaîne 'mot'."""
    résultat = ""
    for caractère in mot:
        if caractère == lettre:
            résultat += motif
        else:
            résultat += caractère
    return résultat


def itérer_lsysteme_1(départ: str, règle: tuple, k: int) -> str:
    """Renvoie le k-ème itéré du L-système basé sur un mot initial et une règle donnée."""
    lettre, motif = règle
    mot = départ
    for _ in range(k):
        mot = remplacer_1(mot, lettre, motif)
    return mot


def tracer_flocon_Koch_full(départ: str, règle: tuple, n: int):
    """Trace les itérations du flocon de Koch pour k de 1 à n."""
    for k in range(1, n + 1):
        mot = itérer_lsysteme_1(départ, règle, k)
        trace_lsysteme(mot, angle=90, échelle=1)
        t.clear()
        t.reset()


def tracer_flocon_Koch_rules():
    """Fonction pour tracer les images du flocon de Koch avec différentes règles."""
    départ = "A"
    règles = [
        ("A", "AdAgAgAAdAdAgA"),
        ("A", "AgAAdAAdAdAgAgAAdAdAgAgAAgAAdA"),
        ("A", "AAdAdAdAdAA"),
        ("A", "AAdAddAdA"),
        ("A", "AAdAdAdAdAdAgA"),
        ("A", "AAdAgAdAdAA"),
        ("A", "AdAAddAdA"),
        ("A", "AdAgAdAdA"),
    ]

    for règle in règles:
        print(
            f"Traçage avec la règle : {règle}"
        )  # Affiche la règle utilisée pour le traçage
        for k in range(1, 6):
            mot = itérer_lsysteme_1(
                départ, règle, k
            )  # Génère un mot avec le départ et la règle souhaitée
            trace_lsysteme(mot, angle=90, échelle=1)  # Trace le motif
            t.clear()  # Efface le dessin
            t.reset()  # Réinitialise la tortue et son orientation


def générer_génome_aléatoire() -> tuple:
    """Génère un génome aléatoire pour le L-système."""
    lettres_possibles = ["A", "B", "g", "d"]
    départ = random.choice(lettres_possibles)
    motif = "".join(
        random.choice(lettres_possibles) for _ in range(random.randint(3, 10))
    )
    return départ, motif


def générer_lsysteme_aléatoire(nb_itérations: int = 5):
    """Génère et trace un L-système aléatoire en fonction d'un nombre d'itérations spécifié."""
    départ, règle = générer_génome_aléatoire()
    print(f"Génome aléatoire généré : Départ = {départ}, Règle = {règle}")
    for k in range(1, nb_itérations + 1):
        mot = itérer_lsysteme_1(départ, règle, k)
        trace_lsysteme(mot, angle=90, échelle=1)
        t.clear()
        t.reset()


def remplacer_2_nul(
    mot: str, lettre1: str, motif1: str, lettre2: str, motif2: str
) -> str:
    """Permets de remplacer la première lettre par le premier motif puis la deuxième lettre par le second motif. Cette fonction n'est pas celle demander mais je la laisse quand même."""
    mot_modifier1 = mot.replace(lettre1, motif1)  # remplace la lettre par la chaîne
    mot_modifier2 = mot_modifier1.replace(
        lettre2, motif2
    )  # Puis recommence avec la deuxième lettre et la deuxième chaîne
    return mot_modifier2  # Renvoie un résultat erronée par rapport aux attentes


def remplacer_2(mot: str, lettre1: str, motif1: str, lettre2: str, motif2: str) -> str:
    """Remplace les lettres par leurs motifs en même temps."""
    résultat = ""  # Initialise le résultat final
    for caractère in mot:
        if caractère == lettre1:
            résultat += motif1  # Ajoute le motif correspondant à la première lettre
        elif caractère == lettre2:
            résultat += motif2  # Ajoute le motif correspondant à la seconde lettre
        else:
            résultat += caractère  # Ajoute le caractère en l’état s'il n'est pas utilisé dans une règle
    return résultat


def itérer_lsysteme_2(départ: str, règle1: tuple, règle2: tuple, k: int) -> str:
    """Calcule le k-ème itéré du L-système en utilisant deux règles de transformation."""
    mot = départ  # Mot de départ
    lettre1, motif1 = règle1  # Première règle
    lettre2, motif2 = règle2  # Seconde règle

    for _ in range(k):
        mot = remplacer_2(
            mot, lettre1, motif1, lettre2, motif2
        )  # Applique les règles k fois

    return mot


def tracer_Sierpiński(
    départ: str = "AdBdB",
    règle1: tuple = ("A", "AdBgAgBdA"),
    règle2: tuple = ("B", "BB"),
    itérations: int = 4,
    angle: int = -120,
    échelle: int = 1,
):
    """Trace les premières images du triangle de Sierpiński en suivant les itérations du L-système."""
    for k in range(1, itérations + 1):
        mot = itérer_lsysteme_2(
            départ, règle1, règle2, k
        )  # Génère le mot avec les règles demandées
        print(f"Itération {k}: {mot}")  # Affiche ce que ça dessine en direct
        trace_lsysteme(
            mot, angle=angle, échelle=échelle
        )  # Trace le système correspondant


def tracer_dragon(k: int = 10):
    """Cette fonction trace la courbe du dragon."""
    départ_dragon = "AX"  # Notre départ selon l’énoncé
    règle1_dragon = ("X", "XgYAg")  # Première règle d’après l’énoncé
    règle2_dragon = ("Y", "dAXdY")  # Seconde règle d'après l'énoncé

    # Génère le mot pour la courbe du dragon
    mot_dragon = itérer_lsysteme_2(départ_dragon, règle1_dragon, règle2_dragon, k)

    print(
        f"Mot de la courbe du dragon pour k={k}: {mot_dragon}"
    )  # Affiche le mot généré

    # Trace le mot généré
    trace_lsysteme(mot_dragon, angle=90, échelle=1)


def tracer_variante_triangle_Sierpiński(k: int = 5):
    """Cette fonction trace la variante du triangle de Sierpiński."""
    départ_triangle = "A"  # Notre départ selon l’énoncé
    règle1_triangle = ("A", "BdAdB")  # Première règle d’après l’énoncé
    règle2_triangle = ("B", "AgBgA")  # Seconde règle d'après l'énoncé

    # Génère le mot pour la variante du triangle de Sierpiński
    mot_triangle = itérer_lsysteme_2(
        départ_triangle, règle1_triangle, règle2_triangle, k
    )

    print(
        f"Mot de la variante du triangle de Sierpiński pour k={k}: {mot_triangle}"
    )  # Affiche le mot généré

    # Trace le mot généré
    trace_lsysteme(mot_triangle, angle=60, échelle=1)


def tracer_Gosper():
    """Cette fonction trace la courbe de Gosper."""
    départ_Gosper = "A"  # Notre départ selon l’énoncé
    règle1_Gosper = ("A", "AgBggBdAddAAdBg")  # Première règle d’après l’énoncé
    règle2_Gosper = ("B", "dAgBBggBgAddAdB")  # Seconde règle d'après l'énoncé

    # Génère le mot pour la courbe de Gosper
    mot_Gosper = itérer_lsysteme_2(
        départ_Gosper, règle1_Gosper, règle2_Gosper, k=5
    )  # Exemple pour k=5

    # Affiche le mot généré pour le débogage
    print(f"Mot de la courbe de Gosper pour k=5: {mot_Gosper}")

    # Trace le mot généré
    trace_lsysteme(mot_Gosper, angle=60, échelle=1)


def générer_génome_aléatoire(nb_règles: int = 2):
    """Génère un génome aléatoire pour le L-système avec plusieurs règles."""

    lettres_possibles = ["A", "B", "g", "d"]  # Lettres utilisées pour le mot
    règles = []  # Initialisation des règles

    for _ in range(nb_règles):
        départ = random.choice(
            lettres_possibles
        )  # Sélectionne une lettre de départ aléatoire

        longueur_motif = random.randint(3, 10)  # Longueur du motif entre 3 et 10
        motif = "".join(
            random.choice(lettres_possibles) for _ in range(longueur_motif)
        )  # Génère un motif aléatoire

        règles.append((départ, motif))  # Ajoute la règle à la liste

    return règles


def générer_lsysteme_aléatoire(nb_itérations: int = 5, nb_règles: int = 2):
    """Génère et trace un L-système aléatoire sur un nombre d'itérations spécifié."""

    règles = générer_génome_aléatoire(nb_règles)  # Créer des règles aléatoires
    print(
        f"Génome aléatoire généré avec {nb_règles} règles : {règles}"
    )  # Affiche les règles à l'utilisateur

    # Initialisation avec un départ aléatoire
    départ = random.choice([règle[0] for règle in règles])

    mot = départ  # Initialise le mot avec le départ

    for k in range(1, nb_itérations + 1):
        for _ in range(k):  # Appliquer les règles k fois
            for règle in règles:
                mot = mot.replace(règle[0], règle[1])  # Remplacer selon les règles

        print(f"Itération {k}: {mot}")  # Affiche le mot pour chaque itération
        trace_lsysteme(mot, angle=90, échelle=1)  # Trace le mot
        t.clear()  # Efface la tortue
        t.reset()  # Réinitialise la tortue


#### Test ####
assert remplacer_1("AdBgd", "d", "AdB") == "AAdBBgAdB", "Erreur dans remplacer_1."
assert (
    itérer_lsysteme_1("AdBgdA", ("A", "Bg"), 5) == "BgdBgdBg"
), "Erreur dans itérer_lsysteme_1"
assert (
    remplacer_2("AdBdBagA", "A", "Bg", "g", "dAgBA") == "BgdBdBadAgBABg"
), "Erreur dans _remplacer_2"
assert (
    itérer_lsysteme_2("AdBgB", ("A", "Bg"), ("d", "BgdA"), 5)
    == "BgBgBgBgBgBgdABgBgBgBgBgB",
    "Erreur dans itérer_lsysteme",
)

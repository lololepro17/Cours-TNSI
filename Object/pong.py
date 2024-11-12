import pyxel

# Dimensions de la fenêtre et du jeu
LARGEUR_ECRAN = 160
HAUTEUR_ECRAN = 120
LARGEUR_RAQUETTE = 4
HAUTEUR_RAQUETTE = 20
VITESSE_RAQUETTE = 3
TROU_DU_BALLON = 1  # La marge pour marquer un point

# Classe pour le Joueur 1
class Joueur1:
    def __init__(self):
        self.x = 10
        self.y = HAUTEUR_ECRAN // 2 - HAUTEUR_RAQUETTE // 2
        self.touche_haut = pyxel.KEY_Z
        self.touche_bas = pyxel.KEY_S
        self.score = 0

    def mouvement(self):
        """Déplace la raquette du joueur 1 en fonction des touches Z et S"""
        if pyxel.btn(self.touche_haut) and self.y > 0:
            self.y -= VITESSE_RAQUETTE
        if pyxel.btn(self.touche_bas) and self.y < HAUTEUR_ECRAN - HAUTEUR_RAQUETTE:
            self.y += VITESSE_RAQUETTE

    def afficher(self):
        """Affiche la raquette du joueur 1"""
        pyxel.rect(self.x, self.y, LARGEUR_RAQUETTE, HAUTEUR_RAQUETTE, 9)

# Classe pour le Joueur 2
class Joueur2:
    def __init__(self):
        self.x = LARGEUR_ECRAN - 10 - LARGEUR_RAQUETTE
        self.y = HAUTEUR_ECRAN // 2 - HAUTEUR_RAQUETTE // 2
        self.touche_haut = pyxel.KEY_UP
        self.touche_bas = pyxel.KEY_DOWN
        self.score = 0

    def mouvement(self):
        """Déplace la raquette du joueur 2 en fonction des touches Haut et Bas"""
        if pyxel.btn(self.touche_haut) and self.y > 0:
            self.y -= VITESSE_RAQUETTE
        if pyxel.btn(self.touche_bas) and self.y < HAUTEUR_ECRAN - HAUTEUR_RAQUETTE:
            self.y += VITESSE_RAQUETTE

    def afficher(self):
        """Affiche la raquette du joueur 2"""
        pyxel.rect(self.x, self.y, LARGEUR_RAQUETTE, HAUTEUR_RAQUETTE, 9)

# Classe pour la Balle
class Balle:
    def __init__(self):
        self.x = LARGEUR_ECRAN // 2
        self.y = HAUTEUR_ECRAN // 2
        self.vitesse_x = 2
        self.vitesse_y = 2
        self.taille = 4

    def deplacer(self):
        """Déplace la balle selon sa vitesse actuelle"""
        self.x += self.vitesse_x
        self.y += self.vitesse_y

        # Rebond sur les murs haut et bas
        if self.y <= 0 or self.y >= HAUTEUR_ECRAN - self.taille:
            self.vitesse_y *= -1

    def afficher(self):
        """Affiche la balle à l'écran"""
        pyxel.rect(self.x, self.y, self.taille, self.taille, 7)

    def reset(self):
        """Réinitialise la balle au centre de l'écran et inverse sa direction"""
        self.x = LARGEUR_ECRAN // 2
        self.y = HAUTEUR_ECRAN // 2
        self.vitesse_x *= -1  # Change la direction de la balle

# Classe principale du Jeu Pong
class Jeu:
    def __init__(self):
        # Initialisation de la fenêtre
        pyxel.init(LARGEUR_ECRAN, HAUTEUR_ECRAN, title="Pong à 2 Joueurs")

        # Création des joueurs et de la balle
        self.joueur1 = Joueur1()
        self.joueur2 = Joueur2()
        self.balle = Balle()

        # Lance la boucle de jeu Pyxel
        pyxel.run(self.update, self.draw)

    def update(self):
        """Met à jour les éléments du jeu pour chaque image"""
        
        # Mouvement des raquettes
        self.joueur1.mouvement()
        self.joueur2.mouvement()

        # Déplacement de la balle
        self.balle.deplacer()

        # Collision avec les raquettes
        if (self.balle.x <= self.joueur1.x + LARGEUR_RAQUETTE and
            self.joueur1.y < self.balle.y < self.joueur1.y + HAUTEUR_RAQUETTE):
            self.balle.vitesse_x *= -1

        if (self.balle.x >= self.joueur2.x - self.balle.taille and
            self.joueur2.y < self.balle.y < self.joueur2.y + HAUTEUR_RAQUETTE):
            self.balle.vitesse_x *= -1

        # Vérifie si un joueur a marqué un point
        if self.balle.x < TROU_DU_BALLON:
            self.joueur2.score += 1
            self.balle.reset()

        if self.balle.x > LARGEUR_ECRAN - TROU_DU_BALLON:
            self.joueur1.score += 1
            self.balle.reset()

    def draw(self):
        """Affiche les éléments du jeu pour chaque image"""
        
        # Efface l'écran
        pyxel.cls(0)

        # Affiche les raquettes et la balle
        self.joueur1.afficher()
        self.joueur2.afficher()
        self.balle.afficher()

        # Affiche les scores
        pyxel.text(5, 5, f"Joueur 1: {self.joueur1.score}", 7)
        pyxel.text(LARGEUR_ECRAN - 45, 5, f"Joueur 2: {self.joueur2.score}", 7)

        # Quitte le jeu quand on appuie sur Q
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

# Lancement du jeu
Jeu()

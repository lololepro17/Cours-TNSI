import pyxel
import random


# Dimensions de la fenetre
LARGEUR_ECRAN = 160
HAUTEUR_ECRAN = 120


# Classe du Jeu
class Jeu:
    def __init__(self):
        # Init fenetre Pyxel
        pyxel.init(LARGEUR_ECRAN, HAUTEUR_ECRAN, title="Jeu d'Évitement")

        # Position de base du joueur
        self.joueur_x = LARGEUR_ECRAN // 2
        self.joueur_y = HAUTEUR_ECRAN - 10
        self.joueur_taille = 8

        # Position et vitesse de l'obstacle de base
        self.obstacle_x = random.randint(0, LARGEUR_ECRAN - 10)
        self.obstacle_y = 0
        self.obstacle_taille = 8
        self.obstacle_vitesse = 2

        # Score du joueur a l'init
        self.score = 0
        self.game_over = False

        # Demarer la boucle du jeu 
        pyxel.run(self.update, self.draw)

    def update(self):
        """Mise a jour de chaque elements de la fenetre"""
        if not self.game_over:
            # Mouvement du joueur (gauche/droite)
            if pyxel.btn(pyxel.KEY_LEFT) and self.joueur_x > 0:
                self.joueur_x -= 2
            if pyxel.btn(pyxel.KEY_RIGHT) and self.joueur_x < LARGEUR_ECRAN - self.joueur_taille:
                self.joueur_x += 2

            # Mise à jour de la position de l'obstacle
            self.obstacle_y += self.obstacle_vitesse

            # Réinitialisation de l'obstacle en haut lorsqu'il sort de l'écran
            if self.obstacle_y > HAUTEUR_ECRAN:
                self.obstacle_y = 0
                self.obstacle_x = random.randint(0, LARGEUR_ECRAN - self.obstacle_taille)
                self.score += 1
                self.obstacle_vitesse += 0.2  # Augmente la difficulté

            # Vérification de la collision
            if (self.joueur_x < self.obstacle_x + self.obstacle_taille and
                self.joueur_x + self.joueur_taille > self.obstacle_x and
                self.joueur_y < self.obstacle_y + self.obstacle_taille and
                self.joueur_y + self.joueur_taille > self.obstacle_y):
                self.game_over = True

    def draw(self):
        """Redessine l'ecran """
        # Efface l'écran
        pyxel.cls(0)

        # Affiche le joueur
        pyxel.rect(self.joueur_x, self.joueur_y, self.joueur_taille, self.joueur_taille, 9)

        # Affiche l'obstacle
        pyxel.rect(self.obstacle_x, self.obstacle_y, self.obstacle_taille, self.obstacle_taille, 8)

        # Display le score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Affiche le message de GO
        if self.game_over:
            pyxel.text(LARGEUR_ECRAN // 2 - 20, HAUTEUR_ECRAN // 2, "GAME OVER", 8)
            pyxel.text(LARGEUR_ECRAN // 2 - 35, HAUTEUR_ECRAN // 2 + 10, "Appuyez sur Q pour Quitter", 7)

        # Quit quand on click sur Q
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

# Lancement du jeu
Jeu()

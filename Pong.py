import pyxel
import game_pong  # Remplacez `fichier_du_jeu` par le nom de votre fichier de jeu

# Dimensions du menu
LARGEUR_MENU = 160
HAUTEUR_MENU = 120

class Menu:
    def __init__(self):
        # Initialisation de la fenêtre pour le menu
        pyxel.init(LARGEUR_MENU, HAUTEUR_MENU, title="Menu Pong")

        # Lancement du menu principal
        self.option_selectionnee = 0  # Option par défaut sélectionnée : "1 Joueur"
        pyxel.run(self.update, self.draw)

    def update(self):
        """Met à jour les éléments du menu pour chaque image"""

        # Détection des touches fléchées pour naviguer dans les options
        if pyxel.btnp(pyxel.KEY_UP):
            self.option_selectionnee = (self.option_selectionnee - 1) % 3
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.option_selectionnee = (self.option_selectionnee + 1) % 3

        # Exécute l'action de l'option sélectionnée lorsque "Entrée" est pressé
        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.option_selectionnee == 0:
                Jeu(mode=1)  # Lancer le jeu en mode 1 joueur
            elif self.option_selectionnee == 1:
                Jeu(mode=2)  # Lancer le jeu en mode 2 joueurs
            elif self.option_selectionnee == 2:
                pyxel.quit()  # Quitter le jeu

        # Affiche les informations lorsque "?" est sélectionné
        if pyxel.btnp(pyxel.KEY_QUESTION):
            self.afficher_informations()

    def afficher_informations(self):
        """Affiche une boîte de dialogue avec les instructions du jeu"""
        pyxel.cls(0)
        pyxel.text(10, 10, "Instructions:", pyxel.COLOR_YELLOW)
        pyxel.text(10, 20, "1 Joueur : Vous contre l'ordinateur", pyxel.COLOR_WHITE)
        pyxel.text(10, 30, "2 Joueurs : Duel entre deux joueurs", pyxel.COLOR_WHITE)
        pyxel.text(10, 40, "Controle : Fleches, Z/S, etc.", pyxel.COLOR_WHITE)
        pyxel.text(10, 50, "Appuyez sur Q pour revenir", pyxel.COLOR_WHITE)

        # Retour au menu si Q est pressé
        while not pyxel.btn(pyxel.KEY_Q):
            pass

    def draw(self):
        """Affiche les éléments du menu à l'écran"""

        # Effacer l'écran
        pyxel.cls(0)

        # Afficher les options
        pyxel.text(10, 30, "1 Joueur", pyxel.COLOR_WHITE if self.option_selectionnee == 0 else pyxel.COLOR_GRAY)
        pyxel.text(10, 40, "2 Joueurs", pyxel.COLOR_WHITE if self.option_selectionnee == 1 else pyxel.COLOR_GRAY)
        pyxel.text(10, 50, "Quitter", pyxel.COLOR_WHITE if self.option_selectionnee == 2 else pyxel.COLOR_GRAY)

        # Afficher le bouton "?"
        pyxel.text(10, 70, "?", pyxel.COLOR_YELLOW)

# Lancer le menu
Menu()

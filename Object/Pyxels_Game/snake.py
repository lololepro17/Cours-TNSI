import pyxel
import random

class SnakeGame:
    def __init__(self):
        pyxel.init(128, 128)  # Initialisation de la fenêtre
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.snake = [(64, 64)]  # Position initiale du serpent au centre
        self.direction = (8, 0)  # Direction initiale : vers la droite
        self.food = self.place_food()
        self.score = 0
        self.game_over = False
        self.speed = 10  # Contrôle de la vitesse du serpent (plus élevé = plus lent)
        self.timer = 0  # Compteur de frames pour contrôler la vitesse du serpent

    def place_food(self):
        # Position aléatoire pour la nourriture (sur une grille de 8x8)
        while True:
            food_position = (random.randint(0, 15) * 8, random.randint(0, 15) * 8)
            if food_position not in self.snake:  # Évite de placer la nourriture sur le serpent
                return food_position

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R):
                self.reset_game()
            return

        # Contrôles du serpent (changement de direction)
        if pyxel.btn(pyxel.KEY_UP) and self.direction != (0, 8):
            self.direction = (0, -8)
        elif pyxel.btn(pyxel.KEY_DOWN) and self.direction != (0, -8):
            self.direction = (0, 8)
        elif pyxel.btn(pyxel.KEY_LEFT) and self.direction != (8, 0):
            self.direction = (-8, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.direction != (-8, 0):
            self.direction = (8, 0)

        # Mise à jour du timer
        self.timer += 1
        if self.timer < self.speed:
            return  # Attend que le timer atteigne la vitesse définie avant de bouger
        self.timer = 0  # Réinitialise le timer pour le prochain déplacement

        # Déplacement du serpent
        new_head = (self.snake[0][0] + self.direction[0],
                    self.snake[0][1] + self.direction[1])

        # Vérifie les collisions avec les murs
        if not (0 <= new_head[0] < 128 and 0 <= new_head[1] < 128):
            self.game_over = True
            return

        # Vérifie les collisions avec le corps du serpent
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake = [new_head] + self.snake  # Ajoute la nouvelle tête au serpent

        # Vérifie si le serpent mange la nourriture
        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()  # Place une nouvelle nourriture
        else:
            self.snake.pop()  # Supprime la queue si pas de nourriture mangée

    def draw(self):
        pyxel.cls(0)  # Efface l'écran

        # Dessine le serpent
        for (x, y) in self.snake:
            pyxel.rect(x, y, 8, 8, 11)

        # Dessine la nourriture
        pyxel.rect(self.food[0], self.food[1], 8, 8, 8)

        # Affiche le score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        if self.game_over:
            pyxel.text(40, 60, "GAME OVER", pyxel.frame_count % 16)
            pyxel.text(30, 70, "Press 'R' to restart", 7)

# Lance le jeu
SnakeGame()

import pyxel
from pong_ai import PongAI
import numpy as np
from ball import*

class Game:
    def __init__(self):
        pyxel.init(180, 120, title="Pong avec IA")
        self.dimensions = (160, 120)
        self.ball = Ball(80, 60, 7, 2, self.dimensions)
        self.player1 = Paddle((10, 60), 9, 5, 20, pyxel.KEY_Z, pyxel.KEY_S, 4, self.dimensions)
        self.ai_player = PongAI()
        self.score_left = 0
        self.score_right = 0
        self.game_started = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.game_started:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.game_started = True
            return

        self.player1.update()
        self.update_ai_player()

        result = self.ball.move()
        if result == "left":
            self.score_right += 1
            self.ball.reset()
        elif result == "right":
            self.score_left += 1
            self.ball.reset()

        self.ball.handle_collision([self.player1, self.ai_player])

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

    def update_ai_player(self):
        # État pour le modèle : positions de la balle et de l'IA, vitesse de la balle
        state = np.array([self.ball.x, self.ball.y, self.ai_player.y, self.ball.y_velocity]).reshape(1, -1)
        
        # Décision du modèle pour le mouvement de l'IA
        action = self.ai_player.choose_action(state)
        
        # Mettre à jour la position de la raquette en fonction de l'action
        if action == 0 and self.ai_player.y > 0:
            self.ai_player.y -= 3
        elif action == 1 and self.ai_player.y < self.dimensions[1] - self.ai_player.height:
            self.ai_player.y += 3
        
        # Déterminer la récompense
        reward = 1 if self.ball.x < self.ai_player.x else -1
        done = result == "left" or result == "right"
        
        # Enregistrer l'expérience dans la mémoire
        next_state = np.array([self.ball.x, self.ball.y, self.ai_player.y, self.ball.y_velocity]).reshape(1, -1)
        self.ai_player.store_experience(state, action, reward, next_state, done)
        
        # Entraînement de l'IA
        self.ai_player.train()

Game()
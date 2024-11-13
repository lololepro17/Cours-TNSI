import pyxel
import random

SPIN = 0.6
BOUNCE = 0.03
BOUNCE_FRICTION = 0.2
MAX_SPEED = 5
PADDLE_SPEED = 4
BOT_SPEED = 1.5
WINNING_SCORE = 5

class Paddle:
    def __init__(self, x, y, colour, control_up, control_down, dimensions, is_bot=False, bot_speed=BOT_SPEED):
        self.x, self.y = x, y
        self.width, self.height = 5, 20
        self.control_up = control_up
        self.control_down = control_down
        self.colour = colour
        self.is_bot = is_bot
        self.bot_speed = bot_speed
        self.dimensions = dimensions

    def move(self, ball_y=None):
        if self.is_bot and ball_y is not None:
            self._bot_move(ball_y)
        else:
            self._player_move()

    def _bot_move(self, ball_y):
        target_y = ball_y - self.height / 2
        distance = target_y - self.y
        if abs(distance) > self.bot_speed:
            self.y += self.bot_speed if distance > 0 else -self.bot_speed
        else:
            self.y = target_y
        self._keep_in_bounds()

    def _player_move(self):
        if pyxel.btn(self.control_up):
            self.y -= PADDLE_SPEED
        elif pyxel.btn(self.control_down):
            self.y += PADDLE_SPEED
        self._keep_in_bounds()

    def _keep_in_bounds(self):
        self.y = max(0, min(self.y, self.dimensions[1] - self.height))

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.colour)


class Ball:
    def __init__(self, x, y, colour, initial_velocity, dimensions):
        self.x, self.y = x, y
        self.width, self.height = 2, 2
        self.colour = colour
        self.initial_velocity = initial_velocity
        self.dimensions = dimensions
        self.reset()

    def move(self):
        # Déplacement de la balle
        self.x += self.x_velocity
        self.y += self.y_velocity
        
        # Gestion du rebond en haut et en bas
        if self.y < 0:
            self.y = 0
            self.y_velocity = -self.y_velocity
        elif self.y + self.height > self.dimensions[1]:
            self.y = self.dimensions[1] - self.height
            self.y_velocity = -self.y_velocity

        # Vérification des sorties de l'écran
        if self.x < 0:
            return "right"
        elif self.x + self.width > self.dimensions[0]:
            return "left"
        return None

    def reset(self):
        # Réinitialise la position et la vitesse de la balle
        self.x, self.y = 80, 60
        self.x_velocity = self.initial_velocity * random.choice([-1, 1])
        self.y_velocity = self.initial_velocity * random.choice([-1, 1])

    def handle_collision(self, paddles):
        # Gère la collision avec les raquettes
        for paddle in paddles:
            if self._is_colliding(paddle):
                self._apply_spin(paddle)
                self.x_velocity = -self.x_velocity
                return True
        return False

    def _apply_spin(self, paddle):
        # Calcule et applique le spin selon la position d'impact sur la raquette
        paddle_centre = paddle.y + paddle.height / 2
        ball_centre = self.y + self.height / 2
        impact_position = (ball_centre - paddle.y) / paddle.height

        # Ajuste la vitesse verticale en fonction de la position d'impact
        if impact_position < 0.33:  # Impact dans la partie supérieure de la raquette
            self.y_velocity -= SPIN
        elif impact_position > 0.66:  # Impact dans la partie inférieure
            self.y_velocity += SPIN
        else:  # Impact au centre de la raquette
            self.y_velocity *= 0.9  # Réduit la vitesse verticale pour une trajectoire plus horizontale

        # Limite la vitesse verticale pour qu'elle ne dépasse pas MAX_SPEED
        self.y_velocity = max(-MAX_SPEED, min(self.y_velocity, MAX_SPEED))

    def _is_colliding(self, paddle):
        # Vérifie la collision entre la balle et la raquette
        return (
            self.x < paddle.x + paddle.width and
            self.x + self.width > paddle.x and
            self.y < paddle.y + paddle.height and
            self.y + self.height > paddle.y
        )

    def draw(self):
        # Affiche la balle à l'écran
        pyxel.circ(self.x, self.y, self.width, self.colour)

class PongGame:
    def __init__(self):
        pyxel.init(180, 120, title="Pong")
        self.dimensions = (160, 120)
        self.paddle_left = Paddle(10, 60, 8, pyxel.KEY_Z, pyxel.KEY_S, self.dimensions)
        self.paddle_right = Paddle(145, 60, 11, pyxel.KEY_UP, pyxel.KEY_DOWN, self.dimensions, is_bot=True)
        self.ball = Ball(80, 60, 7, initial_velocity=2, dimensions=self.dimensions)
        self.score_left, self.score_right = 0, 0
        self.game_started = False
        self.single_player_mode = True
        self.winner = None
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.game_started:
            self._select_mode()
            return
        if self.winner:
            self._check_restart()
            return
        self._update_game_state()

    def _select_mode(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.single_player_mode = True
            self.paddle_right.is_bot = True
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.single_player_mode = False
            self.paddle_right.is_bot = False
        elif pyxel.btnp(pyxel.KEY_RETURN):
            self.game_started = True

    def _check_restart(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self._reset_game()
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def _update_game_state(self):
        self.paddle_left.move()
        self.paddle_right.move(ball_y=self.ball.y if self.paddle_right.is_bot else None)
        self._check_score()
        self.ball.handle_collision([self.paddle_left, self.paddle_right])

    def _check_score(self):
        result = self.ball.move()
        if result == "left":
            self.score_right += 1
            self._check_winner("Droite")
        elif result == "right":
            self.score_left += 1
            self._check_winner("Gauche")

    def _check_winner(self, side):
        if self.score_left >= WINNING_SCORE or self.score_right >= WINNING_SCORE:
            self.winner = side
        else:
            self.ball.reset()

    def _reset_game(self):
        self.score_left, self.score_right = 0, 0
        self.winner = None
        self.ball.reset()
        self.paddle_left.y, self.paddle_right.y = 60, 60

    def draw(self):
        pyxel.cls(0)
        if not self.game_started:
            self._draw_intro()
        elif self.winner:
            self._draw_winner()
        else:
            self._draw_game()

    def _draw_intro(self):
        pyxel.text(30, 40, "Selectionnez le mode:", 7)
        pyxel.text(30, 50, "Mode 1 joueur", 7 if self.single_player_mode else 6)
        pyxel.text(30, 60, "Mode 2 joueurs", 7 if not self.single_player_mode else 6)
        pyxel.text(20, 90, "Appuyez sur ENTREE pour commencer", 8)

    def _draw_winner(self):
        pyxel.text(40, 50, f"Le joueur {self.winner} gagne!", 7)
        pyxel.text(30, 60, "Appuyez sur ENTREE pour rejouer", 7)
        pyxel.text(35, 70, "Appuyez sur Q pour quitter", 8)

    def _draw_game(self):
        self.paddle_left.draw()
        self.paddle_right.draw()
        self.ball.draw()
        pyxel.text(10, 5, f"Score Gauche: {self.score_left}", 7)
        pyxel.text(110, 5, f"Score Droite: {self.score_right}", 7)



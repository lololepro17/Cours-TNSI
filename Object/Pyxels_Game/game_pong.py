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
    def __init__(self, x, y, colour, control_left, control_right, dimensions, is_bot=False, bot_speed=BOT_SPEED):
        self.x, self.y = x, y
        self.width, self.height = 20, 5  # Inverser la largeur et la hauteur pour une raquette horizontale
        self.control_left = control_left
        self.control_right = control_right
        self.colour = colour
        self.is_bot = is_bot
        self.bot_speed = bot_speed
        self.dimensions = dimensions

    def move(self, ball_x=None):
        if self.is_bot and ball_x is not None:
            self._bot_move(ball_x)
        else:
            self._player_move()

    def _bot_move(self, ball_x):
        target_x = ball_x - self.width / 2
        distance = target_x - self.x
        if abs(distance) > self.bot_speed:
            self.x += self.bot_speed if distance > 0 else -self.bot_speed
        else:
            self.x = target_x
        self._keep_in_bounds()

    def _player_move(self):
        if pyxel.btn(self.control_left):
            self.x -= PADDLE_SPEED
        elif pyxel.btn(self.control_right):
            self.x += PADDLE_SPEED
        self._keep_in_bounds()

    def _keep_in_bounds(self):
        self.x = max(0, min(self.x, self.dimensions[0] - self.width))

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
        
        # Gestion du rebond à gauche et à droite
        if self.x < 0:
            self.x = 0
            self.x_velocity = -self.x_velocity
        elif self.x + self.width > self.dimensions[0]:
            self.x = self.dimensions[0] - self.width
            self.x_velocity = -self.x_velocity

        # Vérification des sorties de l'écran
        if self.y < 0:
            return "bottom"
        elif self.y + self.height > self.dimensions[1]:
            return "top"
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
                self.y_velocity = -self.y_velocity  # Inversion de la vitesse verticale
                return True
        return False

    def _apply_spin(self, paddle):
        paddle_centre = paddle.x + paddle.width / 2
        ball_centre = self.x + self.width / 2
        impact_position = (ball_centre - paddle.x) / paddle.width

        if impact_position < 0.33:  # Impact dans la partie gauche de la raquette
            self.x_velocity -= SPIN
        elif impact_position > 0.66:  # Impact dans la partie droite
            self.x_velocity += SPIN
        else:  # Impact au centre de la raquette
            self.x_velocity *= 0.9

        self.x_velocity = max(-MAX_SPEED, min(self.x_velocity, MAX_SPEED))

    def _is_colliding(self, paddle):
        return (
            self.x < paddle.x + paddle.width and
            self.x + self.width > paddle.x and
            self.y < paddle.y + paddle.height and
            self.y + self.height > paddle.y
        )

    def draw(self):
        pyxel.circ(self.x, self.y, self.width, self.colour)


class PongGame:
    def __init__(self):
        pyxel.init(180, 120, title="Pong")
        self.dimensions = (160, 120)
        self.paddle_top = Paddle(80, 10, 8, pyxel.KEY_LEFT, pyxel.KEY_RIGHT, self.dimensions)
        self.paddle_bottom = Paddle(80, 105, 11, pyxel.KEY_A, pyxel.KEY_D, self.dimensions, is_bot=True)
        self.ball = Ball(80, 60, 7, initial_velocity=2, dimensions=self.dimensions)
        self.score_top, self.score_bottom = 0, 0
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
            self.paddle_bottom.is_bot = True
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.single_player_mode = False
            self.paddle_bottom.is_bot = False
        elif pyxel.btnp(pyxel.KEY_RETURN):
            self.game_started = True

    def _check_restart(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self._reset_game()
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def _update_game_state(self):
        self.paddle_top.move()
        self.paddle_bottom.move(ball_x=self.ball.x if self.paddle_bottom.is_bot else None)
        self._check_score()
        self.ball.handle_collision([self.paddle_top, self.paddle_bottom])

    def _check_score(self):
        result = self.ball.move()
        if result == "top":
            self.score_bottom += 1
            self._check_winner("Bas")
        elif result == "bottom":
            self.score_top += 1
            self._check_winner("Haut")

    def _check_winner(self, side):
        if self.score_top >= WINNING_SCORE or self.score_bottom >= WINNING_SCORE:
            self.winner = side
        else:
            self.ball.reset()

    def _reset_game(self):
        self.score_top, self.score_bottom = 0, 0
        self.winner = None
        self.ball.reset()
        self.paddle_top.x, self.paddle_bottom.x = 80, 80

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
        self.paddle_top.draw()
        self.paddle_bottom.draw()
        self.ball.draw()
        pyxel.text(10, 5, f"Score Haut: {self.score_top}", 7)
        pyxel.text(110, 5, f"Score Bas: {self.score_bottom}", 7)


# Lancement du jeu
PongGame()

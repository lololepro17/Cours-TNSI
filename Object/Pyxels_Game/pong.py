import pyxel
import random

SPIN = 0.6
PADDLE_SPEED = 4
BOT_SPEED = 1.5
WINNING_SCORE = 5
MAX_SPEED = 5

# Fonctions de dessin et d'affichage
def title():
    pyxel.text(55, 50, "Pong Game", pyxel.frame_count % 16)

def button(x, y, text, color):
    pyxel.rectb(x, y, 50, 10, color)
    pyxel.text(x + 5, y + 2, text, color)

def display_score(score_left, score_right):
    pyxel.text(10, 5, f"Score Gauche: {score_left}", 7)
    pyxel.text(110, 5, f"Score Droite: {score_right}", 7)

def display_winner(winner):
    pyxel.text(40, 50, f"Le joueur {winner} gagne!", 7)
    pyxel.text(30, 60, "Appuyez sur ENTREE pour rejouer", 7)
    pyxel.text(35, 70, "Appuyez sur Q pour quitter", 8)

class Paddle:
    def __init__(self, x, y, colour, control_up, control_down, is_bot=False, bot_speed=BOT_SPEED):
        self.x, self.y = x, y
        self.width, self.height = 5, 20
        self.control_up = control_up
        self.control_down = control_down
        self.colour = colour
        self.is_bot = is_bot
        self.bot_speed = bot_speed

    def move(self, ball_y=None):
        if self.is_bot and ball_y is not None:
            self._bot_move(ball_y)
        else:
            self._player_move()

    def _bot_move(self, ball_y):
        if ball_y < self.y:
            self.y -= self.bot_speed
        elif ball_y > self.y + self.height:
            self.y += self.bot_speed
        self._keep_in_bounds()

    def _player_move(self):
        if pyxel.btn(self.control_up):
            self.y -= PADDLE_SPEED
        elif pyxel.btn(self.control_down):
            self.y += PADDLE_SPEED
        self._keep_in_bounds()

    def _keep_in_bounds(self):
        self.y = max(0, min(self.y, 120 - self.height))

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.colour)

class Ball:
    def __init__(self, x, y, colour):
        self.x, self.y = x, y
        self.width, self.height = 2, 2
        self.colour = colour
        self.reset()

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.y < 0 or self.y + self.height > 120:
            self.y_velocity = -self.y_velocity

        if self.x < 0:
            return "right"
        elif self.x + self.width > 160:
            return "left"
        return None

    def reset(self):
        self.x, self.y = 80, 60
        self.x_velocity = random.choice([-2, 2])
        self.y_velocity = random.choice([-2, 2])

    def handle_collision(self, paddles):
        for paddle in paddles:
            if self.x < paddle.x + paddle.width and self.x + self.width > paddle.x and self.y < paddle.y + paddle.height and self.y + self.height > paddle.y:
                self.x_velocity = -self.x_velocity
                return True
        return False

    def draw(self):
        pyxel.circ(self.x, self.y, self.width, self.colour)

class PongApp:
    def __init__(self):
        pyxel.init(160, 120, "Pong Game")
        self.paddle_left = Paddle(10, 60, 8, pyxel.KEY_Z, pyxel.KEY_S)
        self.paddle_right = Paddle(145, 60, 11, pyxel.KEY_UP, pyxel.KEY_DOWN, is_bot=True)
        self.ball = Ball(80, 60, 7)
        self.score_left, self.score_right = 0, 0
        self.game_started = False
        self.winner = None
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.game_started:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.game_started = True
        elif self.winner:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self._reset_game()
            elif pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
        else:
            self.paddle_left.move()
            self.paddle_right.move(self.ball.y if self.paddle_right.is_bot else None)
            if self.ball.handle_collision([self.paddle_left, self.paddle_right]):
                pass
            result = self.ball.move()
            if result == "left":
                self.score_right += 1
                self._check_winner("Droite")
            elif result == "right":
                self.score_left += 1
                self._check_winner("Gauche")

    def draw(self):
        pyxel.cls(0)
        if not self.game_started:
            title()
            button(55, 60, "Start Game", 7)
        elif self.winner:
            display_winner(self.winner)
        else:
            self.paddle_left.draw()
            self.paddle_right.draw()
            self.ball.draw()
            display_score(self.score_left, self.score_right)

    def _check_winner(self, side):
        if self.score_left >= WINNING_SCORE or self.score_right >= WINNING_SCORE:
            self.winner = side
        else:
            self.ball.reset()

    def _reset_game(self):
        self.score_left, self.score_right = 0, 0
        self.winner = None
        self.ball.reset()

# Lancement de l'application
PongApp()

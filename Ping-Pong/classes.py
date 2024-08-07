import arcade
from constants import *
import random


class Field(arcade.Window):
    def __init__(self):
        super().__init__(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title=TITLE)
        self.upper_bar = Bar()
        self.down_bar = Bar()
        self.ball = Ball()
        self.setup()
        self.last_key = 0


    def on_draw(self):
        self.clear(WHITE)
        # self.upper_bar.draw()
        self.down_bar.draw()
        self.ball.draw()

    def setup(self):
        # self.upper_bar.center_x = WINDOW_WIDTH / 2
        # self.upper_bar.center_y = WINDOW_HEIGHT / 16 * 15
        # self.upper_bar.scale = 0.4

        self.down_bar.center_x = WINDOW_WIDTH / 2
        self.down_bar.center_y = WINDOW_HEIGHT / 16
        self.down_bar.scale = 0.4

        self.ball.center_x = WINDOW_WIDTH / 2
        self.ball.center_y = WINDOW_HEIGHT / 2
        self.ball.scale = 0.05
        self.ball.change_y = random.randint(-10, 10)
        self.ball.change_x = random.randint(-10, 10)

    def update(self, delta):
        self.down_bar.update()
        # self.upper_bar.update()
        self.ball.update()
        if arcade.check_for_collision(self.upper_bar, self.ball) or arcade.check_for_collision(self.down_bar, self.ball):
            self.ball.change_y = -self.ball.change_y


    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.down_bar.change_x = 5
            self.last_key = arcade.key.RIGHT

        if key == arcade.key.LEFT:
            self.down_bar.change_x = -5
            self.last_key = arcade.key.LEFT

        # if key == arcade.key.A:
        #     self.upper_bar.change_x = 5
        #     self.last_key = arcade.key.A
        #
        # if key == arcade.key.D:
        #     self.upper_bar.change_x = -5
        #     self.last_key = arcade.key.D

    def on_key_release(self, key: int, modifiers: int):
        if self.last_key == key:
            self.down_bar.change_x = 0


class Bar(arcade.Sprite):

    def __init__(self):
        super().__init__(filename='bar.png')

    def update(self):
        self.center_x += self.change_x
        if self.right >= WINDOW_WIDTH:
            self.change_x = 0
        if self.left <= 0:
            self.change_x = 0



class Ball(arcade.Sprite):

    def __init__(self):
        super().__init__(filename='ball.png')
        # self.change_x = 0
        # self.change_y = 0

    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x

        if self.right >= WINDOW_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= WINDOW_HEIGHT:
            self.change_y = -self.change_y
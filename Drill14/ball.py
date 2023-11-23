from pico2d import *
import game_world
import game_framework
import random


class Ball:
    image = None

    def __init__(self, bg, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1780)
        self.y = y if y else random.randint(100, 924)
        self.bg = bg

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        left = self.x - self.bg.window_left - 10
        bottom = self.y - self.bg.window_bottom - 10
        right = self.x - self.bg.window_left + 10
        top = self.y - self.bg.window_bottom + 10
        return left, bottom, right, top

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)
                pass

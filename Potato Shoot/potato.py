from pico2d import load_image, get_time
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_a
import math


class Idle:
    @staticmethod
    def do(potato):
        pass

    @staticmethod
    def enter(potato, e):
        pass

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        potato.image.clip_composite_draw(0, 0, 150, 150, 0, 'r', potato.x, potato.y + 20, 100, 100)


class StateMachine:
    def __init__(self, potato):
        self.potato = potato
        self.cur_state = Idle

    def start(self):
        pass

    def hendle_event(self, e):
        pass

    def update(self):
        self.cur_state.do(self.potato)

    def draw(self):
        self.cur_state.draw(self.potato)

class Potato:
    def __init__(self, x = 300, y = 90):
        self.x, self.y = x, y
        self.action = 3
        self.image = load_image('Resource\\Potato\\potato_1_2.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.hendle_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()

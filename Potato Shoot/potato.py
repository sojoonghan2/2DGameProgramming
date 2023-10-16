from pico2d import load_image, get_time
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_a
import math


def space_down(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e): return e[0] == 'TIME_OUT'


def right_down(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def a_down(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


class Idle:
    @staticmethod
    def do(potato):
        potato.frame = (potato.frame + 1) % 8
        if get_time() - potato.statr_time > 5:
            potato.state_machine.hendle_event(('TIME_OUT', 0))

    @staticmethod
    def enter(potato, e):
        if potato.action == 0:
            potato.action = 2
        elif potato.action == 1:
            potato.action = 3
        potato.frame = 0
        potato.statr_time = get_time()

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        potato.image.clip_draw(potato.frame * 100, potato.action * 100, 100, 100, potato.x, potato.y)


class Sleep:
    @staticmethod
    def do(potato):
        potato.frame = (potato.frame + 1) % 8

    @staticmethod
    def enter(potato, e):
        potato.frame = 0

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        if potato.action == 2:
            potato.image.clip_composite_draw(potato.frame * 100, 200, 100, 100, -math.pi / 2, '', potato.x + 25,
                                          potato.y - 25, 100, 100)
        else:
            potato.image.clip_composite_draw(potato.frame * 100, 300, 100, 100, math.pi / 2, '', potato.x - 25,
                                          potato.y - 25, 100, 100)


class Run:
    @staticmethod
    def do(potato):
        potato.frame = (potato.frame + 1) % 8
        potato.x += potato.dir * 5

    @staticmethod
    def enter(potato, e):
        if right_down(e) or left_up(e):
            potato.dir, potato.action = 1, 1
        elif left_down(e) or right_up(e):
            potato.dir, potato.action = -1, 0

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        potato.image.clip_draw(potato.frame * 100, potato.action * 100, 100, 100, potato.x, potato.y)


class AutoRun():
    @staticmethod
    def do(potato):
        potato.frame = (potato.frame + 1) % 8
        potato.x += potato.dir * 10
        if potato.dir == 1 and potato.x > 800:
            potato.dir, potato.action = -1, 0
        elif potato.dir == -1 and potato.x < 0:
            potato.dir, potato.action = 1, 1
        if get_time() - potato.statr_time > 5:
            potato.state_machine.hendle_event(('TIME_OUT', 0))

    @staticmethod
    def enter(potato, e):
        potato.statr_time = get_time()
        if potato.dir == 1:
            potato.action = 1
        else:
            potato.action = 0
        pass

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        potato.image.clip_draw(potato.frame * 100, potato.action * 100, 100, 100, potato.x, potato.y + 25, 150, 150)


class StateMachine:
    def __init__(self, potato):
        self.potato = potato
        self.cur_state = Idle
        self.table = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, a_down: AutoRun},
            Run: {right_down: Idle, left_down: Idle, left_up: Idle, right_up: Idle, a_down: AutoRun},
            Sleep: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle, a_down: AutoRun},
            AutoRun: {right_down: Run, left_down: Run, time_out: Idle}

        }

    def start(self):
        self.cur_state.enter(self.potato, ('START', 0))

    def hendle_event(self, e):
        for cheak_event, next_state in self.table[self.cur_state].items():
            if cheak_event(e):
                self.cur_state.exit(self.potato, e)
                self.cur_state = next_state
                self.cur_state.enter(self.potato, e)
                return True
        return False

    def update(self):
        self.cur_state.do(self.potato)

    def draw(self):
        self.cur_state.draw(self.potato)
        pass


class Potato:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 1
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.hendle_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()

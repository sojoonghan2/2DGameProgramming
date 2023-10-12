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
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        if get_time() - boy.statr_time > 5:
            boy.state_machine.hendle_event(('TIME_OUT', 0))

    @staticmethod
    def enter(boy, e):
        if boy.action == 0:
            boy.action = 2
        elif boy.action == 1:
            boy.action = 3
        boy.frame = 0
        boy.statr_time = get_time()

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class Sleep:
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def enter(boy, e):
        boy.frame = 0

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def draw(boy):
        if boy.action == 2:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100, -math.pi / 2, '', boy.x + 25,
                                          boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, math.pi / 2, '', boy.x - 25,
                                          boy.y - 25, 100, 100)


class Run:
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.dir * 5

    @staticmethod
    def enter(boy, e):
        if right_down(e) or left_up(e):
            boy.dir, boy.action = 1, 1
        elif left_down(e) or right_up(e):
            boy.dir, boy.action = -1, 0

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class AutoRun():
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.dir * 10
        if boy.dir == 1 and boy.x > 800:
            boy.dir, boy.action = -1, 0
        elif boy.dir == -1 and boy.x < 0:
            boy.dir, boy.action = 1, 1
        if get_time() - boy.statr_time > 5:
            boy.state_machine.hendle_event(('TIME_OUT', 0))

    @staticmethod
    def enter(boy, e):
        boy.statr_time = get_time()
        if boy.dir == 1:
            boy.action = 1
        else:
            boy.action = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y + 25, 150, 150)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.table = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, a_down: AutoRun},
            Run: {right_down: Idle, left_down: Idle, left_up: Idle, right_up: Idle, a_down: AutoRun},
            Sleep: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle, a_down: AutoRun},
            AutoRun: {right_down: Run, left_down: Run, time_out: Idle}

        }

    def start(self):
        self.cur_state.enter(self.boy, ('START', 0))

    def hendle_event(self, e):
        for cheak_event, next_state in self.table[self.cur_state].items():
            if cheak_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True
        return False

    def update(self):
        self.cur_state.do(self.boy)

    def draw(self):
        self.cur_state.draw(self.boy)
        pass


class Boy:
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

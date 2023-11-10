from pico2d import load_image

import potato


class Idle:
    @staticmethod
    def do(bottle):
        pass

    @staticmethod
    def enter(bottle, e):
        pass

    @staticmethod
    def exit(bottle, e):
        pass

    @staticmethod
    def draw(bottle):
        bottle.image.clip_composite_draw(0, 0, 500, 654, 0, 'r', bottle.x + 50, bottle.y + 100, 130, 180)


class Fly:
    @staticmethod
    def do(bottle):
        pass

    @staticmethod
    def enter(bottle, e):
        pass

    @staticmethod
    def exit(bottle, e):
        pass

    @staticmethod
    def draw(bottle):
        bottle.image.clip_composite_draw(0, 0, 500, 654, 4, 'r', bottle.x + 50, bottle.y + 100, 130, 180)


class StateMachine:
    def __init__(self, bottle):
        self.bottle = bottle
        self.cur_state = Idle

    def start(self):
        self.cur_state.enter(self.bottle, ('START', 0))

    def handle_event(self):
        pass

    def update(self):
        self.cur_state.do(self.bottle)

    def draw(self):
        self.cur_state.draw(self.bottle)


class Bottle:
    image = None

    def __init__(self, x=140, y=500):
        if Bottle.image == None:
            Bottle.image = load_image('Resource\\Bottle\\Bottle.png')
        self.x, self.y = x, y
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()

    def handle_event(self, event):
        pass

    def update(self):
        pass

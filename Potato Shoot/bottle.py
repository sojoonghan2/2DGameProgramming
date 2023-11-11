import random

from pico2d import load_image, draw_rectangle, get_time
import play_mode


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
        bottle.image.clip_composite_draw(0, 0, 500, 654, 0, 'r', bottle.x, bottle.y, 130, 180)


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
        bottle.image.clip_composite_draw(0, 0, 500, 654, bottle.angle, 'r', bottle.x, bottle.y, 130, 180)


class Die:
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
        pass


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
        self.die_time = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.angle = random.randint(1, 6)

    def draw(self):
        self.state_machine.draw()

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 220, self.y - 50, self.x + 220, self.y + 50

    def handle_collision(self, group, other):
        if group == 'potato:bottle':
            # 경우의 수에 따라서 bottle[n]의 cur_state를 Fly로 설정
            print(play_mode.potato.case_num)
            if play_mode.potato.case_num > 0 and play_mode.potato.case_num <= 1:
                play_mode.bottle[0].state_machine.cur_state = Fly
            elif play_mode.potato.case_num > 1 and play_mode.potato.case_num <= 2:
                play_mode.bottle[0].state_machine.cur_state = Fly
                play_mode.bottle[4].state_machine.cur_state = Fly
            elif play_mode.potato.case_num > 2 and play_mode.potato.case_num <= 3:
                play_mode.bottle[0].state_machine.cur_state = Fly
                play_mode.bottle[1].state_machine.cur_state = Fly
                play_mode.bottle[4].state_machine.cur_state = Fly
                play_mode.bottle[5].state_machine.cur_state = Fly
                play_mode.bottle[7].state_machine.cur_state = Fly
            elif play_mode.potato.case_num > 3 and play_mode.potato.case_num <= 4:
                play_mode.bottle[1].state_machine.cur_state = Fly
                play_mode.bottle[2].state_machine.cur_state = Fly
                play_mode.bottle[4].state_machine.cur_state = Fly
                play_mode.bottle[5].state_machine.cur_state = Fly
                play_mode.bottle[7].state_machine.cur_state = Fly
                play_mode.bottle[8].state_machine.cur_state = Fly
                play_mode.bottle[9].state_machine.cur_state = Fly
            elif play_mode.potato.case_num > 4 and play_mode.potato.case_num <= 5:
                if play_mode.potato.power > 80:
                    for i in range(10):
                        play_mode.bottle[i].state_machine.cur_state = Fly
                        play_mode.potato.turn = 1
                else:
                    play_mode.bottle[1].state_machine.cur_state = Fly
                    play_mode.bottle[2].state_machine.cur_state = Fly
                    play_mode.bottle[3].state_machine.cur_state = Fly
                    play_mode.bottle[4].state_machine.cur_state = Fly
                    play_mode.bottle[5].state_machine.cur_state = Fly
                    play_mode.bottle[6].state_machine.cur_state = Fly
                    play_mode.bottle[7].state_machine.cur_state = Fly
                    play_mode.bottle[8].state_machine.cur_state = Fly
            elif play_mode.potato.case_num > 5 and play_mode.potato.case_num <= 6:
                play_mode.bottle[1].state_machine.cur_state = Fly
                play_mode.bottle[2].state_machine.cur_state = Fly
                play_mode.bottle[3].state_machine.cur_state = Fly
                play_mode.bottle[5].state_machine.cur_state = Fly
                play_mode.bottle[6].state_machine.cur_state = Fly
                play_mode.bottle[7].state_machine.cur_state = Fly
                play_mode.bottle[8].state_machine.cur_state = Fly
                play_mode.bottle[9].state_machine.cur_state = Fly
            elif play_mode.potato.case_num > 6 and play_mode.potato.case_num <= 7:
                play_mode.bottle[2].state_machine.cur_state = Fly
                play_mode.bottle[3].state_machine.cur_state = Fly
                play_mode.bottle[5].state_machine.cur_state = Fly
                play_mode.bottle[6].state_machine.cur_state = Fly
                play_mode.bottle[8].state_machine.cur_state = Fly
                play_mode.bottle[9].state_machine.cur_state = Fly
            elif play_mode.potato.case_num > 7 and play_mode.potato.case_num <= 8:
                play_mode.bottle[3].state_machine.cur_state = Fly
                play_mode.bottle[6].state_machine.cur_state = Fly
                play_mode.bottle[8].state_machine.cur_state = Fly
            elif play_mode.potato.case_num > 8 and play_mode.potato.case_num <= 9:
                play_mode.bottle[3].state_machine.cur_state = Fly
                play_mode.bottle[6].state_machine.cur_state = Fly
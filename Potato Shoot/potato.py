from pico2d import load_image, draw_rectangle, SDL_BUTTON_LEFT
from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_SPACE, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP

from point import Point


def right_down(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def space_down(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def space_up(e): return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE


def mouse_down(e): return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].key == SDL_BUTTON_LEFT


def mouse_up(e): return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].key == SDL_BUTTON_LEFT


# 대기
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


# 좌우 이동
class Moving:
    @staticmethod
    def do(potato):
        if potato.x > 400 and potato.dir == 1:
            return
        if potato.x < 140 and potato.dir == -1:
            return
        potato.x += potato.dir * 1

    @staticmethod
    def enter(potato, e):
        if right_down(e) or left_up(e):
            potato.dir = 1
        elif left_down(e) or right_up(e):
            potato.dir = -1

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        potato.image.clip_composite_draw(0, 0, 150, 150, 0, 'r', potato.x, potato.y + 20, 100, 100)


# 굴리기 전 파워 설정
class PowerCharging:
    @staticmethod
    def do(potato):
        potato.power += 1
        if potato.power > 100:
            potato.power = 0

    @staticmethod
    def enter(potato, e):
        # 화살표
        global point
        point = Point(potato.x - 50, potato.y + 30)

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        potato.image.clip_composite_draw(0, 0, 150, 150, 0, 'r', potato.x, potato.y + 20, 100, 100)
        point.image.clip_composite_draw(0, 0, 150, 150, potato.angle, 'r', potato.x, potato.y + 100, 100, 100)
        for i in range(0, potato.power):
            draw_rectangle(100, 300, 100 + i * 3.5, 400)
        draw_rectangle(100, 300, 450, 400)


# 굴리기 전 각도 설정
class AngleAdjustment:
    @staticmethod
    def do(potato):
        potato.power += 1
        if potato.power > 100:
            potato.power = 0
        if potato.angle > 0.5 and point.dir == 1:
            return
        if potato.angle < -0.5 and point.dir == -1:
            return
        potato.angle += point.dir * 0.01

    @staticmethod
    def enter(potato, e):
        if right_down(e) or left_up(e):
            point.dir = -1
        elif left_down(e) or right_up(e):
            point.dir = 1

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        potato.image.clip_composite_draw(0, 0, 150, 150, 0, 'r', potato.x, potato.y + 20, 100, 100)
        point.image.clip_composite_draw(0, 0, 150, 150, potato.angle, 'r', potato.x, potato.y + 100, 100, 100)
        for i in range(0, potato.power):
            draw_rectangle(100, 300, 100 + i * 3.5, 400)
        draw_rectangle(100, 300, 450, 400)


# 굴리기
class Rolling:
    @staticmethod
    def do(potato):
        potato.y += 1
        # 감자의 각도에 따라 굴러가는 각도 변경
        potato.x -= potato.angle / 2
        # 감자의 힘에 따라서 굴러가는 스핀 변경
        potato.spin += potato.power / 500
        # 일정 범위 넘으면 감자 위치 초기화
        if potato.y > 1500:
            potato.x = 250
            potato.y = 100
            potato.spin = 0
            potato.power = 0
            potato.angle = 0
            potato.dir = 1
            potato.state_machine.cur_state = Idle
            return

    @staticmethod
    def enter(potato, e):
        pass

    @staticmethod
    def exit(potato, e):
        pass

    @staticmethod
    def draw(potato):
        potato.image.clip_composite_draw(0, 0, 150, 150, potato.spin, 'r', potato.x, potato.y + 20, 100, 100)


class StateMachine:
    def __init__(self, potato):
        self.potato = potato
        self.cur_state = Idle
        self.table = {
            Idle: {right_down: Moving, left_down: Moving, left_up: Moving, right_up: Moving, space_down: PowerCharging},
            Moving: {right_down: Idle, left_down: Idle, left_up: Idle, right_up: Idle},
            PowerCharging: {space_down: Rolling, right_down: AngleAdjustment, left_down: AngleAdjustment},
            AngleAdjustment: {right_up: PowerCharging, left_up: PowerCharging},
            Rolling: {}
        }

    def start(self):
        self.cur_state.enter(self.potato, ('START', 0))

    def handle_event(self, e):
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.potato, e)
                self.cur_state = next_state
                self.cur_state.enter(self.potato, e)
                return True
        return False

    def update(self):
        self.cur_state.do(self.potato)

    def draw(self):
        self.cur_state.draw(self.potato)


class Potato:
    def __init__(self, x=300, y=90):
        self.x, self.y = x, y
        self.spin = 0
        self.power = 0
        self.angle = 0
        self.dir = 1
        self.image = load_image('Resource\\Potato\\normal1.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())  # 튜플을 풀어 헤쳐서 각각 인자로 전달

    def get_bb(self):
        return self.x - 50, self.y - 20, self.x + 50, self.y + 60

    def handle_collision(self, group, other):
        if group == 'potato:bottle':
            pass

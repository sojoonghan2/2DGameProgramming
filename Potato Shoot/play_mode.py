from pico2d import *
import game_framework
import game_world
from ground import Ground
from potato import Potato
from bottle import Bottle
from water import Water
from point import Point

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            potato.handle_event(event)

def init():
    global running
    global ground
    global team
    global world
    global potato
    global bottle
    global water

    running = True
    world = []

    # 땅
    ground = Ground()
    game_world.add_object(ground, 0)

    # 물
    water1 = Water(-230, -120)
    game_world.add_object(water1, 1)
    water2 = Water(230, -120)
    game_world.add_object(water2, 1)

    # 병
    # 4열 4개
    bottle1 = Bottle(80, 800)
    game_world.add_object(bottle1, 2)
    bottle2 = Bottle(160, 800)
    game_world.add_object(bottle2, 2)
    bottle3 = Bottle(240, 800)
    game_world.add_object(bottle3, 2)
    bottle4 = Bottle(320, 800)
    game_world.add_object(bottle4, 2)
    # 3열 3개
    bottle5 = Bottle(120, 770)
    game_world.add_object(bottle5, 2)
    bottle6 = Bottle(200, 770)
    game_world.add_object(bottle6, 2)
    bottle7 = Bottle(280, 770)
    game_world.add_object(bottle7, 2)
    # 2열 2개
    bottle8 = Bottle(160, 740)
    game_world.add_object(bottle8, 2)
    bottle9 = Bottle(240, 740)
    game_world.add_object(bottle9, 2)
    # 1열 1개
    bottle10 = Bottle(200, 710)
    game_world.add_object(bottle10, 2)

    # 감자
    potato = Potato(250, 100)
    game_world.add_object(potato, 2)





def finish():
    game_world.clear()
    pass


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass


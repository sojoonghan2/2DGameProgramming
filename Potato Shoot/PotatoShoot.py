from pico2d import *

from ground import Ground
from potato import Potato
from bottle import Bottle
from water import Water

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            potato.handle_event(event)


def reset_world():
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
    world.append(ground)

    # 물
    water1 = Water(-230, -120)
    world.append(water1)
    water2 = Water(230, -120)
    world.append(water2)

    # 병
    # 4열 4개
    bottle1 = Bottle(80, 800)
    world.append(bottle1)
    bottle2 = Bottle(160, 800)
    world.append(bottle2)
    bottle3 = Bottle(240, 800)
    world.append(bottle3)
    bottle4 = Bottle(320, 800)
    world.append(bottle4)
    # 3열 3개
    bottle5 = Bottle(120, 770)
    world.append(bottle5)
    bottle6 = Bottle(200, 770)
    world.append(bottle6)
    bottle4 = Bottle(280, 770)
    world.append(bottle4)
    # 2열 2개
    bottle5 = Bottle(160, 740)
    world.append(bottle5)
    bottle6 = Bottle(240, 740)
    world.append(bottle6)
    # 1열 1개
    bottle7 = Bottle(200, 710)
    world.append(bottle7)

    # 감자
    potato = Potato(250, 100)
    world.append(potato)



def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas(540, 960)
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()

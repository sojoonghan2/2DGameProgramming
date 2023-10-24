from pico2d import *

from ground import Ground
from potato import Potato
from bottle import Bottle


# Game object class here


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

    running = True
    world = []

    ground = Ground()
    world.append(ground)

    # 4열 4개
    bottle1 = Bottle(70, 500)
    world.append(bottle1)
    bottle2 = Bottle(110, 500)
    world.append(bottle2)
    bottle3 = Bottle(150, 500)
    world.append(bottle3)
    bottle4 = Bottle(190, 500)
    world.append(bottle4)
    # 3열 3개
    bottle5 = Bottle(90, 480)
    world.append(bottle5)
    bottle6 = Bottle(130, 480)
    world.append(bottle6)
    bottle4 = Bottle(170, 480)
    world.append(bottle4)
    # 2열 2개
    bottle5 = Bottle(110, 460)
    world.append(bottle5)
    bottle6 = Bottle(150, 460)
    world.append(bottle6)
    # 1열 1개
    bottle7 = Bottle(130, 440)
    world.append(bottle7)

    potato = Potato()
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


open_canvas(360, 640)
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()

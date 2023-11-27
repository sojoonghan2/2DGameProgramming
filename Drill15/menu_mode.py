import random
import json
import tomllib
import pickle
import os

from pico2d import *
import game_framework
import game_world

import server
import play_mode

from boy import Boy
from zombie import Zombie
from background import FixedBackground as Background


def init():
    global menu
    menu = load_image('menu.png')
    hide_cursor()
    hide_lattice()

def finish():
    global menu
    menu = None

def pause():
    pass

def resume():
    pass


def create_new_world():
    server.background = Background()
    game_world.add_object(server.background, 0)

    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    # 하드 코딩
    # game_world.add_object(Zombie('zwi', 3800, 2560, 1.0), 1)
    # game_world.add_object(Zombie('jeni', 4000, 2560, 2.0), 1)
    # game_world.add_object(Zombie('jisu', 5000, 2560, 0.5), 1)

    # 소프트 코딩
    # 파일을 오픈해서 f에 연결
    with open('zombie_data.toml', 'rb') as f:
        zombie_data_list = tomllib.load(f)['zombies']
        for item in zombie_data_list:
            # zombie = Zombie(item['name'], item['x'], item['y'], item['size'])
            zombie = Zombie()
            zombie.__dict__.update(item)
            game_world.add_object(zombie, 1)



def load_saved_world():
    # fill here
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            create_new_world()
            game_framework.change_mode(play_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load_saved_world()
            game_framework.change_mode(play_mode)

def update():
    pass

def draw():
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)
    update_canvas()







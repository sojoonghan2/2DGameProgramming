from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('Circle')

    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    delay(1)
    pass
def run_rectangle():
    print('Rectangle')
    pass

while(True):
    run_circle()
    run_rectangle()

close_canvas()

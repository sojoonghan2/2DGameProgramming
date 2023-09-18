import math
from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x = 0
y = 90
move = 0
circle = False
while(True):
    # ract
    while (circle == False):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        if (x > 800):
            move = 1
        if (y > 600 and move == 1):
             move = 2
        if (x < 0 and move == 2):
             move = 3
        if (y < 90 and move == 3):
            move = 0
    
        
        if (move == 0):
            x = x + 2
        if (move == 1):
            y = y + 2
        if (move == 2):
            x = x - 2
        if (move == 3):
            y = y - 2
        delay(0.01)
        
close_canvas()

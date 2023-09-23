from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('sp_image.png')

x = 800
frame = 0
switch = 0
while (x > 0):
    clear_canvas()
    grass.draw(400, 30)
    if (switch < 6):
        character.clip_draw(frame * 90, 310, 90, 70, x, 70)
        switch += 1
    if (switch < 12 and switch >= 6):
        character.clip_draw(frame * 90, 180, 90, 70, x, 70)
        switch += 1
    if (switch >= 12):
        switch = 0
    update_canvas()
    frame = (frame + 1) % 6
    x -= 5
    delay(0.05)
    get_events()

close_canvas()

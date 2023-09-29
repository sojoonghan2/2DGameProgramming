from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hand_xPos, hand_yPos = TUK_WIDTH // 2, TUK_HEIGHT // 2
movement_interval = 0.01

def movetohand():
    global hand_xPos
    global hand_yPos
    global x
    global y
    global frame

    dx = hand_xPos - x
    dy = hand_yPos - y
    direction = (dx > 0)

    for i in range(0, 100 + 1, 1):
        t = i / 100
        x = (1 - t) * x + t * hand_xPos
        y = (1 - t) * y + t * hand_yPos
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(hand_xPos, hand_yPos)

        if direction:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)

        update_canvas()
        frame = (frame + 1) % 8


while running:
    movetohand()
    delay(movement_interval)

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                hand_xPos, hand_yPos = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_QUIT:
            running = False

close_canvas()
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
hand_yPos = 0
hand_xPos = 0
temp_xPos = 0
temp_yPos = 0

hide_cursor()

def makehand():
    global hand_xPos
    global hand_yPos
    global temp_xPos
    global temp_yPos
    hand_xPos, hand_yPos = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

def movetohand():
    global hand_xPos
    global hand_yPos
    global temp_xPos
    global temp_yPos
    global x
    global y
    global frame
    for i in range(0, 100 + 1, 1):
        t = i / 100
        x = (1 - t) * x + t * hand_xPos
        y = (1 - t) * y + t * hand_yPos
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if (hand_xPos - temp_xPos) > 0:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
        hand.draw(hand_xPos, hand_yPos)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)

makehand()
movetohand()

while True:
    if x == hand_xPos and y == hand_yPos:
        temp_xPos = hand_xPos
        temp_yPos = hand_yPos
        makehand()
        movetohand()

close_canvas()

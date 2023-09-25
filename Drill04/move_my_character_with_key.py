from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 720
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite_image.png')


def handle_events():
    global running, dir, dir2, way
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                way = 0
            elif event.key == SDLK_LEFT:
                dir -= 1
                way = 1
            elif event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += 1


def draw_image():
    global switch
    update_canvas()
    handle_events()
    switch += 1


running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dir = 0
dir2 = 0
way = 0
switch = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    x += dir * 5
    y += dir2 * 5

    x = clamp(0, x, TUK_WIDTH)
    y = clamp(0, y, TUK_HEIGHT)

    if switch < 3:
        if way == 1:
            character.clip_composite_draw(frame * 220, 820, 200, 180, 0, 'r', x, y, 200, 200)
        elif way == 0:
            character.clip_composite_draw(frame * 220, 820, 200, 180, 0, 'h', x, y, 200, 200)
        draw_image()
        frame = (frame + 1) % 3
    elif (switch < 7) and (switch >= 3):
        if way == 1:
            character.clip_composite_draw(frame * 220, 600, 200, 180, 0, 'r', x, y, 200, 200)
        elif way == 0:
            character.clip_composite_draw(frame * 220, 600, 200, 180, 0, 'h', x, y, 200, 200)
        draw_image()
        frame = (frame + 1) % 4
    elif (switch < 11) and (switch >= 7):
        if way == 1:
            character.clip_composite_draw(frame * 185, 990, 160, 135, 0, 'r', x + 20, y + 20, 170, 160)
        elif way == 0:
            character.clip_composite_draw(frame * 185, 990, 160, 135, 0, 'h', x - 20, y + 20, 170, 160)
        draw_image()
        frame = (frame + 1) % 4
    elif switch >= 11:
        switch = 0

    delay(0.05)

close_canvas()
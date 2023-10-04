from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 720


def load_resources():
    global TUK_ground, character, arrow

    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        # 클릭된 위치를 새로운 점으로 추가
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            points.append((mx, my))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_World():
    global running, cx, cy, frame
    global t
    global action
    global mx, my
    global points

    mx, my = 0, 0
    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3

    points = []
    set_new_target_arrow()


def set_new_target_arrow():
    global sx, sy, hx, hy, t
    global action
    global frame
    global target_exists

    # points 리스트안에 남아있는 점이 있으면
    if points:
        # 시작점
        sx, sy = cx, cy
        # 끝점
        hx, hy = points[0]
        t = 0.0
        action = 1 if sx < hx else 0
        frame = 0
        target_exists = True
    else:
        # 이전에 소년이 우측으로 이동중 이였으면, IDLE 동작시 우측을 바라보도록
        action = 3 if action == 1 else 2
        frame = 0
        target_exists = False


def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for p in points:
        arrow.draw(p[0], p[1])
    arrow.draw(mx, my)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()


def update_world():
    global frame
    global cx, cy
    global t
    global action

    frame = (frame + 1) % 8

    if target_exists:
        if t <= 1.0:
            cx = (1 - t) * sx + t * hx
            cy = (1 - t) * sy + t * hy
            t += 0.001
        # 목표 지점에 도달하면
        else:
            # 캐릭터 위치를 목적지 위치와 정확히 일치시킴
            cx, cy = hx, hy
            # 목표 지점에 도착시, 필요 없는 점 제거
            del points[0]
            set_new_target_arrow()
    elif points:
        set_new_target_arrow()


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_World()

while running:
    # 월드의 현재 내용을 그림
    render_world()
    # 사용자 입력을 받음
    handle_events()
    # 월드 안의 객체 들의 상호 작용을 계산, 결과를 Update
    update_world()

close_canvas()

from pico2d import *


# Pico-2D 초기화
pico2d.open_canvas(1280, 720)

# 볼링 핀과 공 이미지 로드
pin_image = pico2d.load_image('')
ball_image = pico2d.load_image('')

# 핀과 공의 초기 위치 및 속도 설정
pin_x, pin_y = 400, 300
ball_x, ball_y = 400, 100
ball_speed_x, ball_speed_y = 0, 0

running = True
while running:
    pico2d.clear_canvas()

    # 입력 처리
    if pico2d.key.is_pressed(pico2d.SPACE):
        # 스페이스바를 누르면 공을 던짐
        ball_speed_x, ball_speed_y = calculate_ball_speed()

    # 게임 로직 업데이트
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 충돌 검사 및 핀 넘어짐 처리

    # 게임 객체 그리기
    pin_image.draw(pin_x, pin_y)
    ball_image.draw(ball_x, ball_y)

    pico2d.update_canvas()

def calculate_ball_speed():
    # 공의 속도 계산 로직
    pass

def check_collision():
    # 충돌 검사 로직
    pass

pico2d.close_canvas()
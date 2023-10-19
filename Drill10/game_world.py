# 게임 월드 관리 모듈

# 게임 월드의 표현
objects = []


# 월드에 객체를 넣는 함수
def add(o):
    objects.append(o)


# 월드를 업데이트하는, 객체들을 모두 업데이트하는 함수
def update():
    for o in objects:
        o.update()


# 월드 객체들을 모두 그리기
def render():
    for o in objects:
        o.draw()


def remove_object(o):
    objects.remove(o)
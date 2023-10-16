from pico2d import load_image


class Ground:
    def __init__(self):
        self.image = load_image('ground.png')

    def draw(self):
        self.image.draw_to_origin(0, 0, 540, 960)

    def update(self):
        pass

from pico2d import load_image


class Bottle:
    image = None

    def __init__(self, x = 140, y = 500):
        if Bottle.image == None:
            Bottle.image = load_image('Resource\\Bottle\\Bottle.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw_to_origin(self.x, self.y, 130, 180)

    def update(self):
        pass

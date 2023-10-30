from pico2d import get_events, load_image, clear_canvas, update_canvas, get_time

def init():
    global image
    global running
    global logo_start_time

    logo_start_time = get_time()
    image = load_image('tuk_credit.png')
    running = True

def finish():
    pass

def update():
    global running

    if get_time() - logo_start_time >= 2.0:
        running = False

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
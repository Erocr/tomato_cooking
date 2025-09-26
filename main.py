from Inputs import Inputs
from View import View
from Vec import *
from Grid import *
import time

FPS = 50

view = View()
inputs = Inputs()
grid = Grid(Vec(10, 10))


while not inputs.quit:
    start = time.time()
    inputs.update()

    view.draw_tile(Vec(1920, 1080)/2, "tomatest", 0)

    view.update(inputs.get_resized())
    view.fill()

    t = time.time() - start
    if t < 1/FPS:
        time.sleep(1/FPS - t)

from Inputs import Inputs
from View import View
from Vec import *
from Grid import *
import time

FPS = 50

view = View()
inputs = Inputs()
grid = Grid(Vec(10, 10))

grid.tomatoes[5][3].append(Tomato(Vec(3, 5), Vec(1, 0), 0))
grid.tomatoes[5][4].append(Tomato(Vec(4, 5), Vec(1, 0), 0))

while not inputs.quit:
    start = time.time()
    inputs.update()

    view.draw_grid(grid)

    view.update(inputs.get_resized())
    view.fill()

    t = time.time() - start
    if t < 1/FPS:
        time.sleep(1/FPS - t)

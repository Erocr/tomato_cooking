from Inputs import Inputs
from View import View
from Vec import *
from Grid import *
import time

FPS = 50

view = View()
inputs = Inputs()
grid = Grid(Vec(10, 10))

grid.add_tomato(Tomato(Vec(3, 5), Vec(1, 0), 0))
grid.add_tomato(Tomato(Vec(5, 5), Vec(-1, 0), 0))


frame_count = 0
while not inputs.quit:
    frame_count += 1
    start = time.time()
    inputs.update()

    if frame_count % 25 == 0:
        grid.one_turn()

    view.fill()
    view.draw_grid(grid)
    view.update(inputs.get_resized())

    t = time.time() - start
    if t < 1/FPS:
        time.sleep(1/FPS - t)

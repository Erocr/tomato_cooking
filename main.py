from Inputs import Inputs
from View import View
from Vec import *
from Grid import *
import time
from random import random, choice

FPS = 50

view = View()
inputs = Inputs()
grid = Grid(Vec(10, 10))

for i in range(15):
    grid.add_tomato(Tomato(Vec(random()*10, random()*10), choice([Vec(1, 0), Vec(-1, 0), Vec(0, -1), Vec(0, 1)]), 0))


frame_count = 0
while not inputs.quit:
    frame_count += 1
    start = time.time()
    inputs.update()

    if frame_count % 25 == 0:
        grid.one_turn()

    view.fill()
    view.draw_grid(grid, (frame_count % 25)/25)
    view.update(inputs.get_resized())

    t = time.time() - start
    if t < 1/FPS:
        time.sleep(1/FPS - t)

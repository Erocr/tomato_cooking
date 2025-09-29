from Inputs import Inputs
from View import *
from Vec import *
from Grid import *
from Button import *
import time
from random import random, choice

FPS = 50

view = View()
inputs = Inputs()
grid = Grid(Vec(10, 10))

for i in range(15):
    grid.add_tomato(Tomato(Vec(random()*10, random()*10), choice([Vec(1, 0), Vec(-1, 0), Vec(0, -1), Vec(0, 1)]), int(random()*4)))


grid.add_tomato(Tomato(Vec(0, 0), Vec(0, 1), 0))
grid.grid[0][0] = OnMapObstacle(Vec(0, 0), 2)
grid.grid[5][0] = OnMapObstacle(Vec(0, 5), 8)
grid.grid[5][5] = OnMapObstacle(Vec(5, 5), 13)


state = "placing"


def run_function(button):
    global state
    if button.image_id == 0:
        state = "running"
        button.image_id = 2
    else:
        state = "placing"
        button.image_id = 0


grid.add_button(Button(0, run_function, Vec(12, 0)))

frame_count = 0
while not inputs.quit:
    frame_count += 1
    start = time.time()
    inputs.update()

    grid.update(inputs)
    if inputs.get_pressed(pg.K_p):
        state = ("placing", "running")[state == "placing"]
        frame_count = 1

    if state == "running":
        if frame_count % 25 == 0:
            grid.one_turn()

    view.fill()
    if state == "running":
        view.draw_grid(grid, (frame_count % 25)/25)
    else:
        view.draw_grid(grid, 0)
    view.update(inputs.get_resized())

    t = time.time() - start
    if t < 1/FPS:
        time.sleep(1/FPS - t)

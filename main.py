from Inputs import Inputs
from View import View
from Vec import *
from Grid import *

view = View()
inputs = Inputs()
grid = Grid(Vec(10, 10))


while not inputs.quit:
    inputs.update()

    view.draw_tile(Vec(1920, 1080)/2, "tomatest", 0)

    view.update(inputs.get_resized())
    view.fill()

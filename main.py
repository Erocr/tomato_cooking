from Inputs import Inputs
from View import View
from Vec import *

view = View()
inputs = Inputs()


while not inputs.quit:
    inputs.update()

    view.draw_sprite("tomatest", Vec(1920/2, 1080/2))

    view.update(inputs.get_resized())
    view.fill()

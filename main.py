from Inputs import Inputs
from View import View

view = View()
inputs = Inputs()


while not inputs.quit:
    inputs.update()

    view.update(inputs.get_resized())

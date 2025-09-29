from Vec import *
from View import View


class Button:
    def __init__(self, image_id, function, position, size=Vec(1, 1)):
        """ function prend comme paramètre le bouton lui-même """
        self.image_id = image_id
        self.function = function
        self.pos = position
        self.size = size

        self.mouse_on = False

    def update(self, inputs):
        mouse_pos = View.screen2grid(inputs.mouse_pos)
        mouse_on = (self.pos.x <= mouse_pos.x < self.pos.x + self.size.x and
                    self.pos.y <= mouse_pos.y < self.pos.y + self.size.y)
        self.mouse_on = mouse_on
        if self.mouse_on and inputs.mouse_pressed:
            self.function(self)
            self.mouse_on = False

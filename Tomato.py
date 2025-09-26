class Tomato:
    def __init__(self, pos, direction, type_):
        self.pos = pos
        self.dir = direction
        self.type = type_
        self.to_draw_pos = pos

    def one_turn(self, grid):
        if grid.is_legal(self.pos+self.dir, self.dir):
            self.pos += self.dir
        else:
            self.dir = -self.dir

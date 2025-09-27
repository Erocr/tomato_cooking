class Tomato:
    def __init__(self, pos, direction, type_):
        self.pos = pos
        self.dir = direction
        self.type = type_
        self.path = [pos]

    def move(self, grid):
        self.path = [self.path[-1]]
        if grid.is_legal(self.pos+self.dir, self.dir):
            grid.move_tomato(self, self.pos+self.dir)
            self.path.append(self.pos)
        else:
            self.path.append(self.pos + self.dir/2)
            self.path.append(self.pos)
            self.dir = -self.dir

    def apply_collision_visuals(self, grid):
        if grid.nb_tomatoes_at(self.pos) > 1:
            self.path[-1] = self.pos - self.dir / 4



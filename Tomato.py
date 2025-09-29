class Tomato:
    def __init__(self, pos, direction, type_):
        self.pos = pos
        self.dir = direction
        self.type = type_ #0 : tomate normale, 1 tomatiguée, 2 frustomate, 3 tomatriste
        self.path = [pos]
        self.hit = 0 #pour savoir combien de fois les frustomates ont tapé qq

    
    def change_type(self, new_type):
        self.type = new_type

    def move(self, grid):
        self.path = [self.path[-1]]
        if grid.is_legal(self.pos+self.dir, self.dir):
            grid.move_tomato(self, self.pos+self.dir)
            self.path.append(self.pos)
        else:
            self.path.append(self.pos + self.dir / 4)
            self.path.append(self.pos)
            self.dir = -self.dir

    def apply_collision_visuals(self, grid):
        if grid.nb_tomatoes_at(self.pos) > 1:
            self.path[-1] = self.pos - self.dir / 4

    def lerped_position(self, t):
        if len(self.path) == 1:
            return self.path[0]
        t *= len(self.path) - 1
        path_i = int(t)
        t -= path_i
        return self.path[path_i] + (self.path[path_i + 1] - self.path[path_i]) * t

    def interact(self, tomato):
        if self.type == 0:
            if tomato.type == 1:
                self.type = 1
            elif tomato.type == 2 :
                self.type = 3
                tomato.hit += 1
            elif tomato.type == 3: pass
        elif self.type == 1:
            if tomato.type == 0:
                tomato.type = 1
            elif tomato.type == 2 :
                self.type = 0
            elif tomato.type == 3: pass
        elif self.type == 2:
            if tomato.type == 0:
                tomato.type = 3
                self.hit += 1
            elif tomato.type == 1:
                tomato.type = 0
            elif tomato.type == 2:
                tomato.hit += 1
                self.hit += 1
            elif tomato.type == 3:
                self.hit += 1
        elif self.type == 3:
            if tomato.type == 0: pass
            elif tomato.type == 1: pass
            elif tomato.type == 2:
                tomato.hit += 1
            elif tomato.type == 3: pass
        
        if self.hit >= 3:
            self.type = 1
            self.hit = 0
        if tomato.hit >= 3:
            tomato.type = 1
            self.hit = 0



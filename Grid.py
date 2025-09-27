from typing import Optional
from OnMapObstacle import *
from Tomato import *


class Grid:
    def __init__(self, size):
        self.grid: list[list[Optional[OnMapObstacle]]] = [[None for _ in range(int(size.x))] for _ in range(int(size.y))]
        self.tomatoes: list[list[list[Tomato]]] = [[[] for _ in range(int(size.x))] for _ in range(int(size.y))]
        self.tomatoes_list = []

    def add_tomato(self, tomato):
        tomato.pos = tomato.pos.to_int()
        assert self.is_in_grid(tomato.pos), "La tomate ajoutée est au-dehors de la grille"
        self.tomatoes_list.append(tomato)
        self.tomatoes[tomato.pos.y][tomato.pos.x].append(tomato)

    def remove_tomato(self, tomato):
        self.tomatoes[tomato.pos.y][tomato.pos.x].remove(tomato)
        self.tomatoes_list.remove(tomato)

    def move_tomato(self, tomato, new_pos):
        self.tomatoes[tomato.pos.y][tomato.pos.x].remove(tomato)
        self.tomatoes[new_pos.y][new_pos.x].append(tomato)
        tomato.pos = new_pos

    def one_turn(self):
        for tomato in self.tomatoes_list:
            tomato.move(self)
        for tomato in self.tomatoes_list:
            tomato.apply_collision_visuals(self)
        for line in self.tomatoes:
            for tomatoes in line:
                if len(tomatoes) == 2:
                    tomatoes[0].dir, tomatoes[1].dir = tomatoes[1].dir, tomatoes[0].dir
                elif len(tomatoes) > 2:
                    for tomato in tomatoes:
                        tomato.dir = -tomato.dir

    def is_legal(self, pos, direction):
        if not self.is_in_grid(pos):
            return False
        if self.grid[pos.y][pos.x] is None:
            return True
        else:
            return not self.grid[pos.y][pos.x].is_illegal_direction(direction)

    def is_in_grid(self, pos):
        return 0 <= pos.x < len(self.grid[0]) and 0 <= pos.y < len(self.grid[1])

    def nb_tomatoes_at(self, pos):
        return len(self.tomatoes[int(pos.y)][int(pos.x)])

    def other_tomato_at(self, pos, tomato):
        ts = self.tomatoes[int(pos.y)][int(pos.x)]
        if ts[0] == tomato: return ts[1]
        else: return ts[0]


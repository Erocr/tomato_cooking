from typing import Optional
from OnMapObstacle import *
from Tomato import *


class Grid:
    def __init__(self, size):
        self.grid: list[list[Optional[OnMapObstacle]]] = [[None for _ in range(int(size.x))] for _ in range(int(size.y))]
        self.tomatoes: list[list[Optional[Tomato]]] = [[None for _ in range(int(size.x))] for _ in range(int(size.y))]

    def is_legal(self, pos, direction):
        if not self.is_in_grid(pos):
            return False
        if self.grid[pos.y][pos.x] is None:
            return True
        else:
            return not self.grid[pos.y][pos.x].is_illegal_direction(direction)

    def is_in_grid(self, pos):
        return 0 <= pos.x < len(self.grid[0]) and 0 <= pos.y < len(self.grid[1])


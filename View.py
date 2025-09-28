from os import listdir
from Tileset import *
from Shader import *
from OnMapObstacle import *


class View:
    def __init__(self):
        pg.display.set_mode((Vec(860, 540)).get(), pg.RESIZABLE | pg.OPENGL | pg.DOUBLEBUF)
        self.display = pg.Surface((1920, 1080))
        self.shader = Shader2D()

        self.tileSize = Vec(100, 100)

        self.tilesets: dict[str, Tileset] = {}
        self.load_tilesets()

    def load_tilesets(self):
        for file in listdir("sprites/"):
            self.tilesets[file.split(".")[0]] = Tileset("sprites/"+file,  self.tileSize/2)

    def draw_tile(self, screen_position, tileset, tile_id):
        self.tilesets[tileset].blit_tile(screen_position, tile_id, self.display)

    def update(self, window_resized):
        self.shader.add_uniform("image", self.display)
        self.shader.render()
        pg.display.flip()

    def draw_grid(self, grid, t):
        pg.draw.rect(self.display, (255, 255, 255), pg.Rect(*self.grid2screen(Vec(-1/2, -1/2)).get(),
                                                            *self.grid2screen(Vec(len(grid.grid)-1/2, len(grid.grid[0])-1/2)).get()))
        for y in range(len(grid.grid)):
            for x in range(len(grid.grid[y])):
                if grid.grid[y][x] is not None:
                    screen_position = self.grid2screen(Vec(x, y))
                    if isinstance(grid.grid[y][x], OnMapObstacle):
                        grid.grid[y][x].draw(screen_position, self)
                    else:
                        assert False, "not done yet"
                for tomato in grid.tomatoes[y][x]:
                    self.draw_tile(self.grid2screen(tomato.lerped_position(t)), "tomatest", tomato.type)

    def grid2screen(self, v):
        return Vec(100, 100) + v * self.tileSize

    def fill(self):
        self.display.fill((0, 0, 0))


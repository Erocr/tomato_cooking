from os import listdir
from Tileset import *
from Shader import *


class View:
    tileSize = Vec(100, 100)

    def __init__(self):
        pg.display.set_mode((Vec(860, 540)).get(), pg.RESIZABLE | pg.OPENGL | pg.DOUBLEBUF)
        self.display = pg.Surface((1920, 1080))
        self.shader = Shader2D()

        self.tilesets: dict[str, Tileset] = {}
        self.load_tilesets()

    def load_tilesets(self):
        for file in listdir("sprites/"):
            self.tilesets[file.split(".")[0]] = Tileset("sprites/"+file,  self.tileSize/2)

    def draw_tile(self, screen_position, tileset, tile_id, size=None):
        self.tilesets[tileset].blit_tile(screen_position, tile_id, self.display, size)

    def update(self, window_resized):
        self.shader.add_uniform("image", self.display)
        self.shader.render()
        pg.display.flip()

    def draw_grid(self, grid, t):
        pg.draw.rect(self.display, (255, 255, 255), pg.Rect(0, 0,
                                                            *self.grid2screen(Vec(len(grid.grid), len(grid.grid[0]))+Vec(0.25, 0.25)).get()))
        for y in range(len(grid.grid)):
            for x in range(len(grid.grid[y])):
                if grid.grid[y][x] is not None:
                    screen_position = self.grid2screen(Vec(x, y))
                    assert False, "not done yet"
                for tomato in grid.tomatoes[y][x]:
                    self.draw_tile(self.grid2screen(tomato.lerped_position(t)+Vec(0.25, 0.25)), "tomatest", tomato.type)

        for button in grid.buttons:
            self.draw_tile(self.grid2screen(button.pos), "bouttons", button.image_id, button.size*2)

    @staticmethod
    def grid2screen(v):
        return Vec(25, 25) + v * View.tileSize

    @staticmethod
    def screen2grid(v):
        return ((v - Vec(25, 25)) / View.tileSize).to_int()

    def fill(self):
        self.display.fill((0, 0, 0))


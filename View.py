from os import listdir
from Tileset import *
from Shader import *


class View:
    def __init__(self):
        self.screen = pg.display.set_mode((Vec(860, 540)).get(), pg.RESIZABLE | pg.OPENGL | pg.DOUBLEBUF)
        self.display = pg.Surface((1920, 1080))
        self.tilesets: dict[str, Tileset] = {}
        self.load_tilesets()
        self.shader = Shader2D()

    def load_tilesets(self):
        for file in listdir("sprites/"):
            self.tilesets[file.split(".")[0]] = Tileset("sprites/"+file,  Vec(50, 50))

    def draw_tile(self, screen_position, tileset, tile_id):
        self.tilesets[tileset].blit_tile(screen_position, tile_id, self.display)

    def update(self, window_resized):
        self.shader.add_uniform("image", self.display)
        self.shader.render()
        pg.display.flip()

    def draw_circle(self, center, radius, color=(0, 0, 0)):
        pg.draw.circle(self.screen, color, center.get(), radius)

    def fill(self):
        self.screen.fill((0, 0, 0))


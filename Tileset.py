import pygame as pg
from Vec import *


class Tileset:
    def __init__(self, filename, tile_size):
        self.image = pg.image.load(filename)
        self.tileSize = tile_size
        self.size = (Vec(*self.image.get_size()) / self.tileSize).to_int()

    def blit_tile(self, pos, tile_id, screen: pg.Surface):
        my_pos = Vec(*divmod(tile_id, self.size.x)[::-1])
        screen.blit(self.image, pos.get(), pg.Rect(*my_pos.get(), *self.tileSize.get()))

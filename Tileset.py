import pygame as pg
from Vec import *


class Tileset:
    def __init__(self, filename, tile_size):
        self.image = pg.image.load(filename)
        self.tileSize = tile_size
        image_size = Vec(*self.image.get_size())
        self.size = (image_size / self.tileSize).to_int()

    def blit_tile(self, pos, tile_id, screen: pg.Surface, size=None):
        """ size in tiles (50x50 px) """
        if size is None:
            my_pos = Vec(*divmod(tile_id, self.size.x)[::-1]) * self.tileSize
            screen.blit(self.image, pos.get(), pg.Rect(*my_pos.get(), *self.tileSize.get()))
        else:
            for x in range(size.x):
                for y in range(size.y):
                    self.blit_tile(Vec(pos.x+x*50, pos.y+y*50), tile_id+x+y*self.size.x, screen)

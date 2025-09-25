import pygame as pg
from Vec import *
from os import listdir


class View:
    def __init__(self):
        self.factor = Vec(600, 600) / Vec(1920, 1080)
        self.screen = pg.display.set_mode((Vec(1920, 1080) * self.factor).get(), pg.RESIZABLE)
        self.sprites = {}
        self.standard_scale_sprites = {}
        self.load_sprites()
        self.resize_sprites()

    def load_sprites(self):
        for file in listdir("sprites/"):
            im = pg.image.load("sprites/"+file)
            self.standard_scale_sprites[file.split(".")[0]] = im

    def resize_sprites(self):
        for sprite in self.standard_scale_sprites:
            self.sprites[sprite] = pg.transform.scale_by(self.standard_scale_sprites[sprite], self.factor.get())

    def draw_sprite(self, image, position):
        self.screen.blit(self.sprites[image], self.game2screen(position).get())

    def game2screen(self, coord):
        return coord * self.factor

    def screen2game(self, coord):
        return coord / self.factor

    def update(self, window_resized):
        pg.display.flip()
        if window_resized:
            new_size = Vec(*pg.display.get_window_size())
            self.factor = new_size / Vec(1920, 1080)
            self.resize_sprites()

    def draw_circle(self, center, radius, color=(0, 0, 0)):
        pg.draw.circle(self.screen, color, center.get(), radius)

    def fill(self):
        self.screen.fill((0, 0, 0))


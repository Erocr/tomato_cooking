import pygame as pg
from Vec import *


class View:
    def __init__(self):
        self.factor = Vec(600, 600) / Vec(1920, 1080)
        self.screen = pg.display.set_mode((Vec(1920, 1080) * self.factor).get(), pg.RESIZABLE)

    def game2screen(self, coord):
        return coord * self.factor

    def screen2game(self, coord):
        return coord / self.factor

    def update(self, window_resized):
        pg.display.flip()
        if window_resized:
            new_size = Vec(*pg.display.get_window_size())
            self.factor = new_size / Vec(1920, 1080)

    def draw_circle(self, center, radius, color=(0, 0, 0)):
        pg.draw.circle(self.screen, color, center.get(), radius)

    def fill(self):
        self.screen.fill((0, 0, 0))


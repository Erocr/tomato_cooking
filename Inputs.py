import pygame as pg
from Vec import *


class Inputs:
    """
    In the architecture MVC (Model View Controller), Inputs is the Controller.
    So it's one of the greatest and more high-level class.

    Inputs must manage all the inputs of the player.

    Warning: think to call update once per frame
    """
    def __init__(self):
        # keysPressed, keysReleased and keysHolding are sets of pygame key ids
        # For example, pg.K_RIGHT is pygame key id
        self.__keysPressed = set()
        self.__keysReleased = set()
        self.__keysHolding = set()

        self.__isResized = False
        self.__quit = False
        self.__mouse_pos = Vec(0, 0)
        self.__mouse_pressed = False
        self.__mouse_holding = False

        self.window_size_factor = Vec(0, 0)

    def update(self):
        """
        This function is VERY important !!!!!!
        You must call it once per frame, EXACTLY ONCE per frame, not more, not less !
        It listens the inputs of the player, and stores them.
        """
        self.__isResized = False
        self.__keysPressed = set()
        self.__keysReleased = set()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__quit = True
            elif event.type == pg.KEYDOWN:
                self.__keysPressed.add(event.key)
                self.__keysHolding.add(event.key)
            elif event.type == pg.KEYUP:
                self.__keysReleased.add(event.key)
                self.__keysHolding.remove(event.key)
            elif event.type == pg.VIDEORESIZE:
                self.__isResized = True
        mouse_holding = pg.mouse.get_pressed()[0]
        self.__mouse_pressed = not self.__mouse_holding and mouse_holding
        self.__mouse_holding = mouse_holding
        self.__mouse_pos = Vec(*pg.mouse.get_pos())

# getters --------------------------------------------------------------------------------------------------------------

    @property
    def isResized(self):
        return self.__isResized

    @property
    def quit(self):
        return self.__quit

    @property
    def mouse_pos(self):
        info = pg.display.Info()
        w, h = info.current_w, info.current_h
        return self.__mouse_pos / Vec(w, h) * Vec(1920, 1080)

    @property
    def mouse_pressed(self):
        return self.__mouse_pressed

    def get_pressed(self, key: int):
        """
        :param key: the pygame key id. For example, pg.K_RIGHT is for the right arrow
        :return: if it has been pressed during this frame.
        """
        return key in self.__keysPressed

    def get_released(self, key):
        """
        :param key: the pygame key id. For example, pg.K_RIGHT is for the right arrow
        :return: if it has been released during this frame.
        """
        return key in self.__keysReleased

    def get_holding(self, key):
        """
        :param key: the pygame key id. For example, pg.K_RIGHT is for the right arrow
        :return: if the player is holding this key.
        """
        return key in self.__keysHolding

    def get_resized(self):
        return self.__isResized

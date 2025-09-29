from OnMapObstacle import * #as OMO
from Grid import *
from View import *


"""bloc = OMO sur lequel on peut passer mais qui a une interraction avec la tomate""" 

"""class Type(OMO):
        def action(self, tomato):
            ...

"""
"""
blocs:arrivée, tapis-roulant (changement direction ou saut ?), 
"""


class Goal(OnMapObstacle):    
    def __init__(self, pos, goal):
        """ forme de goal [1,2,3,4] nb de tomates de type 0,1,..."""
        self.pos = pos
        self.cpt = [0, 0, 0, 0]  # on peut mettre plein de blocs d'arrivée avec des goals différents
        self.goal = goal
        self.done = False
        self.illegalDirectionsEncoded = 0b0000

    def victory(self):
        for i in range(len(self.cpt)):
            if self.cpt[i] <= self.goal[i]:
                return False
        return True
    
    def action(self, grid, tomato):
        grid.remove_tomato(tomato)
        self.cpt[tomato.type] += 1
        self.done = self.victory

    def draw(self, pos, view):
        view.draw_tile(pos, "trou", 0, Vec(2, 2))

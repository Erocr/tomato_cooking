from Grid import *
from Vec import *
from OnMapObstacle import *
from Blocs import *

"""L'idée à terme c'est de faciliter la création de niveaux (aléatoire ?), peut-être que ça sert à rien je me suis un peu perdue"""
class Level:
    def __init__(self, goal :list): #ajouter paramètres : murs, nb blocs à poser, jsp
        self.grid = Grid(Vec(10,10))
        self.grid.grid[5][5] = OnMapObstacle(Vec(0,0), 0b1111) # le paramètre position a-t-il un sens ?
        self.goal_list = []
    
    def victory(self):
        for goal in self.goal_list:
            if not goal.done:
                return False
        return True
    
    def add_bloc(self, bloc):
        if type(bloc) is Goal:
            self.goal_list.append(bloc)
        self.grid.add_bloc(bloc)
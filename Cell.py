import pygame
from random import choice
from Coordinate import *

class Cell:
    def __init__(self, x, y, size):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.size = size
        self.coordinate = Coordinate(self.x, self.y)

    @property
    def Position(self):
    	return self.coordinate

    @property
    def isVisited(self):
    	return self.visited

    @property
    def Walls(self):
    	return self.walls
    
    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * Coordinate.limits["width"]
        if Coordinate.validate_coordinate(x,y):
            return False
        # return grid_cells[find_index(x, y)]

    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False

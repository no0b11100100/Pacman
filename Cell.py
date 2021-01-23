import pygame
from Coordinate import *

class Cell:
    def __init__(self, x, y, size):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.size = size
        self.coordinate = Coordinate(self.x, self.y)
        self.neighbors = [ Coordinate(self.x, self.y - 1),
                            Coordinate(self.x + 1, self.y),
                            Coordinate(self.x, self.y + 1),
                            Coordinate(self.x - 1, self.y) ]
        self.neighbors = [neighbor for neighbor in self.neighbors if Coordinate.validate_coordinate(neighbor)]

    @property
    def Position(self):
        return self.coordinate

    @property
    def isVisited(self):
        return self.visited

    @isVisited.setter
    def isVisited(self, new_status):
        self.visited = new_status

    @property
    def Walls(self):
        return self.walls

    @property
    def Neighbors(self):
        return self.neighbors
    
    def check_neighbors(self):
        neighbors = []
        for neighbor in self.neighbors:
            if not neighbor.visited:
                neighbors.append(neighbor)

        return neighbors

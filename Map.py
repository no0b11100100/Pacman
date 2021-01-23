import pygame
from Cell import *
from random import choice

class Map:
    def __init__(self, width, height, screen):
        pygame.init()
        self.width, self.height = width, height
        self.isGame = True
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.screen.fill(pygame.Color('black'))
        self.tile_size = 50
        Coordinate.limit["width"], Coordinate.limit["height"] = width // self.tile_size, height // self.tile_size
        self.cells = [Cell(col, row, self.tile_size) for row in range(height // self.tile_size) for col in range(width // self.tile_size)]
        self.current_cell = self.cells[0]
        self.stack = []

    def draw_cells(self):
        for cell in self.cells:
            x, y = cell.Position.X * self.tile_size, cell.Position.Y * self.tile_size
            if cell.isVisited:
                pygame.draw.rect(self.screen, pygame.Color('black'), (x, y, self.tile_size, self.tile_size))
            if cell.Walls['top']:
                pygame.draw.line(self.screen, pygame.Color('darkorange'), (x, y), (x + self.tile_size, y), 3)
            if cell.Walls['right']:
                pygame.draw.line(self.screen, pygame.Color('darkorange'), (x + self.tile_size, y), (x + self.tile_size, y + self.tile_size), 3)
            if cell.Walls['bottom']:
                pygame.draw.line(self.screen, pygame.Color('darkorange'), (x + self.tile_size, y + self.tile_size), (x , y + self.tile_size), 3)
            if cell.Walls['left']:
                pygame.draw.line(self.screen, pygame.Color('darkorange'), (x, y + self.tile_size), (x, y), 3)

    def remove_walls(self, current, next):
        dx = current.Position.X - next.Position.X
        if dx == 1:
            current.Walls['left'] = False
            next.Walls['right'] = False
        elif dx == -1:
            current.Walls['right'] = False
            next.Walls['left'] = False
        dy = current.Position.Y - next.Position.Y
        if dy == 1:
            current.Walls['top'] = False
            next.Walls['bottom'] = False
        elif dy == -1:
            current.Walls['bottom'] = False
            next.Walls['top'] = False

    def check_neighbors(self, cell):
        find_index = lambda coordinate: coordinate.X + coordinate.Y * self.width // self.tile_size
        neighbors = []
        for neighbor in cell.Neighbors:
            c = self.cells[find_index(neighbor)]
            if not c.isVisited:
                neighbors.append(c)

        return neighbors

    def generate_map(self):
        self.stack.append(self.current_cell)
        while len(self.stack) != 0:
            self.current_cell.isVisited = True
            neighbors = self.check_neighbors(self.current_cell)
            next_cell = choice(neighbors) if len(neighbors) != 0 else False
            if next_cell:
                next_cell.isVisited = True
                self.stack.append(self.current_cell)
                self.remove_walls(self.current_cell, next_cell)
                self.current_cell = next_cell
            elif self.stack:
                self.current_cell = self.stack.pop()

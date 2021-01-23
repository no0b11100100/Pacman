import pygame
from Cell import *

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

    def draw_cells(self):
        for cell in self.cells:
            x, y = cell.Position.X * self.tile_size, cell.Position.Y * self.tile_size
            if cell.visited:
                pygame.draw.rect(self.screen, pygame.Color('black'), (x, y, self.tile_size, cell.tile_size))
            if cell.walls['top']:
                pygame.draw.line(self.screen, pygame.Color('darkorange'), (x, y), (x + self.tile_size, y), 3)
            if cell.walls['right']:
                pygame.draw.line(self.screen, pygame.Color('darkorange'), (x + self.tile_size, y), (x + self.tile_size, y + self.tile_size), 3)
            if cell.walls['bottom']:
                pygame.draw.line(self.screen, pygame.Color('darkorange'), (x + self.tile_size, y + self.tile_size), (x , y + self.tile_size), 3)
            if cell.walls['left']:
                pygame.draw.line(self.screen, pygame.Color('darkorange'), (x, y + self.tile_size), (x, y), 3)
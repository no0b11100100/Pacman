import pygame
from Map import *
from Coordinate import *
from Player import *
import Ghost

class Game:
    def __init__(self,width, height):
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.tile_size = 50
        self.map = Map(width, height, self.screen, self.tile_size)
        self.isGame = True
        self.tickrate = 60
        self.map.generate_map()
        self.player = Player(self.tile_size)

    def draw(self):
        self.map.draw_cells()
        pygame.draw.circle(self.screen, pygame.Color('yellow'), (self.player.Center), self.player.Radius)
        pygame.display.flip()
        pygame.time.Clock().tick(self.tickrate)

    def Run(self):
        while self.isGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.player.movement()

            self.draw()
            
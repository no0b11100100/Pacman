import pygame
from Map import *
from Coordinate import *
import Player
import Ghost

class Game:
    def __init__(self,width, height):
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.map = Map(width, height, self.screen)
        self.isGame = True
        self.tickrate = 30


    def draw(self):
        self.map.draw_cells()
        pygame.display.flip()
        pygame.time.Clock().tick(self.tickrate)


    def Run(self):
        while self.isGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.draw()
            
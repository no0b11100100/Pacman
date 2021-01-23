import pygame
from Coordinate import *
import math

class Player:
    def __init__(self, tile_size):
        pygame.init()
        self.radius = tile_size / (2 * math.sqrt(2))
        self.center = ((tile_size // 2), tile_size // 2)

    # TODO: allow only one direction
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.center = (self.center[0]-1, self.center[1])
        if keys[pygame.K_RIGHT]:
            self.center = (self.center[0]+1, self.center[1])
        if keys[pygame.K_DOWN]:
            self.center = (self.center[0], self.center[1]+1)
        if keys[pygame.K_UP]:
            self.center = (self.center[0], self.center[1]-1)

    @property
    def Center(self):
        return self.center

    @property
    def Radius(self):
        return self.radius

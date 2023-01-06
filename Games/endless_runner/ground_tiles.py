import pygame, sys
from pygame.math import Vector2

class Ground:
    def __init__(self, pos, texture_path):
        self.pos = pos
        self.texture = pygame.image.load(texture_path)

    def render(self, screen):
        screen.blit(self.texture, self.pos)
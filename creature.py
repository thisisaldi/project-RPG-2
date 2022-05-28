import pygame
from config import *

class Creature(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.direction = pygame.math.Vector2()
        
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * PLAYER_SPEED
        self.rect.y += self.direction.y * PLAYER_SPEED
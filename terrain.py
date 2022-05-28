import pygame
from config import *

class Terrain(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/map.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (2381, 1195))
        
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    
        
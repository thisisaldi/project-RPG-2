import pygame
from config import *

class Terrain(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/map/map_arena.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * MAP_SCALE, self.image.get_height() * MAP_SCALE))
        
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
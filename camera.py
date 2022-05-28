import pygame
from config import *
from terrain import Terrain

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
           
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - (WINDOW_WIDTH / 2)
        self.offset.y = player.rect.centery - (WINDOW_HEIGHT / 2)
        
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)
                
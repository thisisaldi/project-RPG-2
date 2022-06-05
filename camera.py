import pygame
from config import *
from terrain import Terrain

class Camera(pygame.sprite.Group):
    def __init__(self, enemies):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.enemies = enemies
        self.gradient = pygame.image.load('assets/gradient.png').convert_alpha()
        self.gradient = pygame.transform.scale(self.gradient, WINDOW_SIZE)
           
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - (WINDOW_WIDTH / 2)
        self.offset.y = player.rect.centery - (WINDOW_HEIGHT / 2)
        for sprite in self.sprites():
            if sprite.alive:
                offset_pos = sprite.rect.topleft - self.offset
                self.display.blit(sprite.image, offset_pos)
            
            if sprite in self.enemies:
                sprite.hp1.topleft = sprite.hp1.topleft - self.offset
                sprite.hp2.topleft = sprite.hp2.topleft - self.offset
                pygame.draw.rect(self.display, 'red', sprite.hp1, 5)
                pygame.draw.rect(self.display, 'white', sprite.hp2, 5)
                
        self.display.blit(self.gradient, (0, 0))
                
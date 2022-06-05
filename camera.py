import pygame
from config import *
from terrain import Terrain
from player import Player

class Camera(pygame.sprite.Group):
    def __init__(self, enemies):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.enemies = enemies
        self.vignette = pygame.image.load('assets/vignette.png').convert_alpha()
        self.vignette = pygame.transform.scale(self.vignette, WINDOW_SIZE)
        self.lighting = pygame.image.load('assets/lighting.png').convert_alpha()
        self.lighting = pygame.transform.scale(self.lighting, WINDOW_SIZE)
           
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - (WINDOW_WIDTH / 2)
        self.offset.y = player.rect.centery - (WINDOW_HEIGHT / 2)
        for sprite in self.sprites():
            if sprite.alive:
                if isinstance(sprite, Player):
                    rect = sprite.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                    offset_pos = rect.topleft - self.offset
                else:
                    offset_pos = sprite.rect.topleft - self.offset
                self.display.blit(sprite.image, offset_pos)
                temp = sprite.rect
                temp.topleft = temp.topleft - self.offset
                # pygame.draw.rect(self.display, 'white', temp, 2)

            if sprite in self.enemies:
                sprite.hp1.topleft = sprite.hp1.topleft - self.offset
                sprite.hp2.topleft = sprite.hp2.topleft - self.offset
                pygame.draw.rect(self.display, 'red', sprite.hp1, 5)
                # pygame.draw.rect(self.display, 'white', sprite.hp2, 5)
                
        self.display.blit(self.vignette, (0, 0))
        self.display.blit(self.lighting, (0, 0))
                
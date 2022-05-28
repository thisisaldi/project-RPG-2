import pygame
from config import *
from terrain import Terrain

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        
        self.rect = pygame.Rect(CAMERA_MARGIN_LEFT, CAMERA_MARGIN_TOP, WINDOW_WIDTH - (CAMERA_MARGIN_LEFT * 2), WINDOW_HEIGHT - (CAMERA_MARGIN_TOP * 2))


    def custom_draw(self, player):
        
        print(player.rect)
        
        if player.rect.left < self.rect.left:
            self.rect.left = player.rect.left
        if player.rect.right > self.rect.right:
            self.rect.right = player.rect.right
        if player.rect.top < self.rect.top:
            self.rect.top = player.rect.top
        if player.rect.bottom > self.rect.bottom:
            self.rect.bottom = player.rect.bottom

        self.offset = pygame.math.Vector2(
            self.rect.left - CAMERA_MARGIN_LEFT,
            self.rect.top - CAMERA_MARGIN_TOP
        )
        
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)
                
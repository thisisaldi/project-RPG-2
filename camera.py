import pygame
from config import *
from terrain import Terrain

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.offset_player = pygame.math.Vector2()
        
        self.camera_x = [True, True]
        self.camera_y = [True, True]
        
        self.map_offset = [0, 0]

    def init_terrain(self):
        for sprite in self.sprites():
            if isinstance(sprite, Terrain):
                self.terrain = sprite 
        
    def check_map(self):
        self.camera_x = [True, True]
        self.camera_y = [True, True]
        if self.map_offset[0] >= 0:
            self.camera_x[0] = False
        elif self.map_offset[0] + self.terrain.rect.width <= WINDOW_WIDTH:
            self.camera_x[1] = False
        if self.map_offset[1] >= 0:
            self.camera_y[0] = False
        elif self.map_offset[1] + self.terrain.rect.height <= WINDOW_HEIGHT:
            self.camera_y[1] = False

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - (WINDOW_WIDTH / 2)
        self.offset.y = player.rect.centery - (WINDOW_HEIGHT / 2)
        
        for sprite in self.sprites():
            offset_pos_x = sprite.rect.left - self.offset.x
            offset_pos_y = sprite.rect.top - self.offset.y
            # self.check_map()
            # if isinstance(sprite, Terrain):
            #     self.map_offset = [offset_pos_x, offset_pos_y]
            #     if not self.camera_x[0]:
            #         offset_pos_x = 0
            #     elif not self.camera_x[1]:
            #         offset_pos_x = WINDOW_WIDTH - self.terrain.rect.width
            #     if not self.camera_y[0]:
            #         offset_pos_y = 0
            #     elif not self.camera_y[1]:
            #         offset_pos_y = WINDOW_HEIGHT - self.terrain.rect.height
            # else:
            #     print(self.camera_x)
            #     print(self.camera_y)
            #     print('player: ', end=' ')
                
            #     if not self.camera_x[0] or not self.camera_x[1]:
            #         offset_pos_x = sprite.rect.centerx - self.offset.x + sprite.rect.left
            #     if not self.camera_y[0] or not self.camera_y[1]:
            #         offset_pos_y = sprite.rect.centery - self.offset.y + sprite.rect.top
                    
                    
            self.display.blit(sprite.image, (offset_pos_x, offset_pos_y))
                
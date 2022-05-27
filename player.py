import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/player_idle1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.rect = self.image.get_rect()
        
        self.direction = pygame.math.Vector2()
        
    def input(self):
        self.direction.x = 0
        self.direction.y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        if keys[pygame.K_a]:
            self.direction.x = -1
        if keys[pygame.K_s]:
            self.direction.y = 1
        if keys[pygame.K_d]:
            self.direction.x = 1
        
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * PLAYER_SPEED
        self.rect.y += self.direction.y * PLAYER_SPEED
            
    def update(self):
        self.input()
        self.move()
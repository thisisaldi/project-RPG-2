import pygame
from config import *
from creature import Creature

class Enemy(Creature):
    def __init__(self, group, player):
        super().__init__(group)
        self.image = pygame.image.load('assets/player_idle1.png').convert_alpha() # png belom diganti
        self.image = pygame.transform.scale(self.image, ENEMY_SIZE)
        self.rect = self.image.get_rect()
        self.direction = pygame.math.Vector2()
        self.player = player
        
    def move(self):
        pass

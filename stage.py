import pygame
from config import *
from player import Player
from camera import Camera
from terrain import Terrain
from enemy import Goblin

class Stage:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.create_stage()
    
    def create_stage(self):
        self.visible = Camera()
        self.enemies = pygame.sprite.Group()
        self.terrain = Terrain([self.visible])
        self.player = Player([self.visible], self.enemies)
        self.enemy1 = Goblin([self.visible, self.enemies], self.player, self.enemies, (100, 100))
        self.enemy2 = Goblin([self.visible, self.enemies], self.player, self.enemies, (200, 200))
        self.enemy3 = Goblin([self.visible, self.enemies], self.player, self.enemies, (300, 300))
        self.enemy4 = Goblin([self.visible, self.enemies], self.player, self.enemies, (600, 700))

    def run(self):
        
        self.visible.custom_draw(self.player)

        self.visible.update()
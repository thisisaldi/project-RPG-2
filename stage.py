import pygame
from config import *
from player import Player
from camera import Camera
from terrain import Terrain
from enemy import Goblin

class Stage:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.visible = Camera()
        self.terrain = Terrain([self.visible])
        self.player = Player([self.visible])
        self.enemy = Goblin([self.visible], self.player)
        
    def run(self):
        
        self.visible.custom_draw(self.player)

        self.visible.update()
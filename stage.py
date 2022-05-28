import pygame
from config import *
from player import Player
from camera import Camera
from terrain import Terrain

class Stage:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.visible = Camera()
        self.terrain = Terrain([self.visible])
        self.player = Player([self.visible])
        
    def run(self):
        # self.visible.draw(self.display)
        self.visible.custom_draw(self.player)
        self.visible.update()
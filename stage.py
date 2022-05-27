import pygame
from config import *
from player import Player

class Stage:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.visible = pygame.sprite.Group()
        self.player = Player([self.visible])
        
    def run(self):
        self.visible.draw(self.display)
        self.visible.update()
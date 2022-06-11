import pygame, random
import soundfx as sfx
from config import *
from player import Player
from camera import Camera
from terrain import Terrain
from enemy import *

class Stage:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.create_stage()
    
    def create_stage(self):
        # self.visible = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.visible = Camera(self.enemies)
        self.terrain = Terrain([self.visible])
        self.player = Player([self.visible], self.enemies)
        sfx.ambience_sound()
        self.enemy1 = Goblin([self.visible, self.enemies], self.player, self.enemies, (random.randint(-100, 100), random.randint(-100, 100)))
        self.enemy2 = MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (random.randint(-50, 50), random.randint(-50, 50)))
        self.enemy3 = Boss([self.visible, self.enemies], self.player, self.enemies, (random.randint(-150, 150), random.randint(-150, 150)))
        

    def run(self, interval, now):
        
        self.visible.custom_draw(self.player)
        # self.visible.draw(self.display)

        self.visible.update()

        if interval - now >= 5000:
            Goblin([self.visible, self.enemies], self.player, self.enemies, (random.randint(-200, 200), random.randint(-200, 200)))
            MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (random.randint(-200, 200), random.randint(-200, 200)))

            return interval

        return now
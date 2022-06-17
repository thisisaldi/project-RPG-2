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
        self.font = pygame.font.SysFont('consolas', 30)
        self.wave = 1
        self.enemies = pygame.sprite.Group()
        self.enemies.count = 1
        self.create_stage()
    
    def create_stage(self):
        # self.visible = pygame.sprite.Group()
        self.visible = Camera(self.enemies)
        self.terrain = Terrain([self.visible])
        self.player = Player([self.visible], self.enemies)
        
    def run(self, interval, now):
        
        self.visible.custom_draw(self.player)
        # self.visible.draw(self.display)

        self.visible.update()

        if self.wave == 1 and self.enemies.count != 0:
            sfx.ambience_sound()
            Goblin([self.visible, self.enemies], self.player, self.enemies, (-1200, 350))
            Goblin([self.visible, self.enemies], self.player, self.enemies, (2300, 300))
            Goblin([self.visible, self.enemies], self.player, self.enemies, (600, -1300))
            Goblin([self.visible, self.enemies], self.player, self.enemies, (600, 1800))
            Goblin([self.visible, self.enemies], self.player, self.enemies, (500, 1800))
            while self.enemies.count != 0:
                if self.enemies.count == 0:
                    self.wave += 1
        


        # if interval - now >= 5000:
        #     Goblin([self.visible, self.enemies], self.player, self.enemies, (random.randint(-200, 200), random.randint(-200, 200)))
        #     MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (random.randint(-200, 200), random.randint(-200, 200)))
        #     return interval
        return now
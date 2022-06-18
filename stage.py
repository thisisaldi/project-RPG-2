import pygame
import soundfx as sfx
from config import *
from player import Player
from camera import Camera
from terrain import Terrain
from enemy import *

class Stage:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.wave = 1
        self.enemies = pygame.sprite.Group()
        self.font = pygame.font.SysFont('consolas', 30)
        self.create_stage()
        self.started = True
        self.game_over = False
        self.reset = False
        Goblin.enemies_count = 0
        MaskedOrc.enemies_count = 0
        Boss.enemies_count = 0

    def __del__(self):
        self.visible.empty()
        self.enemies.empty()

    def create_stage(self):
        # self.visible = pygame.sprite.Group()
        self.visible = Camera(self.enemies)
        self.terrain = Terrain([self.visible])
        self.player = Player([self.visible], self.enemies)

    def reset_stage(self):
        if (Goblin.enemies_count != 0 or MaskedOrc.enemies_count != 0 or Boss.enemies_count != 0) and self.player.hp <= 0:
            self.reset = True

        
    def run(self, interval, now):
        
        self.visible.custom_draw(self.player)
        # self.visible.draw(self.display)

        self.visible.update()

        if self.wave == 1 and self.started:
            self.started = False
            sfx.ambience_sound()
            Goblin([self.visible, self.enemies], self.player, self.enemies, (-1200, 350))
            Goblin([self.visible, self.enemies], self.player, self.enemies, (2300, 300))
            Goblin([self.visible, self.enemies], self.player, self.enemies, (600, -1300))
            Goblin([self.visible, self.enemies], self.player, self.enemies, (600, 1800))
            Goblin([self.visible, self.enemies], self.player, self.enemies, (500, 1800))
        elif self.wave == 2 and self.started:
            self.started = False
            sfx.ambience_sound()
            MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (-1200, 350))
            MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (2300, 300))
            MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (600, -1300))
            MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (600, 1800))
            MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (500, 1800))
        elif self.wave == 3 and self.started:
            self.started = False
            Boss([self.visible, self.enemies], self.player, self.enemies, (550, 1800))
        
        print(Goblin.enemies_count, MaskedOrc.enemies_count, Boss.enemies_count)


        # print(Goblin.enemies_count)
        if self.wave == 3 and Goblin.enemies_count == 0 and MaskedOrc.enemies_count == 0 and Boss.enemies_count == 0:
            self.game_over = True
        if Goblin.enemies_count == 0 and MaskedOrc.enemies_count == 0 and Boss.enemies_count == 0:
            self.wave += 1
            self.started = True

        self.reset_stage()
        
        # if interval - now >= 5000:
        #     Goblin([self.visible, self.enemies], self.player, self.enemies, (random.randint(-200, 200), random.randint(-200, 200)))
        #     MaskedOrc([self.visible, self.enemies], self.player, self.enemies, (random.randint(-200, 200), random.randint(-200, 200)))
        #     return interval
        return now
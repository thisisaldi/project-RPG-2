import pygame
from config import *
from creature import Creature

class Enemy(Creature):
    def __init__(self, group, player):
        super().__init__(group)
        self.player = player
        
    def move(self):
        pass

class Goblin(Enemy):
    def __init__(self, group, player):
        super().__init__(group, player)
    

        self.image_idle_right = []
        self.image_idle_left = []
        self.image_run_right = []
        self.image_run_left = []

        for i in range(0, 4):
            self.image = pygame.image.load(f'assets/0x72_DungeonTilesetII_v1.4/frames/goblin_idle_anim_f{i}.png').convert_alpha() # png belom diganti
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

            self.image_idle_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_idle_left.append(self.image)
        
        self.rect = self.image.get_rect()

        for i in range(0, 4):
            self.image = pygame.image.load(f'assets/0x72_DungeonTilesetII_v1.4/frames/goblin_run_anim_f{i}.png').convert_alpha() # png belom diganti
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

            self.image_run_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_run_left.append(self.image)
        
        self.rect = self.image.get_rect()

        self.rect.x = WINDOW_WIDTH / 2.2
        self.rect.y = WINDOW_HEIGHT / 2.2
        self.right = True
        self.running = False
        self.index = 0
        self.anim_delay = 0
    
    def animation(self):
        if self.index >= len(self.image_idle_right):
            self.index = 0
        if self.right:
            self.image = self.image_idle_right[self.index]
        else:
            self.image = self.image_idle_left[self.index]
        self.anim_delay += 1
        if self.anim_delay >= ENEMY_IDLE_DELAY:
            self.index += 1
            self.anim_delay = 0

    def update(self):
        self.animation()
        self.move()
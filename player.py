import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image_idle_right = []
        self.image_idle_left = []
        self.image_run_right = []
        self.image_run_left = []
        
        for i in range(1, 10):
            self.image = pygame.image.load(f'assets/player_idle{i}.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
            
            self.image_idle_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_idle_left.append(self.image)
            self.rect = self.image.get_rect()
        
        for i in range(1, 10):
            self.image = pygame.image.load(f'assets/player_run{i}.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
            
            self.image_run_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_run_left.append(self.image)
            self.rect = self.image.get_rect()
        
        self.direction = pygame.math.Vector2()
        self.rect.x = WINDOW_WIDTH / 2
        self.rect.y = WINDOW_HEIGHT / 2
        self.right = True
        self.idle = True
        
        self.index = 0
        self.anim_delay = 0
        
        # Stats
        
        self.level = 1
        self.base_damage = PLAYER_BASE_DAMAGE + (PLAYER_GROWTH_DAMAGE * (self.level - 1))
        self.hp = PLAYER_BASE_HP + (PLAYER_GROWTH_HP * (self.level - 1))
        self.mana = PLAYER_BASE_MANA + (PLAYER_GROWTH_MANA * (self.level - 1))
        
    def input(self):
        self.direction.x = 0
        self.direction.y = 0
        self.idle = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.idle = False
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.right = False
            self.idle = False
        if keys[pygame.K_s]:
            self.direction.y = 1
            self.idle = False
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.right = True
            self.idle = False
        
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * PLAYER_SPEED
        self.rect.y += self.direction.y * PLAYER_SPEED
        
    def animation(self):
        if self.idle:
            if self.index >= len(self.image_idle_right):
                self.index = 0
            if self.right:
                self.image = self.image_idle_right[self.index]
            else:
                self.image = self.image_idle_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= PLAYER_IDLE_DELAY:
                self.index += 1
                self.anim_delay = 0
                
        else:
            if self.index >=  len(self.image_run_right):
                self.index = 0
            if self.right:
                self.image = self.image_run_right[self.index]
            else:
                self.image = self.image_run_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= PLAYER_RUN_DELAY:
                self.index += 1
                self.anim_delay = 0
            
    def update(self):
        self.input()
        self.animation()
        self.move()
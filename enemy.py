import pygame
import math
import json
from config import *
from creature import Creature

class Enemy(Creature):
    def __init__(self, group, player, enemies):
        super().__init__(group)
        self.display = pygame.display.get_surface()
        self.player = player
        self.enemies = enemies
        self.distance = pygame.math.Vector2()
        with open('enemy_stats.json', 'r') as enemy_stats:
            self.stats = json.load(enemy_stats)
            
        self.attacking = False
        self.attacked = False
        


    def config_stats(self, name):
        self.name = name
        self.max_hp = self.stats[self.name]['HP']
        self.hp = self.max_hp
        self.damage = self.stats[self.name]['Damage']
        self.level = self.stats[self.name]['Level']
        self.range = self.stats[self.name]['Range']
        self.type = self.stats[self.name]['Type']
        
    def collision(self, dir):
        for enemy in self.enemies:
            if self.rect.colliderect(enemy.rect) and enemy is not self:
                if dir == 'x':
                    if self.direction.x > 0:
                        self.rect.right = enemy.rect.left
                    elif self.direction.x < 0:
                        self.rect.left = enemy.rect.right
                elif dir == 'y':
                    if self.direction.y > 0:
                        self.rect.bottom = enemy.rect.top
                    elif self.direction.y < 0:
                        self.rect.top = enemy.rect.bottom
                self.idle = True

    def check_distance(self, range):
        self.distance = math.sqrt((self.direction.x)**2 + (self.direction.y)**2)
        return (self.distance < range and self.distance >= 60)
                        
    def move(self):

        self.direction.x = self.player.rect.x - self.rect.x
        self.direction.y = self.player.rect.y - self.rect.y
        
        if self.check_distance(self.range) and not self.attacking:
            if self.direction.magnitude() != 0:
                self.direction.normalize()
                self.direction.scale_to_length(self.speed)
            self.attacking = False
            self.idle = False
            self.rect.x += self.direction.x
            self.collision('x')
            self.rect.y += self.direction.y
            self.collision('y')

        elif self.distance < 60 and not self.attacking:
            self.attacking = True
            self.damaged = False
            self.idle = False
            self.direction.x = 0
            self.direction.y = 0

        elif not self.attacking:
            self.idle = True
            self.attacking = False
            self.direction.x = 0
            self.direction.y = 0
        
        if self.direction.x > 0:
            self.right = True
        elif self.direction.x < 0:
            self.right = False
            
    def hp_bar(self):
        red = (self.rect.width * self.hp) // self.max_hp
        white = self.rect.width - red
        self.hp1 = pygame.rect.Rect(self.rect.left, self.rect.top - (6 * SCALE * ZOOM), red, 1)
        self.hp2 = pygame.rect.Rect(self.rect.left + red, self.rect.top - (6 * SCALE * ZOOM), white, 1)
        # pygame.draw.rect(self.display, 'red', hp1, 6)
        # pygame.draw.rect(self.display, 'white', hp2, 6)

class Goblin(Enemy):
    def __init__(self, group, player, enemies, pos):
        super().__init__(group, player, enemies)
        self.config_stats('Goblin')
        self.image_idle_right = []
        self.image_idle_left = []
        self.image_run_right = []
        self.image_run_left = []
        self.image_attacking_right = []
        self.image_attacking_left = []

        for i in range(0, 4):
            self.image = pygame.image.load(f'assets/enemies/goblin_idle_anim_f{i}.png').convert_alpha() # png belom diganti
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

            self.image_idle_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_idle_left.append(self.image)
        
        self.rect = self.image.get_rect()

        for i in range(0, 4):
            self.image = pygame.image.load(f'assets/enemies/goblin_run_anim_f{i}.png').convert_alpha() # png belom diganti
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

            self.image_run_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_run_left.append(self.image)
        
        self.rect = self.image.get_rect()

        for i in range(1, 9):
            self.image = pygame.image.load(f'assets/enemies/goblin_attack_anim_f{i}.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

            self.image_attacking_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_attacking_left.append(self.image)
        
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.index = 0
        self.anim_delay = 0
        self.speed = ENEMY_SPEED
        self.idle = False
        self.right = True
    
        self.hp_bar()
    
    def animation(self):
        if not self.idle and not self.attacking:
            if self.index >= len(self.image_run_right):
                self.index = 0
            if self.right:
                self.image = self.image_run_right[self.index]
            else:
                self.image = self.image_run_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= ENEMY_DELAY:
                self.index += 1
                self.anim_delay = 0

        elif self.idle:
            if self.index >= len(self.image_idle_right):
                self.index = 0
            if self.right:
                self.image = self.image_idle_right[self.index]
            else:
                self.image = self.image_idle_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= ENEMY_DELAY:
                self.index += 1
                self.anim_delay = 0
        
        elif self.attacking:
            if self.index >= 5:
                if self.rect.colliderect(self.player.rect) and not self.damaged:
                    self.player.hp -= self.damage
                    self.damaged = True
            if self.index >= len(self.image_attacking_right):
                self.index = 0
                self.attacking = False
            if self.right:
                self.image = self.image_attacking_right[self.index]
            else:
                self.image = self.image_attacking_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= ENEMY_ATTACKING_DELAY:
                self.index += 1
                self.anim_delay = 0



    def update(self):
        if self.hp <= 0:
            self.alive = False
            self.kill()
        if self.alive:
            self.hp_bar()
            self.animation()
            self.move()
            # pygame.draw.rect(self.display, 'white', self.rect, 2)

class MaskedOrc(Enemy):
    def __init__(self, group, player, enemies, pos):
        super().__init__(group, player, enemies)
        self.config_stats('Masked Orc')
        self.image_idle_right = []
        self.image_idle_left = []
        self.image_run_right = []
        self.image_run_left = []
        self.image_attacking_right = []
        self.image_attacking_left = []

        for i in range(0, 4):
            self.image = pygame.image.load(f'assets/enemies/masked_orc_idle_anim_f{i}.png').convert_alpha() # png belom diganti
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

            self.image_idle_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_idle_left.append(self.image)
        
        self.rect = self.image.get_rect()

        for i in range(0, 4):
            self.image = pygame.image.load(f'assets/enemies/masked_orc_run_anim_f{i}.png').convert_alpha() # png belom diganti
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

            self.image_run_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_run_left.append(self.image)
        
        self.rect = self.image.get_rect()

        for i in range(0, 4):
            self.image = pygame.image.load(f'assets/enemies/masked_orc_idle_anim_f{i}.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

            self.image_attacking_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_attacking_left.append(self.image)
        
        # self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.index = 0
        self.anim_delay = 0
        self.speed = ENEMY_SPEED
        self.idle = False
        self.right = True
        
        self.hp_bar()
    
    def animation(self):
        if not self.idle and not self.attacking:
            if self.index >= len(self.image_run_right):
                self.index = 0
            if self.right:
                self.image = self.image_run_right[self.index]
            else:
                self.image = self.image_run_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= ENEMY_DELAY:
                self.index += 1
                self.anim_delay = 0

        elif self.idle:
            if self.index >= len(self.image_idle_right):
                self.index = 0
            if self.right:
                self.image = self.image_idle_right[self.index]
            else:
                self.image = self.image_idle_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= ENEMY_DELAY:
                self.index += 1
                self.anim_delay = 0
        
        elif self.attacking:
            if self.index >= 5:
                if self.rect.colliderect(self.player.rect) and not self.damaged:
                    self.player.hp -= self.damage
                    self.damaged = True
            if self.index >= len(self.image_attacking_right):
                self.index = 0
                self.attacking = False
            if self.right:
                self.image = self.image_attacking_right[self.index]
            else:
                self.image = self.image_attacking_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= ENEMY_ATTACKING_DELAY:
                self.index += 1
                self.anim_delay = 0



    def update(self):
        if self.hp <= 0:
            self.alive = False
            self.kill()
        if self.alive:
            self.hp_bar()
            self.animation()
            self.move()
            # pygame.draw.rect(self.display, 'white', self.rect, 2)
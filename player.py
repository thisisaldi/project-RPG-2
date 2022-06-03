import pygame
from config import *
from creature import Creature

class Player(Creature):
    def __init__(self, group, enemies):
        super().__init__(group)
        self.image_idle_right = []
        self.image_idle_left = []
        self.image_run_right = []
        self.image_run_left = []
        self.image_attack_right = []
        self.image_attack_left = []
        self.display = pygame.display.get_surface()
        for i in range(1, 10):
            self.image = pygame.image.load(f'assets/player/player_idle{i}.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
            
            self.image_idle_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_idle_left.append(self.image)
            self.rect = self.image.get_rect()
        
        for i in range(1, 10):
            self.image = pygame.image.load(f'assets/player/player_run{i}.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
            
            self.image_run_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_run_left.append(self.image)
            self.rect = self.image.get_rect()
        
        for i in range(1, 11):
            self.image = pygame.image.load(f'assets/player/player_attack{i}.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
            
            self.image_attack_right.append(self.image)
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_attack_left.append(self.image)
            self.rect = self.image.get_rect()
        
        self.enemies = enemies
        
        self.rect.x = WINDOW_WIDTH / 2
        self.rect.y = WINDOW_HEIGHT / 2
        self.right = True
        self.running = False
        self.attacking = False
        self.dashing = False
        self.damaged = False
        self.attack_speed = 3

        self.dash_cooldown = 0
        
        self.index = 0
        self.anim_delay = 0
        
        self.level = 1
        self.base_damage = PLAYER_BASE_DAMAGE + (PLAYER_GROWTH_DAMAGE * (self.level - 1))
        self.hp = PLAYER_BASE_HP + (PLAYER_GROWTH_HP * (self.level - 1))
        self.mana = PLAYER_BASE_MANA + (PLAYER_GROWTH_MANA * (self.level - 1))

        
    def input(self):
        self.direction.x = 0
        self.direction.y = 0
        self.running = True
        self.dashing = False
        keys = pygame.key.get_pressed()
        if not self.attacking and not self.dashing:
            if keys[pygame.K_w]:
                self.direction.y = -1
            if keys[pygame.K_a]:
                if self.direction.x == 1:
                    self.direction.x = 0
                else:
                    self.direction.x = -1
            if keys[pygame.K_s]:
                if self.direction.y == -1:
                    self.direction.y = 0
                else:
                    self.direction.y = 1
            if keys[pygame.K_d]:
                if self.direction.x == -1:
                    self.direction.x = 0
                else:
                    self.direction.x = 1
        if not self.attacking:
            if keys[pygame.K_SPACE] and self.dash_cooldown <= 0:
                self.dashing = True
                self.dash_cooldown = PLAYER_DASH_CD
        if keys[pygame.K_j]:
            if not self.attacking:
                self.attacking = True
                self.index = 0
                
        if self.attacking and self.index >= len(self.image_attack_right):
            self.attacking = False
                       
        if self.direction.x == 0 and self.direction.y == 0:
            self.running = False
        else:
            self.running = True
            
        if self.direction.x == 1:
            self.right = True
        elif self.direction.x == -1:
            self.right = False
    
    def attack(self):
        if self.attacking and self.index >= 5:
            if self.right:
                self.hitbox = pygame.rect.Rect(self.rect.centerx, self.rect.top, PLAYER_ATTACK_RANGE + (self.rect.width / 2), self.rect.height)
            else:
                self.hitbox = pygame.rect.Rect(self.rect.centerx - PLAYER_ATTACK_RANGE - (self.rect.width / 2), self.rect.top, PLAYER_ATTACK_RANGE + (self.rect.width / 2), self.rect.height)
            # pygame.draw.rect(self.display, 'white', self.hitbox, 2)
            for enemy in self.enemies:
                if self.hitbox.colliderect(enemy.rect):
                    enemy.hp -= self.base_damage
     
    def animation(self):
        if self.running:
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
                
        elif self.attacking:
            if self.index >=  len(self.image_attack_right):
                self.index = 0
            if self.right:
                self.image = self.image_attack_right[self.index]
            else:
                self.image = self.image_attack_left[self.index]
            self.anim_delay += 1
            if self.anim_delay >= self.attack_speed:
                self.index += 1
                self.anim_delay = 0
                
        else:
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
            
    def update(self):
        self.attack()
        self.input()
        self.animation()
        if self.dashing:
            self.move(PLAYER_DASH)
        else:
            self.move(PLAYER_SPEED)
        self.dash_cooldown -= 1
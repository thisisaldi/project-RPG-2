import pygame, random
from config import *

pygame.mixer.init()

def player_attack_sound():
    sound = pygame.mixer.Sound(f"soundfx/player/swing{random.randint(1, 3)}.wav")
    sound.play()

def player_dash_sound():
    pass

def player_dash_voice():
    sound = pygame.mixer.Sound("soundfx/player/dash.wav")
    sound.play()

def enemy_hit_sound():
    sound = pygame.mixer.Sound("soundfx/enemy/masked_orc/enemy_hit.wav")
    sound.play()
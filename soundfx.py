import pygame, random
from config import *

pygame.mixer.init()

def ambience_sound():
    pygame.mixer.music.load("soundfx/ambient/ambience_sound.mp3")
    pygame.mixer.music.set_volume(0.5 * VOLUME_LEVEL)
    pygame.mixer.music.play(-1)

def player_footsteps_sound():
    sound = pygame.mixer.Sound(f"soundfx/player/footstep.ogg")
    sound.set_volume(0.5 * VOLUME_LEVEL)
    sound.play()

def player_attack_sound():
    sound = pygame.mixer.Sound(f"soundfx/player/swing{random.randint(1, 3)}.wav")
    sound.set_volume(1 * VOLUME_LEVEL)
    sound.play()

def player_dash_sound():
    sound = pygame.mixer.Sound(f"soundfx/player/dash.wav")
    sound.set_volume(1 * VOLUME_LEVEL)
    sound.play()

def masked_orc_attack_sound():
    sound = pygame.mixer.Sound(f"soundfx/enemy/masked_orc/masked_orc_attack{random.randint(1, 4)}.wav")
    sound.set_volume(0.8 * VOLUME_LEVEL)
    sound.play()

def masked_orc_death_sound():
    sound = pygame.mixer.Sound(f"soundfx/enemy/masked_orc/masked_orc_death.wav")
    sound.set_volume(0.8 * VOLUME_LEVEL)
    sound.play()

def enemy_hit_sound():
    sound = pygame.mixer.Sound(f"soundfx/enemy/enemy_hit{random.randint(1, 3)}.flac")
    sound.set_volume(1 * VOLUME_LEVEL)
    sound.play()
from game import Game

"""
    TO-DO (MAIN):
    - Survival/Wave (3 Waves) (Done)
    - Enemy Spawn (Wave 1 : 5 Goblin, Wave 2 : 5 Masked Orc, Wave 3 : Boss) (Done)
    - 1 Stage Kotak (Done)
    - Pake pedang doang (Done)
    - Health Drop
    - Level Up
    - Game Over
    - GUI HP, Level, Stats
    - Convert Exe

    TO-DO (Side):
    - Story
    - Combat Development:
        - Player and Enemy HP
        - Player attack and skill system
        - Other fixes
    - Enemy SFX
    - Map Optimization (Obstacle and others)
    - Lighting
    - Enemy animations
    - Main Menu
"""

if __name__ == '__main__':
    game = Game()
    game.run()
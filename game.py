import pygame, sys
from config import *
from stage import Stage

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Project: RPG')
        self.display = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.stages = Stage()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.display.fill('black')
            self.stages.run()
            pygame.display.update()
            self.clock.tick(DEFAULT_FPS)
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
        self.font = pygame.font.SysFont('consolas', 30)
        self.time = pygame.time.get_ticks()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.display.fill('black')

            if self.stages.reset:
                del self.stages
                self.stages = Stage()

            if not self.stages.game_over:
                self.time = self.stages.run(pygame.time.get_ticks(), self.time)
            
                self.fps = self.font.render('{:.2f}'.format(self.clock.get_fps()), True, 'white')
                self.display.blit(self.fps, (50, 50))
                
                self.wave_text = self.font.render(f'WAVE : {self.stages.wave}/3', True, 'white')
                self.display.blit(self.wave_text, (500, 100))

                self.player_hp = self.font.render(f'HP : {self.stages.player.hp}', True, 'white')
                self.display.blit(self.player_hp, (50, 100))
        
            elif self.stages.game_over:
                self.gameover_text = self.font.render(f'GAMEOVER!!!', True, 'white')
                self.gameover_text_rect = self.gameover_text.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                self.display.blit(self.gameover_text, self.gameover_text_rect)



            # self.enemy_hp = self.font.render(f'HP : {self.stages.enemy1.hp}', True, 'white')
            # self.display.blit(self.enemy_hp, (50, 150))
            
            # print(self.clock.get_fps())
            pygame.display.update()
            self.clock.tick(DEFAULT_FPS)
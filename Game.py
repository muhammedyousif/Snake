import pygame
import sys
import random

class Game:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            clock.tick(60)

import pygame
import sys
import random



class Game:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        screen = pygame.display.set_mode((width,height))
        clock =pygame.time.Clock()
        surface1 =self.surface(width,height)
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.blit(surface1,(200,250))
            pygame.display.update()
            clock.tick(60)

    def surface(self,w,h)->pygame.surface:
        testsurface = pygame.Surface((w,h))
        return testsurface


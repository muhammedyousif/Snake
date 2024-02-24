import pygame
import sys
import random
from Food import Food
from Snake import Snake


class Game:
    def __init__(self,cell_size,cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
        clock =pygame.time.Clock()
        pygame.init()
        food=Food(cell_number)
        snake = Snake()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill(pygame.Color('dark green '))
            snake.draw_snake(cell_size,screen)
            food.draw_fruit(cell_size,screen)
            pygame.display.update()
            clock.tick(60)

    def surface(self,w,h)->pygame.surface:
        testsurface = pygame.Surface((w,h))
        return testsurface


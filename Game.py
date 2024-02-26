import pygame
import sys
import random

from pygame import Vector2

from Food import Food
from Snake import Snake


class Game:
    def __init__(self,cell_size,cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
        clock =pygame.time.Clock()
        pygame.init()
        self.food=Food(cell_number)
        self.snake = Snake()

        SCREEN_UPDATE=pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE,150)

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==SCREEN_UPDATE:
                    self.update()
                if event.type==pygame.KEYDOWN:
                    self.check_key(event)
            screen.fill(pygame.Color('dark green '))
            self.draw_elements(screen)
            pygame.display.update()
            clock.tick(60)

    def update(self):
        self.snake.move_snake()
        self.did_eat()
        self.check_fail()

    def draw_elements(self,screen):
        self.snake.draw_snake(self.cell_size, screen)
        self.food.draw_fruit(self.cell_size, screen)

    def surface(self,w,h)->pygame.surface:
        testsurface = pygame.Surface((w,h))
        return testsurface
    def check_key(self,event):
        if event.key==pygame.K_UP:
            if self.snake.direction.y!=1:
                self.snake.direction=Vector2(0,-1)
        if event.key==pygame.K_DOWN:
            if self.snake.direction.y!=-1:
                self.snake.direction=Vector2(0,1)
        if event.key==pygame.K_RIGHT:
            if self.snake.direction.x!=-1:
                self.snake.direction=Vector2(1,0)
        if event.key==pygame.K_LEFT:
            if self.snake.direction.x!=1:
                self.snake.direction=Vector2(-1,0)
    def did_eat(self):
        if self.food.pos==self.snake.body[0]:
            self.food_eaten()
            self.snake.add_block()


    def food_eaten(self):
        self.food=Food(self.cell_number)

    def check_fail(self):
        if not 0<=self.snake.body[0].x <self.cell_number or not 0<=self.snake.body[0].y <self.cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block==self.snake.body[ 0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()


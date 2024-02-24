import pygame,random
from pygame.math import Vector2

class Food:
    def __init__(self,cell_number):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x,self.y)
    def draw_fruit(self,cell_size,screen):
        fruit_rect=pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
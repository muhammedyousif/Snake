import pygame
from pygame.math import Vector2
class Snake:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(6,10),Vector2(7,10)]
    def draw_snake(self,cell_size,screen):
        for block in self.body:
            block_rect=pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(183,191,122),block_rect)
import pygame
from pygame.math import Vector2
class Snake:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.newblock=False
    def draw_snake(self,cell_size,screen):
        for block in self.body:
            block_rect=pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(183,191,122),block_rect)
    def move_snake(self):
        if self.newblock==True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.newblock=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[: ]
    def add_block(self):
        self.newblock=True
    def set_newblock(self,abool):
        self.newblock=abool
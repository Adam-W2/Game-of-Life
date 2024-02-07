import pygame
import numpy as np
import random
from Cell import Cell

darkBlue = (0,0,128)
white = (255,255,255)

class Grid:
    def __init__(self, width, height, scale, offset):
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.scale = scale
        self.grid_array = np.empty((self.rows, self.columns))
        self.prob = 0.3
        self.offset = offset
        self.rects = []

    def create_grid(self):
        for x in range(self.rows):
            for y in range(self.columns):
                r = random.random()
                if r <= self.prob:
                    self.grid_array[x][y] = 1
                else:
                    self.grid_array[x][y] = 0

    def get_grid(self):
        return self.grid_array

    def conways_game(self, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos = x * self.scale
                y_pos = y * self.scale

                if self.grid_array[x][y] == 1:
                    rect = pygame.draw.rect(surface, darkBlue, (x_pos, y_pos,self.scale - self.offset, self.scale - self.offset), 0)
                    self.rects.append(rect)
                else:
                    rect = pygame.draw.rect(surface, white, (x_pos, y_pos, self.scale - self.offset, self.scale - self.offset), 0)
                    self.rects.append(rect)
        next = np.empty((self.rows, self.columns))

        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x,y)

                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next

    def get_neighbours(self, x, y):
        temp = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                temp += self.grid_array[x_edge][y_edge]
        temp -= self.grid_array[x][y]
        return temp

    def resurrect(self, pos):
        x_pos = pos[0] / self.scale
        y_pos = pos[1] / self.scale
        if self.grid_array[x_pos][y_pos] == 0:
            self.grid_array[x_pos][y_pos] = 1

            #NOT WORKING ATM, FIGURE OUT HOW TO GET COORDS OF CLICK AND TRANSFER THAT INTO THE GRID
            #MAKE LIST OF RECTS THEN ITERATE OVER TO CHECK IF EVENT POS WAS ON PARTICULAR RECTANGLE


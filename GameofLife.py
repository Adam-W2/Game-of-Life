import pygame
import Grid
width, height = 1000, 800
size = (width, height)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 50

black = (0,0,0)
blue = (0,14,71)
white = (255, 255, 255)

scaler = 20
offset = 1

Grid = Grid.Grid(width, height, scaler, offset)
Grid.create_grid()

run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Grid.resurrect(event.pos)

    Grid.conways_game(screen)

    pygame.display.update()
pygame.quit()
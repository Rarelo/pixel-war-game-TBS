import pygame
from sys import exit
import os

BASEDIR = os.getcwd()
GRAPHICS = os.path.join(BASEDIR,"Graphics")

WIDTH = 360
HEIGHT = 202
#make rendering system based on multiples?

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT)) #360 202?
#print(pygame.display.list_modes())
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
    #print(type(pygame.rect))
    pygame.display.update()
    clock.tick(60)
    SCREEN.fill((255,255,255))

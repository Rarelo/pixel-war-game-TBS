import pygame
from sys import exit
import os
import random

#program code import
import hexagon
import camera
import render
import terminal

## TODO:
#raise the window resolution, higher resolutions? Fullscreen?
#add movement functionality to polygons
#add engine functionality nit features (MVP)
#clean up the code


#global vars
WIDTH = 360 #make rendering system based on multiples?
HEIGHT = 202 #848, 480, also remove scaled from mode b/c it breaks vsync
GAMESTATE = True

#first things program needs to work
pygame.init()
clock = pygame.time.Clock()


#display settings
pygame.display.set_caption('pixel war game')
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.SCALED, vsync=1) #360 202?

#create objects
hexagon.Hexagon(0,0,'normal') #creates a single polygon to prevent a render crash

for i in range(50):
    value = random.randint(0,1)
    if value == 0:
        value = 'normal'
    else: value = 'water'
    hexagon.Hexagon(random.randint(-2,2),random.randint(-2,2),value)

hexagon.hexagon_group = render.sort_polygons()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit game
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN: #only checks when a key is hit initally
            if event.key == pygame.K_f: #fullscreen
                pygame.display.toggle_fullscreen()
            if event.key == pygame.K_a: #need to make hold down button work
                camera.camera1.a_pressed = True
            if event.key == pygame.K_d: #need to make hold down button work
                camera.camera1.d_pressed = True
            if event.key == pygame.K_w: #need to make hold down button work
                camera.camera1.w_pressed = True
            if event.key == pygame.K_s: #need to make hold down button work
                camera.camera1.s_pressed = True
            if event.key == pygame.K_BACKQUOTE: #need to make hold down button work
                terminal.user_command_input()
        if event.type == pygame.KEYUP: #for buttons that need to be held down
            if event.key == pygame.K_a:
                camera.camera1.a_pressed = False
            if event.key == pygame.K_d:
                camera.camera1.d_pressed = False
            if event.key == pygame.K_w:
                camera.camera1.w_pressed = False
            if event.key == pygame.K_s:
                camera.camera1.s_pressed = False

    #draw/update screen/objects
    pygame.display.update()
    clock.tick(60)

    if GAMESTATE:
        SCREEN.fill((255,255,255))
        hexagon.hexagon_group.draw(SCREEN)
        hexagon.hexagon_group.update()
        camera.camera1.update()
#if __name__ == "__main__": can make a debug suite with arguments

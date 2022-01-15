import pygame
from sys import exit
import os
import random

#program code import
import constants

import hexagon
import camera
import render
import terminal

## TODO:
#raise the window resolution, higher resolutions? Fullscreen?
#add movement functionality to polygons
#add engine functionality nit features (MVP)
#

#first things program needs to work
pygame.init()
clock = pygame.time.Clock()


#display settings
render.create_game_screen(1920,1200) #if you call this render function again it breaks placing hexagons

#create objects
hexagon.Hexagon(0,0,'normal') #creates a single polygon to prevent a render crash

for i in range(0):
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

    if constants.GAMESTATE:
        render.game_update_screen()
#if __name__ == "__main__": can make a debug suite with arguments

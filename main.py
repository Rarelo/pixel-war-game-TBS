import pygame
from sys import exit
import os
import random

import constants

import hexagon
import unit
import camera
import render
import terminal
#import unit

## TODO:

#focus on making code I'll need to use more than in one instance as clean and modular as possible
#create a prototype, then create a presetable MVP as a proof of concept

#this program doesn't actually delete any of the hexagons from memory, which might be a problem

#### BUGS ####
#camera x,y movemnt does not scale, and scaling down causes the game to become really far away
#strange things happening in the terminal with inputs like hexagon(1,0,normal(


pygame.init()
clock = pygame.time.Clock()


#display settings
render.create_game_screen(1920,1080) #if you call this render function again it breaks placing hexagons
#original size 360,202

hexagon.Hexagon(0,0,'normal')
zunit.Unit(0,0)

render.sort_polygons()

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

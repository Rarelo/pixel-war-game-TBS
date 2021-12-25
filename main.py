import pygame
from sys import exit
import os
import random

#program code import
import main_classes

## TODO:
#fix the broken rendering for the added terminal polygons
#split the classes structure into mutliple files
#raise the window resolution, higher resolutions? Fullscreen?
#add movement functionality to polygons
#add engine functionality nit features (MVP)


#global vars
WIDTH = 360 #make rendering system based on multiples?
HEIGHT = 202 #848, 480, also remove scaled from mode b/c it breaks vsync
GAMESTATE = True

#display settings
pygame.display.set_caption('pixel war game')
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.SCALED, vsync=1) #360 202?

#create objects

main_classes.RenderEngine1.create_polygons(None,None) #need this polygon so hexagon_list exists
TextConsole1 = main_classes.TextConsole() #init console

#for i in range(5):
#    RenderEngine1.create_polygons(main_classes.hexagon_list[i],random.randint(1,6))

main_classes.hexagon_group = main_classes.RenderEngine1.sort_polygons(main_classes.hexagon_list)

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
                main_classes.camera.a_pressed = True
            if event.key == pygame.K_d: #need to make hold down button work
                main_classes.camera.d_pressed = True
            if event.key == pygame.K_w: #need to make hold down button work
                main_classes.camera.w_pressed = True
            if event.key == pygame.K_s: #need to make hold down button work
                main_classes.camera.s_pressed = True
            if event.key == pygame.K_BACKQUOTE: #need to make hold down button work
                TextConsole1.user_command_input()
        if event.type == pygame.KEYUP: #for buttons that need to be held down
            if event.key == pygame.K_a:
                main_classes.camera.a_pressed = False
            if event.key == pygame.K_d:
                main_classes.camera.d_pressed = False
            if event.key == pygame.K_w:
                main_classes.camera.w_pressed = False
            if event.key == pygame.K_s:
                main_classes.camera.s_pressed = False

    #draw/update screen/objects
    pygame.display.update()
    main_classes.clock.tick(60)

    if GAMESTATE:
        SCREEN.fill((255,255,255))
        main_classes.hexagon_group.draw(SCREEN)
        main_classes.hexagon_group.update()
        main_classes.camera.update()

import pygame
from sys import exit
import os

#program code import
import main_classes

## TODO:
#add fps indepdence for camera
#add multiple polygons (placing them)
#add movement functionality to polygons


#global vars
WIDTH = 360 #make rendering system based on multiples?
HEIGHT = 202

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),pygame.SCALED, pygame.OPENGL, vsync=1) #360 202?
clock = pygame.time.Clock()

#creates the camera
camera = main_classes.Camera()

hexagon_group = pygame.sprite.Group()
hexagon_group.add(main_classes.Hexagon(100,100))

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
    clock.tick(60)

    SCREEN.fill((255,255,255))
    hexagon_group.draw(SCREEN)
    hexagon_group.update()
    main_classes.camera.update()

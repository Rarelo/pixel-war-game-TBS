import pygame
from sys import exit
import os

#program code import
import main_classes

## TODO:
#add multiple polygons (placing them)
#add movement functionality to polygons
#add engine functionality nit features (MVP)
#raise pixel sise for better animations


#global vars
WIDTH = 360 #make rendering system based on multiples?
HEIGHT = 202

#display settings
pygame.display.set_caption('pixel war game')
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),pygame.SCALED, pygame.OPENGL, vsync=1) #360 202?

#create objects
hexagon_group = pygame.sprite.Group()

def create_polygons(new_hexagon,realative_hexagon, side):
    '''create new polygons and place them correctly'''
    realative_hexagon.create_neighboring_polygon(side,new_hexagon)
    hexagon_group.add(new_hexagon)

hexagon1 = main_classes.Hexagon(100,100)
hexagon_group.add(hexagon1)

hexagon2 = main_classes.Hexagon(200,200)
create_polygons(hexagon2,hexagon1,6)

hexagon3 = main_classes.Hexagon(200,200)
create_polygons(hexagon3,hexagon1,4)

hexagon4 = main_classes.Hexagon(200,200)
create_polygons(hexagon4,hexagon2,4)

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
    main_classes.clock.tick(60)

    SCREEN.fill((255,255,255))
    hexagon_group.draw(SCREEN)
    hexagon_group.update()
    main_classes.camera.update()

import pygame
import hexagon
import camera
import unit

import constants

def create_game_screen(width,height):
    '''sets the game width/height according to the new arguments.
    Responsible for creating the game screen and updating the size of everything existing on it'''
    global SCREEN
    SCREEN = pygame.display.set_mode((width,height), vsync=1)
    pygame.display.set_caption(constants.GAMENAME)

    #scaling value corrects every sprite to the correct size and position
    constants.SCALING_VALUE_ABSOLUTE = width/360 #360,202 being the original game width
    #correct the pos/size of each sprite group
    for i in hexagon.hexagon_group:
        i.update_size_and_position()
    for i in unit.unit_group: #need to run unit group after hexagon group b/c unit placement
        i.update_size_and_position()


def game_update_screen():
    SCREEN.fill((255,255,255))
    hexagon.hexagon_group.draw(SCREEN)
    hexagon.hexagon_group.update()
    camera.camera1.update()
    unit.unit_group.draw(SCREEN)
    unit.unit_group.update() #would use a generic render group but need control of sprite order
    #print(unit.unit_group.sprites())

def sort_polygons():
    '''Clear the hexagon_group render group and fills with the an ordered
    hexagon_dictionary so that sprites render in the correct order.
    NOTE: Run after each new polygon that is added after game init'''
    hexagon.hexagon_group = pygame.sprite.LayeredUpdates()
    ydictionary = {}
    for i in hexagon.hexagon_dictionary.values():
        y = i.y_pos
        ydictionary[y] = i
    ydictionary_keys_sorted = sorted(ydictionary.keys())
    hexagon_list_sorted = []
    for i in ydictionary_keys_sorted:
        hexagon_list_sorted.append(ydictionary[i])
    for i in hexagon_list_sorted:
        hexagon.hexagon_group.add(i)

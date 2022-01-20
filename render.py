import pygame
import hexagon
import camera
import unit

import constants

def create_game_screen(width,height):
    '''sets the game width/height according to the constants file unless new arguments are given.
    Responsible for creating the game screen'''
    global SCREEN
    constants.SCALEINGVALUEREL = width/constants.WIDTH
    constants.SCALEINGVALUEABS = width/360
    #print(constants.SCALEINGVALUEX)
    try:
        for i in hexagon_group:
            i.update_size_and_position()
    except: None
    constants.WIDTH = width
    constants.HEIGHT = height
    SCREEN = pygame.display.set_mode((width,constants.HEIGHT), vsync=1)
    pygame.display.set_caption(constants.GAMENAME)

def game_update_screen():
    SCREEN.fill((255,255,255))
    hexagon.hexagon_group.draw(SCREEN)
    hexagon.hexagon_group.update()
    camera.camera1.update()
    unit.unit_group.draw(SCREEN)
    unit.unit_group.update()
    #print(unit.unit_group.sprites())

def sort_polygons():
    '''orders the hexagon_dictionary so that sprites render in the correct order.
    NOTE: Run after each new polygon that is added after game init'''
    global hexagon_group
    hexagon_group = pygame.sprite.LayeredUpdates()
    ydictionary = {}
    for i in hexagon.hexagon_dictionary.values():
        y = i.y_pos
        ydictionary[y] = i
    ydictionary_keys_sorted = sorted(ydictionary.keys())
    hexagon_list_sorted = []
    for i in ydictionary_keys_sorted:
        hexagon_list_sorted.append(ydictionary[i])
    for i in hexagon_list_sorted:
        hexagon_group.add(i)
    return hexagon_group

import pygame
import hexagon

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

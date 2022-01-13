import pygame
import hexagon

import render

#hexagon group that contains the hexagons to be rendered
hexagon_group = pygame.sprite.LayeredUpdates()

def add_hexagon(a,b):
    '''Creates new hexagon and adds to hexagon list before calling the function to
    positon the polgyon. Hexagon_list needs to be inputed into the render engine
    in sort_hexagons() to render them in the correct order'''
    global hexagon_list
    new_hexagon = hexagon.Hexagon(a,b)
    try: hexagon_list.append(new_hexagon)
    except:
        hexagon_list = []
        hexagon_list.append(new_hexagon)
    print(render.hexagon_list)
    #new_hexagon.position_hexagon_absolute(a,b)

def sort_polygons(hexagon_list):
    '''takes in a list of hexagons and an empty render group and outputs a
    full render group from that list based on hexagon y_pos
    NOTE: Run after each new polygon that is added after game init'''
    global hexagon_group
    hexagon_group = pygame.sprite.LayeredUpdates()
    ydictionary = {}
    for i in hexagon_list:
        y = i.y_pos
        ydictionary[y] = i
    ydictionary_keys_sorted = sorted(ydictionary.keys())
    hexagon_list_sorted = []
    for i in ydictionary_keys_sorted:
        hexagon_list_sorted.append(ydictionary[i])
    for i in hexagon_list_sorted:
        hexagon_group.add(i)
    return hexagon_group

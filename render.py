import pygame
import hexagon

#hexagon group that contains the hexagons to be rendered
hexagon_group = pygame.sprite.LayeredUpdates()

def create_polygons(relative_hexagon, side):
    '''Creates new hexagon and adds to hexagon list before calling the function to
    positon the polgyon. hexagon_list needs to be inputed into the render engine
    in sort_hexagons() to render them in the correct order'''
    global hexagon_list
    new_hexagon = hexagon.Hexagon(100,100)
    try: hexagon_list.append(new_hexagon)
    except:
        hexagon_list = []
        hexagon_list.append(new_hexagon)
    if relative_hexagon != None:
        relative_hexagon.position_neighboring_polygon(side,new_hexagon)
    else: None

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
        print(i.y_pos)
    return hexagon_group

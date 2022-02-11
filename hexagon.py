import pygame
import os

import constants
import directories

import camera
import pixelobject


hexagon_group = pygame.sprite.LayeredUpdates()
hexagon_dictionary = {}


def retrieve_hexagon_at_position(a,b):
    '''used to retrieve a hexgon without needing another hexagon'''
    try:
        hexagon_tile = hexagon_dictionary[(a,b)]
        #print('Hexagon found')
    except:
        print('Error: Error finding that hexagon')
        return None
    return hexagon_tile

def export_hexagon_dictionary():
    '''exports a complete list of the positions and types of hexagons in the
    level for level/game saving'''
    level_hexagons = list(hexagon_dictionary.keys())
    #print(level_hexagons)
    list_index = -1
    for i in level_hexagons:
        list_index += 1 #have to keep track of the element of the list to write it later
        specific_hexagon = hexagon_dictionary.get(i)
        specific_hexagon_type = specific_hexagon.type #get the type of the hexagon
        x = i[0]
        y = i[1]
        level_hexagons[list_index] = (x,y,specific_hexagon_type)
    return level_hexagons

def import_hexagon_dictionary(level_hexagons_list):
    global hexagon_dictionary
    clear_all_hexagons()
    for i in level_hexagons_list:
        hexagon = Hexagon(i[0],i[1],i[2])
        hexagon_dictionary[i[0],i[1]] = hexagon

def clear_all_hexagons():
    '''deltes all hexagons from the hexagon_dictionary. Should also delete from
    memory but I have no idea how that works'''
    #hexagon_list = hexagon_dictionary.values()
    #for i in hexagon_list:
    #    print(i)
        #cull each hexagon
    hexagon_dictionary.clear()

class Hexagon(pixelobject.Pixelobject):
    def __init__(self,a,b,type):
        '''create the hexagon class for OOB'''
        super().__init__()

        # hexagons are represented by a simple a,b coordinate system
        self.a_pos = a
        self.b_pos = b
        self.type = None

        self.original_x_pos = (100 + 28*a +2*b) #before scaling
        self.original_y_pos = (100 +13*a +28*b) #before scaling
        self.x_pos,self.y_pos = self.output_scaled_xy()

        #setting the type
        if type == 'normal':
            self.original_image = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon.png')).convert_alpha()
            self.type = 'normal'
        elif type == 'water':
            self.original_image = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon_water.png')).convert_alpha()
            self.type = 'water'
        else:
            print('Error: Not a valid hexagon type.')
            return None

        self.create_scaled_image_and_rect()
        self.check_conflicting_hexagons(a,b)

    def check_conflicting_hexagons(self,a,b):
        '''creates a dictionay to keep track of where hexagons are
        placed and is used to create the hexagon_group for rendering.
        Called after hexagon init.'''
        global hexagon_dictionary
        ablist = (a,b)
        #try:
        hexagonskeys = hexagon_dictionary.keys()
        for i in hexagonskeys:
            if ablist == i:
                print('Overwriting hexagon at '+ str(ablist))
        hexagon_dictionary[a,b] = self

    def get_position(self):
        '''gets the x and y position of a hexagon (used in unit placement)'''
        return self.x_pos,self.y_pos

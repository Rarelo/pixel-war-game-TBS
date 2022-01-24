import pygame
import os

import constants
import directories

import camera
import pixelobject


hexagon_group = pygame.sprite.LayeredUpdates()


def retrieve_hexagon_at_position(a,b):
    '''used to retrieve a hexgon without needing another hexagon'''
    try:
        hexagon_tile = hexagon_dictionary[(a,b)]
        #print('Hexagon found')
    except:
        print('Error: Error finding that hexagon')
        return None
    return hexagon_tile

class Hexagon(pixelobject.Pixelobject):
    def __init__(self,a,b,type):
        '''create the hexagon class for OOB'''
        super().__init__()

        # hexagons are represented by a simple a,b coordinate system
        self.a_pos = a
        self.b_pos = b

        self.original_x_pos = (100 + 28*a +2*b) #before scaling
        self.original_y_pos = (100 +13*a +28*b) #before scaling
        self.x_pos,self.y_pos = self.output_scaled_xy()

        #setting the type
        if type == 'normal':
            self.original_image = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon.png')).convert_alpha()
        elif type == 'water':
            self.original_image = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon_water.png')).convert_alpha()
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
        try:
            hexagonskeys = hexagon_dictionary.keys()
            for i in hexagonskeys:
                if ablist == i:
                    print('Overwriting hexagon at '+ str(ablist))
        except:
            hexagon_dictionary = {}
        hexagon_dictionary[a,b] = self

    def get_position(self):
        '''gets the x and y position of a hexagon (used in unit placement)'''
        return self.x_pos,self.y_pos

    #need to call hexagon pos upon unit creation to place it on a hexagon
    #every time the game resolution is resized these units need to be replaced

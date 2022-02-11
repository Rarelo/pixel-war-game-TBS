import pygame
import os

import directories
import constants

import camera
import pixelobject
import hexagon

unit_group = pygame.sprite.LayeredUpdates()

def clear_all_units():
    '''deltes all units from the unit_group and should also delte from memory
    but I have no idea how that works'''
    global unit_group
    #would it save time to add this method to the class itself?
    unit_group = pygame.sprite.LayeredUpdates()

class Unit(pixelobject.Pixelobject):
    def __init__(self,a,b):
        '''create the unit class for OOB'''
        global unit_group
        super().__init__()
        #will need to recalculate x, y pos when a,b changes
        self.a_pos = a
        self.b_pos = b
        self.place_unit(a,b) #unit placement borrowed from hexagon


        self.original_image = pygame.image.load(os.path.join(directories.GRAPHICS,'unit.png')).convert_alpha()
        self.create_scaled_image_and_rect()

        unit_group.add(self)

    def update_size_and_position(self):
        '''An overwrite of the pixelobject method because units get their position
        from hexagons'''
        self.place_unit(self.a_pos,self.b_pos)
        self.create_scaled_image_and_rect()

    def place_unit(self,a,b):
        hexagon_tile = hexagon.retrieve_hexagon_at_position(a,b)
        x,y = hexagon_tile.get_position()
        self.x_pos,self.y_pos = x,y-29*constants.SCALING_VALUE_ABSOLUTE

import pygame
import directories
import os

import camera
import constants


class Hexagon(pygame.sprite.Sprite):
    def __init__(self,a,b,type):
        '''create the hexagon class for OOB'''
        super().__init__()
        # a and b position a roated x,y grid that represents each hexagon's position
        self.a_pos = a
        self.b_pos = b
        self.x_pos = (100 + 28*a +2*b)*constants.SCALEINGVALUEREL
        self.y_pos = (100 +13*a +28*b)*constants.SCALEINGVALUEREL

        #setting the type
        flavor = None
        if type == 'normal':
            flavor = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon.png')).convert_alpha()
        elif type == 'water':
            flavor = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon_water.png')).convert_alpha()
        else:
            print('Error: Not a valid hexagon type.')
            return None
        try:
            image_width = hexagon_width
            image_height = hexagon_height
        except:
            image_height_old = flavor.get_height()
            image_width_old = flavor.get_width()
            image_width = image_width_old*constants.SCALEINGVALUEREL
            image_height = image_height_old*constants.SCALEINGVALUEREL
        self.image = pygame.transform.scale(flavor,(image_width,image_height))
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        self.check_conflicting_hexagons(a,b)


    def update(self):
        '''updates the hexagon display/location based on camera movement'''
        #call animation function
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        #self.destroy()


    def update_size_and_position(self):
        '''my attempt to make hexagons scale correctly with the changing screen size'''
        global hexagon_height, hexagon_width
        self.x_pos = self.x_pos*constants.SCALEINGVALUEREL
        self.y_pos = self.y_pos*constants.SCALEINGVALUEREL
        image_height_old = self.image.get_height()
        image_width_old = self.image.get_width()
        image_width = image_width_old*constants.SCALEINGVALUEREL
        image_height = image_height_old*constants.SCALEINGVALUEREL
        hexagon_width = image_width
        hexagon_height = image_height
        self.image = pygame.transform.scale(self.image,(image_width,image_height))
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        #print(self.x_pos,self.y_pos)

    def check_conflicting_hexagons(self,a,b):
        '''creates a dictionay to keep track of where hexagons are placed and is used to create
        the hexagon_group for rendering. Called after hexagon init.'''
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

def get_unit_position(self):
    return [self.x_pos,self.y_pos]

import pygame
import directories
import os

import camera


class Hexagon(pygame.sprite.Sprite):
    def __init__(self,a,b,type):
        '''create the hexagon class for OOB'''
        super().__init__()
        # a and b position a roated x,y grid that represents each hexagon's position
        self.a_pos = a
        self.b_pos = b
        self.x_pos = 100 + 28*a +2*b
        self.y_pos = 100 +13*a +28*b

        #setting the type
        hexagon = None
        if type == 'normal':
            hexagon = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon.png')).convert_alpha()
        if type == 'water':
            hexagon = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon_water.png')).convert_alpha()
        if type == None:
            print('type error')
            return None
        #hexagon = pygame.transform.scale2x(hexagon)
        self.image = hexagon
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        self.check_conflicting_hexagons(a,b)


    def update(self):
        '''updates the hexagon display/location based on camera movement'''
        #call animation function
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        #self.destroy()

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

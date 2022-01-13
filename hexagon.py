import pygame
import directories
import os

import camera


class Hexagon(pygame.sprite.Sprite):
    def __init__(self,a,b):
        '''create the hexagon class for OOB'''
        super().__init__()
        # a and b position a roated x,y grid that represents each hexagon's position
        self.a_pos = a
        self.b_pos = b
        self.x_pos = 100 + 28*a
        self.y_pos = 100 +13*b
        hexagon = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon.png')).convert_alpha()
        #hexagon = pygame.transform.scale2x(hexagon)
        self.image = hexagon
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))


    def update(self):
        '''updates the hexagon display/location based on camera movement'''
        #call animation function
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        #self.destroy()

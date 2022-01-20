import pygame
import hexagon
import camera

import os
import directories
import constants

unit_group = pygame.sprite.LayeredUpdates()

class Unit(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos):
        '''create the unit class for OOB'''
        global unit_group
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        image = pygame.image.load(os.path.join(directories.GRAPHICS,'unit.png')).convert_alpha()

        image_height_old = image.get_height()
        image_width_old = image.get_width()
        image_width = image_width_old*constants.SCALEINGVALUEREL
        image_height = image_height_old*constants.SCALEINGVALUEREL

        self.image = pygame.transform.scale(image,(image_width,image_height))
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        unit_group.add(self)

    def update(self):
        '''updates the hexagon display/location based on camera movement'''
        #call animation function
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        #print(self.image.get_height())

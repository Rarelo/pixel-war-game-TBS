import pygame
import os

import directories
import constants
import camera

class Pixelobject(pygame.sprite.Sprite):
    ## METHODS FOR SPRITE CREATION
    def __init__(self):
        '''create the underlying class and nessesary functions for
        this game's sprites'''
        self.original_image = pygame.image.load(os.path.join(directories.GRAPHICS,'missing_texture.png')).convert_alpha()
        self.original_x_pos,self.original_y_pos = 0,0 #before scaling
        self.x_pos, self.y_pos = 0,0
        super().__init__()

    def create_scaled_image_and_rect(self):
        self.image = self.output_scaled_image()
        self.rect = self.image.get_rect(center = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))

## METHODS FOR SCALING SPRITES ACCORDING TO THE WINDOW SIZE
    def output_scaled_image(self):
        '''used in init and the main loop scaling'''
        image_width = self.original_image.get_width()
        image_height = self.original_image.get_height()
        scaled_width = image_width*constants.SCALING_VALUE_ABSOLUTE
        scaled_height = image_height*constants.SCALING_VALUE_ABSOLUTE
        scaled_image = pygame.transform.scale(self.original_image,(scaled_width,scaled_height))
        return scaled_image

    def output_scaled_xy(self):
        '''used in init and the main loop scaling'''
        scaled_x_pos = self.original_x_pos*constants.SCALING_VALUE_ABSOLUTE
        scaled_y_pos = self.original_y_pos*constants.SCALING_VALUE_ABSOLUTE
        #print('sprite scale updated to '+str(scaled_x_pos)+' '+str(scaled_y_pos))
        return scaled_x_pos, scaled_y_pos

## SPRITE UPDATE FUNCTIONS
    def update(self):
        '''Updates sprite display/location based on camera movement'''
        #call animation function
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))

    def update_size_and_position(self):
        '''Scale sprite unit and position according to the current screen resolution'''
        self.x_pos,self.y_pos = self.output_scaled_xy()
        self.create_scaled_image_and_rect()

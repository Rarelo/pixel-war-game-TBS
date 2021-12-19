import pygame
import os

pygame.init()

#game directories
BASEDIR = os.getcwd()
GRAPHICS = os.path.join(BASEDIR,"graphics")


class Camera(pygame.math.Vector2):
    def __init__(self):
        '''creates the 'global' vars of camera.x and y. Don't change the vars outside of these functions of course'''
        super().__init__()
        self.x = 0
        self.y = 0
        self.a_pressed = False
        self.d_pressed = False
        self.w_pressed = False
        self.s_pressed = False

    def update(self):
        vector = pygame.Vector2()
        vector.xy = 0,0
        if self.a_pressed:
            vector +=1,0
        if self.d_pressed:
            vector -=1,0
        if self.w_pressed:
            vector +=0,1
        if self.s_pressed:
            vector -=0,1
        try:
            vector = vector.normalize()
            self.x +=vector.x
            self.y +=vector.y
        except:
            return None

#apparently need to define the camera here too for the hexagon class
camera = Camera()

class Hexagon(pygame.sprite.Sprite):
    def __init__(self,x,y):
        '''create the hexagon class for OOB'''
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        hexagon = pygame.image.load(os.path.join(GRAPHICS,'hexagon.png')).convert_alpha()
        #hexagon = pygame.transform.scale2x(hexagon)
        self.image = hexagon
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.x,self.y_pos-camera.y))

    def update(self):
        #call animation function
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.x,self.y_pos-camera.y))
        #self.destroy()

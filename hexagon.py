import pygame
import directories
import os

import camera


class Hexagon(pygame.sprite.Sprite):
    def __init__(self,x,y):
        '''create the hexagon class for OOB'''
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        hexagon = pygame.image.load(os.path.join(directories.GRAPHICS,'hexagon.png')).convert_alpha()
        #hexagon = pygame.transform.scale2x(hexagon)
        self.image = hexagon
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        self.side1 = None
        self.side2 = None
        self.side3 = None
        self.side4 = None
        self.side5 = None
        self.side6 = None
        self.xylist = None


    def update(self):
        '''updates the hexagon display/location based on camera movement'''
        #call animation function
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.camera1.x,self.y_pos-camera.camera1.y))
        #self.destroy()

    def position_neighboring_polygon(self,side,hexagon):
        '''determines the correct xy for the new adjacent polygon.
        Called by the Render Engine during polygon creation'''
        if side == 1:
            #self.side1 = hexagon
            xylist = [self.x_pos - 28, self.y_pos - 13]
            hexagon.correct_position(xylist)
            #hexagon_group.move_to_back(hexagon)
        if side == 2:
            #self.side2 = hexagon
            xylist = [self.x_pos - 2, self.y_pos - 28]
            hexagon.correct_position(xylist)
            #hexagon_group.move_to_back(hexagon)
            #if 2 or 3 rendered after 1 the visuals will break
        if side == 3:
            #self.side3 = hexagon
            xylist = [self.x_pos + 26, self.y_pos - 15]
            hexagon.correct_position(xylist)
            #hexagon_group.move_to_back(hexagon)
        if side == 4:
            #self.side4 = hexagon
            xylist = [self.x_pos - 26, self.y_pos + 15]
            hexagon.correct_position(xylist)
        if side == 5:
            #self.side5 = hexagon
            xylist = [self.x_pos + 2, self.y_pos + 28]
            hexagon.correct_position(xylist)
        if side == 6:
            #self.side6 = hexagon
            xylist = [self.x_pos + 28, self.y_pos + 13]
            hexagon.correct_position(xylist)

    def correct_position(self,xylist):
        '''called to update the location of the hexagon self in relation to it's
        neighbor after position_neighboring_polygon. Called by the render engine
        during polygon creation'''
        self.x_pos = xylist[0]
        self.y_pos = xylist[1]
        #print(self.x_pos)
        #print(self.y_pos)

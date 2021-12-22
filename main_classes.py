import pygame
import os

#first things program needs to work
pygame.init()
clock = pygame.time.Clock()

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
        '''sets camera direction and velocity each frame. past_frame_time and current_frame_time are global vars'''
        global past_frame_time, current_frame_time
        try: #loop to make camera speed frame independent
            past_frame_time = current_frame_time
            current_frame_time = pygame.time.get_ticks()/1000
            dt = current_frame_time-past_frame_time
        except:
            current_frame_time = pygame.time.get_ticks()/1000
            dt = 1
        dt = dt * 60
        vector = pygame.Vector2()
        vector.xy = 0,0
        if self.a_pressed:
            vector -=1,0
        if self.d_pressed:
            vector +=1,0
        if self.w_pressed:
            vector -=0,1
        if self.s_pressed:
            vector +=0,1
        try:
            vector = vector.normalize()
            self.x +=vector.x*dt
            self.y +=vector.y*dt
        except:
            return None

#define game camera object here for hexagon class
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
        self.rect = self.image.get_rect(midbottom = (self.x_pos-camera.x,self.y_pos-camera.y))
        #self.destroy()

    def create_neighboring_polygon(self,side,hexagon):
        '''saves polygon adjacency and moves a polygon to the correct neighboring side'''
        if side == 1:
            self.side1 = hexagon
        if side == 2:
            self.side2 = hexagon
        if side == 3:
            self.side3 = hexagon
        if side == 4:
            self.side4 = hexagon
            xylist = [self.x_pos - 26, self.y_pos + 15]
            hexagon.correct_position(xylist)
            print(4, xylist)
        if side == 5:
            self.side5 = hexagon
            xylist = [self.x_pos + 2, self.y_pos + 28]
            hexagon.correct_position(xylist)
            print(5, xylist)
        if side == 6:
            self.side6 = hexagon
            xylist = [self.x_pos + 28, self.y_pos + 13]
            hexagon.correct_position(xylist)
            print(6, xylist)

    def correct_position(self,xylist):
        '''called to update the location of a hexagon in relation to it's neighbor'''
        self.x_pos = xylist[0]
        self.y_pos = xylist[1]
        #print(self.x_pos)
        #print(self.y_pos)

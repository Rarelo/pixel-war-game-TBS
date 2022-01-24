import pygame
import constants


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
            self.x +=(vector.x*dt)*constants.SCALING_VALUE_ABSOLUTE
            self.y +=(vector.y*dt)*constants.SCALING_VALUE_ABSOLUTE
        except:

            return None

#define game camera object here for hexagon class
camera1 = Camera()

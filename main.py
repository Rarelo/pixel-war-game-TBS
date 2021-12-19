import pygame
from sys import exit
import os

## TODO:
#vsync not existing
#polygon placement system
#fix hexagons to render as a group


#global vars
WIDTH = 360 #make rendering system based on multiples?
HEIGHT = 202

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),pygame.SCALED) #360 202?
#print(pygame.display.list_modes())
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
        print(dir())


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

class Hexagon(pygame.sprite.Sprite):
    def __init__(self):
        '''create the hexagon class for OOB'''
        super().__init__()
        hexagon = pygame.image.load(os.path.join(GRAPHICS,'hexagon.png')).convert_alpha()
        #hexagon = pygame.transform.scale2x(hexagon)
        self.image = hexagon
        self.rect = self.image.get_rect(midbottom = (80-camera.x,100-camera.y))

    def update(self):
        #call animation function
        self.rect = self.image.get_rect(midbottom = (300-camera.x,100-camera.y))
        #self.destroy()

#creates the camera
camera = Camera()

#creates the map hexagons
hexagon1 = pygame.sprite.GroupSingle()
hexagon1.add(Hexagon())

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit game
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN: #only checks when a key is hit initally
            if event.key == pygame.K_f: #fullscreen
                pygame.display.toggle_fullscreen()
            if event.key == pygame.K_a: #need to make hold down button work
                camera.a_pressed = True
            if event.key == pygame.K_d: #need to make hold down button work
                camera.d_pressed = True
            if event.key == pygame.K_w: #need to make hold down button work
                camera.w_pressed = True
            if event.key == pygame.K_s: #need to make hold down button work
                camera.s_pressed = True
        if event.type == pygame.KEYUP: #for buttons that need to be held down
            if event.key == pygame.K_a:
                camera.a_pressed = False
            if event.key == pygame.K_d:
                camera.d_pressed = False
            if event.key == pygame.K_w:
                camera.w_pressed = False
            if event.key == pygame.K_s:
                camera.s_pressed = False

    #draw/update screen/objects
    pygame.display.update()
    clock.tick(60)

    SCREEN.fill((255,255,255))
    hexagon1.draw(SCREEN)
    hexagon1.update()
    camera.update()

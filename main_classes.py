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
#define the render group for the hexagons
hexagon_group = pygame.sprite.LayeredUpdates()

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
        '''called to update the location of a hexagon in relation to it's
        neighbor after position_neighboring_polygon. Called by the render engine
        during polygon creation'''
        self.x_pos = xylist[0]
        self.y_pos = xylist[1]
        #print(self.x_pos)
        #print(self.y_pos)

class RenderEngine():
    def __init__(self):
        None

    def create_polygons(self, relative_hexagon, side):
        '''Creates new hexagon and adds to hexagon list before calling the function to
        positon the polgyon. hexagon_list needs to be inputed into the render engine
        in sort_hexagons() to render them in the correct order'''
        global hexagon_list
        new_hexagon = Hexagon(100,100)
        try: hexagon_list.append(new_hexagon)
        except:
            hexagon_list = []
            hexagon_list.append(new_hexagon)
        if relative_hexagon != None:
            relative_hexagon.position_neighboring_polygon(side,new_hexagon)
        else: None

    def sort_polygons(self, hexagon_list):
        '''takes in a list of hexagons and an empty render group and outputs a
        full render group from that list based on hexagon y_pos
        NOTE: Run after each new polygon that is added after game init'''
        global hexagon_group
        hexagon_group = pygame.sprite.LayeredUpdates()
        ydictionary = {}
        for i in hexagon_list:
            y = i.y_pos
            ydictionary[y] = i
        ydictionary_keys_sorted = sorted(ydictionary.keys())
        hexagon_list_sorted = []
        for i in ydictionary_keys_sorted:
            hexagon_list_sorted.append(ydictionary[i])
        for i in hexagon_list_sorted:
            hexagon_group.add(i)
            print(i.y_pos)
        return hexagon_group

RenderEngine1 = RenderEngine() #creates an instance of the render engine class for the console

class TextConsole():
    def __init__(self):
        None

    def user_command_input(self):
        command_input = input("Enter Command: ")
        self.parse_command(command_input)

    def run_command(self, command, arguments):
        '''runs implemented commands while testing for errors.
        NOTE: Should break into sub methods/classes'''
        global hexagon_group, hexagon_list
        if command == 'create_polygons':
            try:
                arguments_list = arguments.split(",")
            except:
                print('Error: Enter Integers for Arguments')
                return None
            for i in arguments_list:
                try:
                    int(i)
                except:
                    print("Error: Enter Integers for Arugments")
                    return None
            hexagon_number = int(arguments_list[0])
            side = int(arguments_list[1])
            if side > 6:
                print('Error: First argument too big. Hexagons only have 6 sides')
            RenderEngine1.create_polygons(hexagon_list[hexagon_number-1],side)
            hexagon_group = RenderEngine1.sort_polygons(hexagon_list)
            print('Success')
            #print(hexagon_list)
            return None
        if command == 'help':
            print('unimplemented')
            #input relative hexagon number and desired side, both in integers
        else:
            print('Error: Not a command')

    def parse_command(self, command_input):
        '''pareses the command_list into command and argument variables while also
        testing for parenthesis errors'''
        if command_input.find("(") != -1:
            command_list = []
            command_list = command_input.split("(")
            if command_list[1].find(")") == -1:
                print('Error: Parenthesis Error')
                return None
            else:
                command_list.append(command_list[1].split(")")[0])
            command = command_list[0]
            arguments = command_list[2]
            self.run_command(command,arguments)
        else:
            command = command_input
            self.run_command(command,None)

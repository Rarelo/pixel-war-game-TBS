import pygame
import directories
import render
import hexagon

import constants


def user_command_input():
    '''takes and outputs user input'''
    command_input = input("Enter Command: ")
    parse_command(command_input)

def parse_command(command_input):
    '''Uses parethesis to parse the user input into runable commands and calls the run function'''
    if command_input.find("(") != -1: #if it finds a
        command_input = command_input.replace(' ','') #spaces are removed
        command_list = command_input.split(")") #using ) to parse the number of commands
        command_list = command_list[:-1]
        for i in command_list: #split all the commands into parsable bits
            command_split = i.split('(')
            command = command_split[0]
            arguments = command_split[1]
            arguments_list = arguments.split(',')
            choose_command(command,arguments_list)
    else:
        print('Error: No Parenthesis')
        user_command_input()

def choose_command(command,arguments_list):
    '''runs implemented commands. NOTE will crash easily upon mistyping'''
    if command == 'hexagon':
        run_hexagon(arguments_list)
    if command == 'help':
        run_help(arguments_list)
    if command == 'quit':
        run_quit()
    if command == 'render':
        #run_change_resolution(arguments_list)
        print('currently disabled for safety because it will break hexagon placement')
    if command == 'rendersizes':
         print(pygame.display.list_modes())
    if command == 'game':
        None

def run_help(arguments_list):
    print('unimplemented')

def run_quit():
    pygame.quit()
    exit()

def run_hexagon(arguments_list):
    '''command that creates a hexagon based on parsed user inputs'''
    for i in range(2):
        try:
            arguments_list[i] = int(arguments_list[i])
        except: print("Error: Input integers for first two arguments")
    try:
        if type(arguments_list[0]) == type(1): #check to make sure the arguments are the right types
            if type(arguments_list[1]) == type(1):
                hexagon.Hexagon(arguments_list[0],arguments_list[1],arguments_list[2])
                hexagon.hexagon_group = render.sort_polygons()
                print('Hexagon created at ('+str(arguments_list[0])+','+str(arguments_list[1])+')')
            else:
                print('Error: Hexagon takes 3 arguments. An integer, an integer, and a string')
                user_command_input()
        else:
            print('Error: Hexagon takes 3 arguments. An integer, an integer, and a string')
            user_command_input()
    except:
        print('Error: Input Error')
        user_command_input()

def run_change_resolution(arguments_list):
    for i in range(2):
        try:
            arguments_list[i] = int(arguments_list[i])
        except:
            print('Error3: Input numbers for screen width and height')
            user_command_input()
    if type(arguments_list[0]) == type(1): #check to make sure the arguments are the right types
        if type(arguments_list[1]) == type(1):
            render.create_game_screen(arguments_list[0],arguments_list[1])
        else:
            print('Error2: Input numbers for screen width and height')
            user_command_input()
    else:
        print('Error1: Input numbers for screen width and height')
        user_command_input()

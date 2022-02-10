import pygame
import directories
import render
import hexagon
import unit
import parse
import save

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
        return None

def choose_command(command,arguments_list):
    '''selects desired command.Add another command with arguments by copying the unit or hexagon
    command section and changing the desired function inputs to test for. Runs check_inputs to
    prevent user input crashes and to change arguments_list strings into integers'''
    if command == 'hexagon':
        arguments_list = parse.check_inputs_and_interify(arguments_list,type(1),type(1),type('s'),None,None)
        if arguments_list != None: #keeps hexagon from activating with invalid inputs
            #print('check passed')
            run_hexagon(arguments_list)
        else: return None
    if command == 'quit':
        run_quit()
    if command == 'render':
        arguments_list = parse.check_inputs_and_interify(arguments_list,type(1),type(1),None,None,None)
        render.create_game_screen(arguments_list[0],arguments_list[1])
    if command == 'rendersizes':
         print(pygame.display.list_modes())
    if command == 'game':
        None #to go back to the game
    if command == 'unit':
        arguments_list = parse.check_inputs_and_interify(arguments_list,type(1),type(1),None,None,None)
        if arguments_list != None: #keeps hexagon from activating with invalid inputs
            #print('check passed')
            place_unit(arguments_list)
        else:
            return None
    if command == 'savelevel':
        save.save_level()
    if command == 'loadlevel':
        save.load_level()

#################################################################################################
########################## ACTUAL TERMINAL COMMANDS HERE ########################################
#################################################################################################

def run_hexagon(arguments_list):
    '''command that creates a hexagon based on parsed user inputs'''
    hexagon.Hexagon(arguments_list[0],arguments_list[1],arguments_list[2])
    render.sort_polygons()
    print('Hexagon created at ('+str(arguments_list[0])+','+str(arguments_list[1])+')')

def place_unit(arguments_list):
    a = arguments_list[0] #actual code begins
    b = arguments_list[1]
    hexagon_tile = hexagon.retrieve_hexagon_at_position(a,b)
    if hexagon_tile == None:
        user_command_input() #restart the terminal attempt
        return None
    unit.Unit(a,b)

def run_quit():
    pygame.quit()
    exit()

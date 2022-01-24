import pygame
import directories
import render
import hexagon
import unit

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
        arguments_list = check_inputs_and_interify(arguments_list,type(1),type(1),type('s'),None,None)
        if arguments_list != None: #keeps hexagon from activating with invalid inputs
            #print('check passed')
            run_hexagon(arguments_list)
        else: return None
    if command == 'quit':
        run_quit()
    if command == 'render':
        arguments_list = check_inputs_and_interify(arguments_list,type(1),type(1),None,None,None)
        render.create_game_screen(arguments_list[0],arguments_list[1])
    if command == 'rendersizes':
         print(pygame.display.list_modes())
    if command == 'game':
        None #to go back to the game
    if command == 'unit':
        arguments_list = check_inputs_and_interify(arguments_list,type(1),type(1),None,None,None)
        if arguments_list != None: #keeps hexagon from activating with invalid inputs
            #print('check passed')
            place_unit(arguments_list)
        else:
            return None

def check_inputs_and_interify(arguments_list, input1, input2, input3, input4, input5):
    '''a modular function to check if the user inputed inputs are correct for the desired command
    NOTE: Exports a arguments list with strings converted to integers (when possible) and takes on the
    user defined arguments_list and each type of desired input for each part of that list.
    Run before calling the desired terminal function to avoid errors. Input None in the inputs field
    for extra parameters"'''

    function_arguments_list = []
    function_arguments_list.append(input1)
    function_arguments_list.append(input2)
    function_arguments_list.append(input3)
    function_arguments_list.append(input4)
    function_arguments_list.append(input5)
    for i in function_arguments_list:
        try:
            function_arguments_list.remove(None) #skip inputs of None
        except:
            None
    i_pos = -1 #keep track of the index element in a list
    for i in arguments_list: #convert strings to integers
        try:
            i_pos += 1
            arguments_list[i_pos] = int(i)
        except:
            None
    #check to make sure the number of user inputs matches the function input
    if len(function_arguments_list) == len(arguments_list):
        None
    else:
        print('Error: Incorrect Number of arguments')
        user_command_input() #restart the terminal attempt
        return None
    i_pos = -1
    for i in function_arguments_list:
        i_pos +=1
        if i == type(arguments_list[i_pos]): #check if each user input equals the desired function input type
            None
        else:
            print('Error: Wrong type of input for argument '+str(i_pos+1))
            user_command_input() #restart the terminal attempt
            return None
    return arguments_list

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

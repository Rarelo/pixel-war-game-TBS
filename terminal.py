import pygame
import directories
import render
import hexagon


def user_command_input():
    '''takes and outputs user input'''
    command_input = input("Enter Command: ")
    parse_command(command_input)

def parse_command(command_input):
    '''pareses the command_list into command and argument variables.
    NOTE: Will crash easily upon mistyping'''
    if command_input.find("(") != -1:
        command_input.replace(" ",'')
        command_input.replace(" ",'')
        command_list = []
        command_list = command_input.split("(")
        if command_list[1].find(")") == -1:
            print('Error: Parenthesis Error')
            return None
        else:
            command_list.append(command_list[1].split(")")[0])
        command = command_list[0]
        arguments = command_list[2]
        run_command(command,arguments)
    else:
        command = command_input
        run_command(command,None)

def run_command(command, arguments):
    '''runs implemented commands. NOTE will crash easily upon mistyping'''
    if command == 'hexagon':
        try:
            arguments_list = arguments.split(",")
        except:
            print('Error: Enter Integers for Arguments')
            return None
        #for i in arguments_list:
        #    try:
        #        int(i)
        #    except:
        #        print("Error: Enter Integers for Arugments")
        #        return None
        a_pos = int(arguments_list[0])
        b_pos = int(arguments_list[1])
        type = arguments_list[2]
        hexagon.Hexagon(a_pos,b_pos,type)
        hexagon.hexagon_group = render.sort_polygons()
        print('Success')
        #print(render.hexagon_group)
        return None
    if command == 'help':
        print('unimplemented')
        #input relative hexagon number and desired side, both in integers
    else:
        print('Error: Not a command')

import pygame
import directories
import render
import hexagon


def user_command_input():
    command_input = input("Enter Command: ")
    parse_command(command_input)

def run_command(command, arguments):
    '''runs implemented commands while testing for errors.
    NOTE: Should break into sub methods/classes'''
    if command == 'hexagon':
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
        render.create_polygons(render.hexagon_list[hexagon_number-1],side)
        hexagon.hexagon_group = render.sort_polygons(render.hexagon_list)
        print('Success')
        #print(render.hexagon_group)
        return None
    if command == 'help':
        print('unimplemented')
        #input relative hexagon number and desired side, both in integers
    else:
        print('Error: Not a command')

def parse_command(command_input):
    '''pareses the command_list into command and argument variables while also
    testing for parenthesis errors'''
    #should remove spaces and tabs at some point in here
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
        run_command(command,arguments)
    else:
        command = command_input
        run_command(command,None)

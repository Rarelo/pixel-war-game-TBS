import os
import directories
import hexagon
import parse
import render
import unit

###############################################################################
################ File for Saving and Loading Levels and Games #################
###############################################################################

def save_level():
    '''function to save a level layout to a file. Does not save units'''
    filepath = os.path.join(directories.LEVELS, 'level_test.txt')
    with open(filepath,'w') as file: #this seems to be nessesary to use a path
    #var to the file to write to before os.path.join to avoid a crash
        file.write('This is a Project Hexagon level file.\n')
        level_hexagons = hexagon.export_hexagon_dictionary()
        print(level_hexagons)
        file.write(str(level_hexagons))

#future features to implement in saving:
#chose a filename
#overwrite protection
#possible that it should read the file chunks at a time for memory purporses

def load_level():
    '''take in the level hexagon save file, parse it into a list, replace the
    old hexagon dictionary, & update the hexagon render group. Deletes units.'''
    unit.clear_all_units()
    filepath = os.path.join(directories.LEVELS, 'level_test.txt')
    with open(filepath,'r') as file:
        first_line = file.readline() #outputs a string
        file_contents = file.read() #seek starts after the first line
    level_hexagons_list = parse.parse_save_file(first_line,file_contents)
    if level_hexagons_list == None: #quit the save attempt if file is corrupt
        return None
    hexagon.import_hexagon_dictionary(level_hexagons_list)
    render.sort_polygons()

#possibly add load confirmation

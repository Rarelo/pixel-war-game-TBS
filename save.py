import os
import directories
import hexagon

###############################################################################
################ File for Saving and Loading Levels and Games #################
###############################################################################

def save_level():
    filepath = os.path.join(directories.LEVELS, 'level_test.txt')
    with open(filepath,'w') as file: #this seems to be nessesary to create the
    #file to write before os.path.join to avoid a crash
        file.write('This is a Project Hexagon level file.\n')
        level_hexagons = hexagon.export_hexagon_dictionary()
        print(level_hexagons)
        file.write(str(level_hexagons))

#future features to implement in saving:
#chose a filename
#overwrite protection

def load_level():
    pass

#need to clear both the hexagon and units by nessesity when loading a new level


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
        return None
    i_pos = -1
    for i in function_arguments_list:
        i_pos +=1
        if i == type(arguments_list[i_pos]): #check if each user input equals the desired function input type
            None
        else:
            print('Error: Wrong type of input for argument '+str(i_pos+1))
            return None
    return arguments_list

def parse_save_file(first_line,file_contents):
    '''double check the save file is actually correct and return the hexagon list'''
    if first_line == 'This is a Project Hexagon level file.\n':
        pass
    else:
        print("Error: Not a valid hexagon save file")
        return None
    loaded_list = eval(file_contents) #convert file string into code
    if type(loaded_list) != type([]):
        print('Error: Imported string should be a list')
        return None
    for i in loaded_list:
        Nonecheck = check_inputs_and_interify(i, type(1), type(2), type('s'), None, None)
        if i[2] != 'normal': #a bit of sloppy coding right here, which will break with new hexagons, to check if the list strings
        #are actually hexagon values - probably should rewrite the whole hexagon type system while I'm at it
            if i[2] != 'water':
                print(i[2])
                print('Error: Invalid type of hexagon')
                return None
    if Nonecheck == None: #if check inputs encounters an error abort
        return None
    print(loaded_list)
    return loaded_list

def function_names(file_handle):
    ''' (io.TextIOWrapper) -> list of str
    Returns the name of the function in the file opened.
    REQ: The file read has to be in the same folder as this file.
    '''
    # read the entire file line by line
    whole_file = file_handle.readlines()
    # initialize all variables
    list_of_functions = []
    has_def = False
    # loop through whole_file
    for next_line in whole_file:
        # check if the line has 'def ' occurs
        if next_line.startswith("def "):
            bracket_index = next_line.find('(')
            function_name = next_line[4:bracket_index]
            list_of_functions += [function_name]
    # return the list
    return list_of_functions


def justified(file_handle):
    ''' (io.TextIOWrapper) -> bool
    Returns True iff the entire file is left-justified.
    REQ: The file read should be in the same folder as this file.
    '''
    # read the entire file line by line
    whole_file = file_handle.readlines()
    # initialize any variables needed
    is_justified = True
    index = 0
    # loop through the entire file
    while (is_justified is True) and (index < len(whole_file)):
        # check if none of the lines start with a space ' '
        is_justified = not whole_file[index].startswith(' ')
        index += 1
    # return the result
    return is_justified

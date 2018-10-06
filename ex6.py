def copy_me(unchange_list):
    ''' (list) -> list
    Returns a copy of unchange_list with the following changes:
    - Strings with upper case letters
    - Integers and floats increased by 1
    - Booleans are reversed (i.e. False becomes True and vice versa)
    - Lists are replaced with 'List'
    The input unchange_list will not be mutated in anyway.
    REQ: The list should not contain elements other than strings, integers,
    floats, booleans and lists.
    >>> copy_me(['hello', -2, 2.0, True, [1, 2, 5000]])
    ['HELLO', -1, 3.0, False, 'List']
    >>> copy_me([False, 'world', 'ROUND', 6, 100.001])
    [True, 'WORLD', 'ROUND', 7, 101.001]
    '''
    # Make a copy of the list
    copied_list = unchange_list[:]
    # make an empty final list
    final_list = []
    # go through each element of the new list
    for index in range(0, len(copied_list), 1):
        # if type of element is str
        if (type(copied_list[index]) is str):
            # convert str to upper case
            copied_list[index] = copied_list[index].upper()
        # if type is boolean
        elif (type(copied_list[index]) is bool):
            # negate it
            copied_list[index] = not copied_list[index]
        # if type is float or int
        elif (type(copied_list[index]) is float) or (type(copied_list[index])
                                                     is int):
            # add one to element
            copied_list[index] += 1
        # if type is list
        elif (type(copied_list[index]) is list):
            # replace it with 'List'
            copied_list[index] = 'List'
        final_list += [copied_list[index]]
    # return the new list
    return final_list


def mutate_me(change_list):
    ''' (list) -> NoneType
    Returns None and changes change_list in the following ways:
    - Converts strings to upper case
    - Adds 1 to floats and integers
    - Negates booleans (i.e True becomes False and vice versa)
    - Replaces lists with 'Lists'
    REQ: The list should not contain elements other than strings, integers,
    floats, booleans and lists.
    >>> change_list = ['hello', -2, 2.0, True, [1, 2, 5000]]
    >>> mutate_me(change_list)
    >>> change_list == ['HELLO', -1, 3.0, False, 'List']
    True
    >>> change_list = [False, 'world', 'ROUND', 6, 100.001]
    >>> mutate_me(change_list)
    >>> change_list == [True, 'WORLD', 'ROUND', 7, 101.001]
    True
    '''
    # make an empty final list
    final_list = []
    # go through each element of the input list
    for index in range(0, len(change_list), 1):
        # if type of element is str
        if (type(change_list[index]) is str):
            # convert str to upper case
            change_list[index] = change_list[index].upper()
        # if type is boolean
        elif (type(change_list[index]) is bool):
            # negate it
            change_list[index] = not change_list[index]
        # if type is float or int
        elif (type(change_list[index]) is float) or (type(change_list[index])
                                                     is int):
            # add one to element
            change_list[index] += 1
        # if type is list
        elif (type(change_list[index]) is list):
            # replace it with 'List'
            change_list[index] = 'List'
        # add the changed element into the final list
        final_list += [change_list[index]]

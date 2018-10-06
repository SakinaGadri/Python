def insert(changing_element, insert_this, index):
    ''' (list|str, list|str, int) -> list|str
    Returns a copy of changing_element after inserting insert_this at the input
    index.
    REQ: index >= 0
    REQ: index < length of the input changing_element
    REQ: index has to be a whole number
    REQ: changing_element and insert_this always have to be the same data type
    >>> insert('Hy', 'e', 1)
    'Hey'
    >>> insert([5, 6, 5, 2, 7, 3, 4], [3], 0)
    [3, 5, 6, 5, 2, 7, 3, 4]
    '''
    # slice the list/str till the index and store the first in a variable
    first_part = changing_element[:index]
    # slice the list/str again and store the end part in a variable
    second_part = changing_element[index:]
    # add the parts together, adding insert_this to the new list/str
    changed_element = first_part + insert_this + second_part
    # return the new list
    return changed_element


def up_to_first(changing_element, change_up_to):
    ''' (list|str, object) -> list|str
    Returns changing_element up to the first occurance of change_up_to.
    Returns changing_element if change_upto is not found.
    REQ: change_up_to has to be a string or an integer
    >>> up_to_first([6, 0, 7, 5], 5)
    [6, 0, 7]
    >>> up_to_first('HelloWorld', 'W')
    'Hello'
    >>> up_to_first('Study Room', 'A')
    'Study Room'
    '''
    # check if change_up_to exists
    if (change_up_to in changing_element):
        # find the index at which it occurs
        index = changing_element.index(change_up_to)
        # splice to the index
        result = changing_element[:index]
    else:
        result = changing_element
    # return the result
    return result


def cut_list(cut_list, at_index):
    ''' (list|str, int) -> list|str
    Returns the cut_list after swapping the list at at_index
    REQ: at_index > 0
    REQ: at_index < length of cut_list
    >>> cut_list('ABBC', 1)
    'BCBA'
    >>> cut_list([1, 2, 3, 9, 8, 7], 2)
    [9, 8, 7, 3, 1, 2]
    '''
    # splice cut_list at at_index; store the parts in different variables
    first_part = cut_list[:at_index]
    second_part = cut_list[at_index+1:]
    # store the element at index
    item_at_index = cut_list[at_index:at_index+1]
    # return the combination of the previous parts
    return second_part + item_at_index + first_part

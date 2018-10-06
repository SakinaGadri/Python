def create_dict(file_handle):
    ''' (io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
    Returns a dictionary with username as a key and list of last name,
    first name, gender, age and email address, in that order.
    REQ: age has be greater than 0
    REQ: gender can be either F, M, X
    '''
    # initialize any variables needed
    username_to_personal_info = {}
    usernames = []
    personal_info = []
    all_personal_info = []
    # read all the lines in the file as a list
    all_lines = file_handle.readlines()
    # for each string in the list
    for next_line in all_lines:
        # split the string by spaces
        list_of_info = next_line.split()
        # make the first element into a key
        usernames += [list_of_info[0]]
        # get the last name, first name, gender, age and email_address
        last_name = list_of_info[2]
        first_name = list_of_info[1]
        gender = list_of_info[4]
        age = list_of_info[3]
        email_address = list_of_info[5]
        # combine last name, first name, gender, age and email address into a
        # single variable
        personal_info = [last_name, first_name, email_address, int(age), gender]
        all_personal_info += [personal_info]
    # construct the dictionary
    for index in range(len(usernames)):
        username_to_personal_info[usernames[index]] = all_personal_info[index]
    # return the dictionary
    return username_to_personal_info


def update_field(username_to_personal_info, username, field_name, new_value):
    ''' (dict, str, str, str|int) -> dict
    This function mutates username_to_personal_info according to the given
    inputs.
    REQ: field_name has to be one of the following: {'AGE', 'LAST', 'FIRST',
    'GENDER', 'EMAIL', 'AGE'}
    REQ: username should already exists in the dictionary
    REQ: username_to_personal_info should not be empty
    >>> username_to_personal_info = {'asmith':['Smith', 'Alice', \
    'alice.smith@utsc.utoronto.ca', 31, 'F']}
    >>> update_field(username_to_personal_info, 'asmith', 'AGE', 32)
    >>> username_to_personal_info == {'asmith':['Smith', 'Alice', \
    'alice.smith@utsc.utoronto.ca', 32, 'F']}
    True
    '''
    change_value_at = 0
    # check which field has been input
    if (field_name == 'LAST'):
        change_value_at = 0
    elif (field_name == 'FIRST'):
        change_value_at = 1
    elif (field_name == 'EMAIL'):
        change_value_at = 2
    elif (field_name == 'AGE'):
        change_value_at = 3
    elif (field_name == 'GENDER'):
        change_value_at = 4
    # use the username and call all the values
    values = username_to_personal_info[username]
    # according to the field that has been input
    # change the value that exists
    values[change_value_at] = new_value
    # update the dictionary
    username_to_personal_info[username] = values

file_handle = open('data_4e.txt', 'r')
# constructing my dict
my_dict = create_dict(file_handle)
file_handle.close()

# updating the email
print (my_dict)
print ('\n------\n') # to the dictionaries things out
update_field(my_dict, 'jsmith', 'EMAIL', 'iliveinpei@cavendish.ca')
print (my_dict)
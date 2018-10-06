class LightSwitch:
    '''This is a class for a light switch'''
    def __init__(self, switch_state):
        ''' (LightSwitch, str) -> NoneType
        Returns None and assigns the input parameters to class variables
        REQ: switch_state can only be 'on' and 'off'
        '''
        # assign the input parameters to instance variables in the class
        # 'on' is true and 'off' is false
        self._switch_state = (switch_state == 'on')

    def turn_on(self):
        ''' (LightSwitch) -> NoneType
        Returns None and turns the switch 'on' if it was 'off'
        '''
        # if the switch is 'off'
        if (self._switch_state is False):
            # make it 'on'
            self._switch_state = True

    def turn_off(self):
        ''' (LightSwitch) -> NoneType
        Returns None and turns the switch 'off' if it was 'on'
        '''
        # if the switch is 'on'
        if (self._switch_state is True):
            # make it 'off'
            self._switch_state = False

    def flip(self):
        ''' (LightSwitch) -> NoneType
        Returns None and flips the switch when called; i.e. when it is 'on',
        flip method will flip it to 'off' and vice versa
        '''
        self._switch_state = not self._switch_state

    def get_position(self):
        ''' (LightSwitch) -> bool
        Returns a bool of the state of the switch
        '''
        return self._switch_state

    def __str__(self):
        ''' (LightSwitch) -> str
        Returns a str which tells the user about the current state on the
        switch
        '''
        # if the switch is 'on'
        if (self._switch_state is True):
            # return a statement with 'on'
            string = 'I am on'
        # if the switch is off
        else:
            # return the statement with off
            string = 'I am off'
        # return the string
        return string


class SwitchBoard():
    '''This class represents a switch board with multiple switches'''
    def __init__(self, num_of_switches):
        ''' (SwitchBoard, int) -> NoneType
        Returns None and assigns the input parameters to class variables
        REQ: num_of_switches should be greater than 0
        '''
        # make an empty list about switches
        self._switches = []
        # create the input number of switches
        for index in range(num_of_switches):
            # set the default as off
            self._switches.append(LightSwitch('off'))

    def __str__(self):
        ''' (SwitchBoard) -> str
        Returns a string which informs the user about the index of the switch
        that is 'on'
        '''
        # initialize the string
        string = ''
        # loop through all the switches
        for index in range(len(self._switches)):
            # check if the switch is on. If true
            if (self._switches[index].get_position()):
                # add it to the string
                string += ' ' + str(index)
        # return string
        return 'The following switches are on: ' + string

    def which_switch(self):
        ''' (SwitchBoard) -> list of int
        Returns a list where the switches that are on.
        '''
        # initialize all varoables
        on_switches = []
        # go through each switch
        for index in range(len(self._switches)):
            # if the switch is 'on'
            if (self._switches[index].get_position()):
                # then add it to the list
                on_switches.append(index)
        # return the list
        return on_switches

    def flip(self, switch_number):
        ''' (SwitchBoard, int) -> NoneType
        Returns None and flips the switch at switch_number i.e. flips 'on' to
        'off' and vice versa.
        REQ: switch_number should be greater than 0
        '''
        # flip the switch_number by calling the flip method in switch
        self._switches[switch_number].flip()

    def flip_every(self, add_this):
        ''' (SwitchBoard, int) -> NoneType
        Returns None and flips the position of the switches starting from 0 and
        adding add_this to it
        REQ: add this has to be greater than 0 and less than the number of
        switches
        '''
        for index in range(0, len(self._switches), add_this):
            self._switches[index].flip()

    def reset(self):
        ''' (SwitchBoard) -> NoneType
        Returns None and resets all the switches to 'off'
        '''
        # loop through the entire list
        for index in range(len(self._switches)):
            # set the position to 'off' for each switch
            self._switches[index].turn_off()

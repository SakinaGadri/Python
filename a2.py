"""CSCA08 Assignment 2, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Sakina Shabbir Gadriwala
 UtorID: gadriwa1
 Student Number: 1004351051
 Date: December 3rd, 2017
"""


class PositionError(Exception):
    ''' an error that is raised when the position does not have a set
    chromosome value'''


class PairError(Exception):
    ''' an error that is raised when the pair does not have a set chromosome
    value '''


class ChromosomeError(Exception):
    ''' an error that is raised when there are no chromosome set at a pair
    '''


class IncorrectTypeError(Exception):
    ''' an error that is raised when the input type is not according to the
    type contract that has been assigned to the method/function
    '''


class QueryError(Exception):
    ''' an error that is raised when the query is empty
    '''


class BinderError(Exception):
    ''' an error that occurs when the binder is empty i.e. it does not have a
    set chromosome
    '''


class MarkerError(Exception):
    ''' an error that is raised when a marker is assigned a chromosome before
    it has been set
    '''


class GenderError(Exception):
    ''' an error that is raised when the gender is not Male or Female
    '''


class Chromosome:
    ''' A class that represents chromosomes'''

    def __init__(self, nucleotides={}):
        ''' (Chromosome, dict) -> NoneType
        Returns None and initializes all variables that are needed for this
        class to compute its methods
        '''
        # initialize a dictionary that maps the pairs to chromosomes (as lists)
        # we will be updating this dictionary in other methods
        self._nucleotides = nucleotides
        # initialize a dictionary that will map a marker to the position that
        # has been entered
        self._markers = {}

    def __getitem__(self, position):
        ''' (Chromosome, int[, str]) -> list
        Returns the chromosome that has been set at the given position.
        If there is no position set, then it will create an empty list for that
        chromosome
        REQ: position can not be a negative number
        RAISES: IncorrectTypeError when position is not a string or an integer
        '''
        # check if position is a str. If so, then check if it is the marker
        # dictionary
        if (type(position) is str):
            # if it is not, then make a new key for that position and assign
            # it to an empty list (an unknown chromosome)
            if (position not in self._markers):
                self._markers[position] = []
            chromosome = self._markers[position]
        # else if the position is int and it is not in the nucleotides
        # dictionary then make a new key for
        # that position and assign it an empty list (an unknown chromosome)
        elif (type(position) is int):
            if (position not in self._nucleotides):
                self._nucleotides[position] = []
            chromosome = self._nucleotides[position]
        else:
            error = 'position can only be a string or an'
            raise IncorrectTypeError(error + ' intger')
        # return the chromosome
        return chromosome

    def set_by_pos(self, position, chromosome):
        ''' (Chromosome, int, str) -> NoneType
        Return None and sets the chromosome to the position given. If the
        position has been assigned before then the previous chromosome will be
        overwritten by the new chromosome i.e. the previous chromosome set will
        be lost
        REQ: chromosome should not be empty (ex: '' or ' ')
        REQ: position can not be negative
        '''
        # what I want is to make a position key that will map the chromosome to
        # that position key.
        # map the chromosome to the position that was entered by the user
        # convert the chromosome to a list so that we are able to mutate it
        # later on
        # check if the position is in the dictionary. If not, then make a new
        # key with that position and map the chromosome to that key
        if (position not in self._nucleotides):
            self._nucleotides[position] = list(chromosome)
        # if it does then append the chromosome to the dictionary
        # loop through the entire chromosome and append each letter into the
        # list
        else:
            # clear the previous elements out
            self._nucleotides[position].clear()
            # append the new chromosome into it
            for index in range(len(chromosome)):
                self._nucleotides[position].append(chromosome[index])
        # why use dictionary? because dictionaries are useful for the purpose
        # of keeping track of the items that we have stored. We can also very
        # easily find the chromosome by the key, which helps us in getting the
        # chromosome

    def get_by_pos(self, position):
        ''' (Chromosome, int) -> str
        Returns the chromosome that is set at that position. Raises a Position
        Error if the position is not set
        REQ: position can not be negative numbers
        REQ: position should have a set chromosome
        RAISES: PositionError when position does not have a set value
        '''
        # if the position (key) is in the dictionary/ has been mapped to a
        # chromosome, then store the chromosome
        if (position in self._nucleotides):
            chromosome = self._nucleotides[position]
        # otherwise raise a position error telling the user that their input
        # does not have a key error
        else:
            raise PositionError('position does not have a set value')
        # return the chromosome after converting it into a string
        return ''.join(chromosome)

    def set_marker(self, marker, position):
        ''' (Chromosome, str, int) -> NoneType
        Returns None and assigns marker to the position that has been entered.
        Note that this function only takes in a position, not pair and position
        REQ: position can not be a negative number
        REQ: marker should not be empty (ex: '' or ' ')
        '''
        # we want to link the marker to the position, such that when we
        # update the position with a chromosome, we also update the marker
        # with the same chromosome. This is why we stored our
        # chromosomes as lists, since they are mutatable.
        # storing the chromosome data in a variable (variable name credits to
        # google, our helpful mutual friend)
        # check if nucleotides has the position in it; if not then make a new
        # key of position and equal to an empty list (an unknown chromosome)
        # *insert dramatic music*
        if (position not in self._nucleotides):
            self._nucleotides[position] = []
        # get the chromosome that is stored at the position
        genetic_data = self._nucleotides[position]
        # and make the marker equal to the chromosome at that point
        self._markers[marker] = genetic_data

    def set_by_marker(self, marker, chromosome):
        ''' (Chromosome, str, str) -> NoneType
        Returns None and sets the marker to the chromosome. Note that this will
        also change the chromosome stored at the position that the marker has
        been linked before in set_marker
        REQ: chromosome or chromosome should not be empty (ex: '' or ' ')
        REQ: marker has to be set before it is assigned a chromosome
        RAISES: MarkerError when marker is called before assignment
        '''
        # check if the marker has been set before it is being assigned to a
        # chromosome. If yes,
        if (marker in self._markers):
            # map the list representation of the chromosome to the marker
            # get the list and see if it has any elements. If it does not, then
            # append it.
            if (len(self._markers[marker]) == 0):
                # loop through the chromosome and append each letter of the
                # chromosome into the list
                for index in range(len(chromosome)):
                    self._markers[marker].append(chromosome[index])
            # if it does, then delete all the elements and append the new
            # chromosome
            else:
                # delete all previous chromosome in it and then append the
                # new chromosome in it
                self._markers[marker].clear()
                # loop through the chromosome and append each letter of the
                # chromosome into the list
                for index in range(len(chromosome)):
                    self._markers[marker].append(chromosome[index])
        # if the marker is not set before it is being assigned to a chromosome
        else:
            # then raise an error to notify the user about the problem
            error = 'marker has to be set before it is assigned to'
            raise MarkerError(error + ' a chromosome')

    def get_by_marker(self, marker):
        ''' (Chromosome, str) -> str
        Returns a string representation of chromosome that has been set at
        marker. Will throw an error if the marker has not been set/assigned
        REQ: marker has to be assigned and set to a chromosome
        REQ: marker should not be empty (ex: '' or ' ')
        RAISES: MarkerError when marker does not have a chromosome assigned to
        it
        '''
        # initialize the chromosome
        chromosome = ''
        # check to see if the marker exists in the dictionary. it does
        if (marker in self._markers):
            # get the chromosome set there and use the join method to make
            # it into a string
            genetic_data = self._markers[marker]
            chromosome = ''.join(genetic_data)
        # if it doesn't then raise an error to alert the user about the marker
        # they have inputted
        else:
            error = 'marker does not have a chromosome assigned to'
            raise MarkerError(error + ' it yet')
        # return the chromosome
        return chromosome

    def get_nucleotides(self):
        ''' (Chromosome) -> dict
        returns the dictionary that maps the position to the chromosomes
        '''
        # return the dictionary that maps the nucleotides to its positions
        return self._nucleotides

    def get_markers(self):
        ''' (Chromosome) -> dict
        returns the dictionary that maps the markers to the chromosomes that
        have been entered
        '''
        # return the dictionary that maps the markers to the chromosomes
        return self._markers


class Cell:
    ''' this abstract class represents cells that have all basic functionality
    that is needed for this program to work'''

    def __init__(self):
        ''' (Cell) -> NoneType
        This class initializes all variables that are needed for this class
        to work
        '''
        # initializing any dictionaries that we will be needing to make
        # our methods work
        # for markers mapping to chromosomes
        self._store_marker = {}
        # for pairs mapping to chromosomes
        self._store_pair = {}

    def __getitem__(self, pair, position):
        ''' (Cell, int[, str], int) -> dict
        Returns the chromosome that is stored at pair in a dict form:
        {int: str}
        REQ: pair and position can not be negative numbers
        RAISES: IncorrectTypeError when position is not a string or integer
        '''
        # check if pair is a str. If so, then check if it is the marker
        # dictionary
        # if it is not, then raise an error because you can not access the
        # marker without first setting it
        if (type(pair) is str) and (pair not in self._store_marker):
                raise MarkerError('marker has not been set yet')
        # else if the position is int and it is not in the nucleotides
        # dictionary then make a new key for
        # check if it is a marker and has been mapped/linked to a chromosome
        elif (type(pair) is str) and (pair in self._store_marker):
            # get the chromosome set at the marker
            chromosome = self._store_marker[marker]
        # that position and assign it an empty list (an unknown chromosome)
        elif (type(pair) is int) and (pair not in self._store_pair):
            self._store_pair[pair] = self.set_by_pos(pair, position, '')
        # else check if type is int and has been paired with the chromosome
        elif (type(pair) is int) and (pair in self._store_pair):
            # get the chromosome at the pair and position
            chromosome = self._store_pair[pair][position]
        else:
            error = 'position can only be a string or an intger'
            raise IncorrectTypeError(error)
        # return the chromosome
        return chromosome

    def set_by_pos(self, pair, position, chromosome):
        ''' (Cell, int, int, str) -> NoneType
        Returns None and sets the pair-position to the chromosome
        REQ: pair and position can not be negative numbers
        REQ: chromosome should not be empty (ex: '' or ' ')
        '''
        # what I want is to map pair to a Chromosome obj
        # that can call the method set_by_pos in Chromosome
        # and map the Chromosome to the pos_num
        # therefore, create a Chromosome obj called genetic code
        # (shoutout to Google for the variable name) that can map the position
        # to the chromosome given as an input
        # create a Chromosome obj
        genetic_code = Chromosome()
        # call that obj to map the pos_num to the list version of chromosome
        genetic_code.set_by_pos(position, chromosome)
        # then map the Chromosome obj to pair_num. This will update the
        # dictionary
        self._store_pair[pair] = genetic_code.get_nucleotides()
        # Explaination of the data types chosen:
        # dictionaries because you can easily reference things to each other.
        # we also know that pos_num will be unique i.e. each chromosome will
        # have a unique pos_num
        # why convert the chromosome to a list? because lists are mutatable.
        # updating the list will update all IDs (memory #) where it has been
        # stored

    def get_by_pos(self, pair, position):
        ''' (Cell, int, int) -> str
        Returns the chromosome that is set at pair-position. Will throw an
        error if there is no chromosome assigned at pair or position.
        REQ: position and pair can not be negative numbers
        REQ: position and pair should have been mapped to a chromosome
        RAISES: PositionError when position does not have a chromosome set
        RAISES: PairError when pair does not have a chromosome set
        '''
        # check if the pair is in the dictionary. If it is,
        if (pair in self._store_pair):
            # check if the position is in the dictionary. If it is
            if (position in self._store_pair[pair]):
                # get the value and store it in the result
                chromosome = self._store_pair[pair][position]
            # if not present, then throw a position error saying that the
            # position is not defined
            else:
                error = 'the position does not have a chromosome'
                raise PositionError(error + ' set')
        # if it is not, then raise a Pair error saying that pair has not been
        # assigned a chromosome value
        else:
            raise PairError('the pair does not have a chromosome set')
        # return the chromosome
        return ''.join(chromosome)

    def get_markers_dict(self):
        ''' (Cell) -> dict
        Returns the dict which maps the markers to chromosomes.
        '''
        # return the dictionary which maps markers to chromosomes
        return self._store_marker

    def get_pairs_dict(self):
        ''' (Cell) -> dict
        Returns the dictionary which maps the pair-position to chromosomes
        '''
        # return the dictionary which maps markers to chromosomes
        return self._store_pair

    def set_marker(self, marker, pair, position):
        ''' (Cell, str, int, int) -> NoneType
        Returns None and links the marker to the chromosome at pair-position,
        such that changing one changes the other.
        REQ: marker can not be an empty string
        REQ: pair and position can not be negative numbers
        REQ: marker can not be repeated
        '''
        # we want to link the marker to the pair-position, such that when we
        # update the pair-position with a chromosome, we also update the marker
        # with exactly the same chromosome. This is why we stored our
        # chromosomes as lists, since they are mutatable.
        # storing the chromosome data in a variable (variable name credits to
        # google, our helpful mutual friend)
        # we first check if the pair is not in the dictionary so that we can
        # create one if we need to
        if (pair not in self._store_pair):
            # create a new pair by calling the method set_by_pos (cell class)
            # and set it to an empty str ('')
            Cell.set_by_pos(self, pair, position, '')
        # otherwise if pair is in the dictionary then
        elif (position not in self._store_pair[pair]):
            # check if the position is the dictionary too, if it is
            # if the position is not in the dictionary, make one and then
            # set it equal to the marker
            self._store_pair[pair][position] = []
        chromosome = self._store_pair[pair][position]
        # mapping that variable to marker, hence updating the dictionary
        self._store_marker[marker] = chromosome

    def set_by_marker(self, marker, chromosome):
        ''' (Cell, str, str) -> NoneType
        Returns None and sets the marker to the entered chromosome such that
        the pair-position it is paired to also updates. If marker is already
        set a value then it will overwrite the previous values. Will thow an
        error if marker is not linked to a pair-position before.
        REQ: marker and chromosome have to be of length one
        REQ: marker should be set before it is assigned a chromosome
        RAISES: MarkerError when marker is not linked to a pair-position before
        it is being set to a chromosome
        '''
        # check if the marker is in the dictionary, i.e it has been linked to
        # a pair-position before. If so,
        if (marker in self._store_marker):
            # get the contents of chromosome and check if the length of
            # chromosome is 0 (empty). If so
            if (len(self._store_marker[marker]) == 0):
                # then append all the input chromosome letters into the list
                # one at a time
                for index in range(len(chromosome)):
                    self._store_marker[marker].append(chromosome[index])
            # if it does have a previous chromosome in it, then clear all the
            # contents from the list and then append the new chromosome one
            # letter at a time
            else:
                self._store_marker[marker].clear()
                for index in range(len(chromosome)):
                    self._store_marker[marker].append(chromosome[index])
        # else give an error saying that the marker has not been set yet
        else:
            # since the message was very long, I split it into 2 pieces for
            # pep-8 sake
            error_message = 'marker has not been linked to a pair-position'
            raise MarkerError(error_message + ' chromosome')

    def get_by_marker(self, marker):
        ''' (Cell, str) -> str
        Returns the chromosome which is set at the marker. Will throw an error
        if the marker is called before assignment.
        REQ: marker can not be an empty string
        RAISES: MarkerError when marker is not linked to a pair-position before
        it is asked for a chromosome
        '''
        # initialize any variable we need
        chromosome = []
        # if the marker is in the dictionary, get the contents of it and store
        # it in a variable
        if (marker in self._store_marker):
            chromosome = self._store_marker[marker]
        # if the marker is not there, throw an error saying that the marker
        # has not been assigned a chromosome yet
        else:
            raise MarkerError('marker has not been assigned a chromosome yet')
        # return the result as a string. convert using join method
        return ''.join(chromosome)

    def get_chromosome(self, pair):
        ''' (Cell, int) -> dict
        Returns all the chromosomes that are set at the pair. Will throw an
        error if the pair is not defined
        REQ: pair has to be a positive number
        RAISES: ChromosomeError when pair does not have any chromosomes
        assigned to it
        '''
        # access the pair dictionary and see if the pair exists in the dict
        # if it does, get the all the chromosomes from there and store them in
        # a variable that will be returned later
        if (pair in self._store_pair):
            chromosome = self._store_pair[pair]
        # if it does not exist, throw an error saying that there are no
        # chromosomes set at that pair
        else:
            raise ChromosomeError('pair does not have any chromosomes set')
        # return the chromosome at the pair
        return chromosome

    def set_chromosome(self, pair, chromosome):
        ''' (Cell, int, dict) -> NoneType
        Sets chromosome to the pair and returns None.
        REQ: pair has to a positive number
        '''
        # what I want is to map the chromosome to the pair that has been given
        # we can do that easily by setting the dict key (pair) to chromosome
        # we have two cases to consider, however. 1- where the pair (key) does
        # not exist and 2- where the pair (key) exists. Our solution deals with
        # both the cases. Hence, with full steam ahead, writing the code
        self._store_pair[pair] = chromosome


class Binder(Cell):
    ''' a class that represents a binding chromosome which help decide which
    nucleotide comes from which parent.
    '''
    # setting genders for Male and Female
    MALE = 'M'
    FEMALE = 'F'

    def __init__(self):
        ''' (Binder) -> NoneType
        Returns None and initializes all variables that are needed to compute
        the class
        '''
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to pairs
        self._store_pair = {}
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to markers
        self._store_marker = {}
        # create a variable that stores the gender
        self._gender = ''

    def set_sex(self, gender):
        ''' (Binder, str) -> NoneType
        Returns None and sets the sex of the child to gender. Will throw an
        exception if it is not 'M' or 'F'
        REQ: gender can be {'M', 'F'}
        RAISES: GenderError when gender is not M or F
        '''
        # if the gender is either M or F then store the gender
        if (gender == Binder.MALE) or (gender == Binder.FEMALE):
            self._gender = gender
        # otherwise raise an error telling the user what issue is
        else:
            raise GenderError('gender can be either male(M) or female(F)')

    def get_sex(self):
        ''' (Binder) -> str
        Returns the sex of the child. Will throw an exception if gender hasn't
        been set.
        RAISES: GenderError when gender is not set yet
        '''
        # if the gender is an empty string then raise an exception saying that
        # the gender has not been set yet
        if (self._gender == ''):
            raise GenderError('gender has not been set yet')
        # otherwise return the gender that has been set
        return self._gender

    def __str__(self):
        ''' (Binder) -> str
        Returns the sex that has been set for this binder. If no sex is set,
        will return a sad face.
        '''
        # initialize sex as the gender of the binder
        sex = self._gender
        # check if gender is an empty string. If so, assign sex a sad face
        if (sex == ''):
            sex = ':('
        # make a string that has the binder name and gender of the binder
        info = 'This binder has its sex set as '
        # return that string
        return info + sex


class Query(Cell):
    ''' A class that represents a query obj which compares chromosomes to see
    if certain nucleotide patterns exist in them
    '''
    def __init__(self):
        ''' (Query) -> NoneType
        Initializes any variables that we will be needing to compute the class
        methods
        '''
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to pairs
        self._store_pair = {}
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to markers
        self._store_marker = {}


class Animal(Cell):
    ''' This class represents an animal
    '''
    def __init__(self, client_id):
        ''' (Animal, str) -> NoneType
        Returns None and initializes all variables that this class will need to
        be able to compute
        REQ: client_id should not be empty
        '''
        self._client_id = client_id
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to pairs
        self._store_pair = {}
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to markers
        self._store_marker = {}

    def get_client_id(self):
        '''(Animal) -> str
        Returns the client id
        '''
        # return the client id
        return self._client_id

    def set_client_id(self, client_id):
        '''(Animal, str) -> NoneType
        Returns a NoneType and resets client_id to the input client_id
        REQ: client_id can not be empty and has to be numeric
        '''
        # reset the client_id to the input client id
        self._client_id = client_id

    def test(self, query):
        ''' (Animal, Query) -> NoneType
        Returns None. This class does not do anything, since every animal has a
        different ways of being tested. This will be overwritten in other
        animal classes (such as birds and insects) where they will be tested
        according to their methods and DNA sequence.
        '''
        # this class does nothing but returns none
        return None

    def procreate(self, mate, binder):
        ''' (Animal, Animal, Binder) -> NoneType
        Returns None. This class does not do anything, since every animal has a
        different way of procreating. This will be overwritten in other
        animal classes (such as birds and insects) where they will procreate
        according to their genetic way
        '''
        # this class does nothing but returns none
        return None


class Human(Animal):
    ''' a class that represents a human'''
    TOTAL_PAIRS = 22

    def __init__(self, client_id):
        ''' (Human, str) -> NoneType
        Returns None and initializes all variables that are needed to compute
        this class
        REQ: client_id can not be empty
        '''
        # initialize client id using animal's init
        Animal.__init__(self, client_id)
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to pairs
        # loop 22 times to make 23 pairs of chromosomes for the human (b/c
        # humans have 23 chromosome pairs)
        for index in range(Human.TOTAL_PAIRS):
            self._store_pair[index] = Chromosome()
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to markers
        self._store_marker = {}
        # to map the memory nucleotides to the normal nucleotides
        self._memory_nucleotides = {}

    def procreate(self, mate, binder):
        ''' (Human, Human, Binder) -> Human
        Returns an object of type Human that has a pair of nucleotides
        constructed with the help of self and mate. If the binder is set using
        a marker then the child's chromosome will be set at the same marker
        which will be linked to 0-0
        REQ: mate and binder should have atleast one nucleotide pair
        REQ: binder should have a gender set
        RAISES: BinderError when binder does not have a set chromosome
        RAISES: GenderError when self is not Female and mate is not Male
        RAISES: ChromosomeError when binder's chromosome is not {'LM', 'RM'}
        '''
        # to make a child, we need the chromosomes and gender that binder has
        # since we don't know if the binder is set by marker or set by pair-
        # position, therefore we will check both. If both don't have any
        # chromosomes in it, then raise an error saying that binder does not
        # have a chromosome that can be assigned to the child.
        # checking if both don't have a chromosome set to it, if true
        if ((len(binder.get_pairs_dict()) == 0) and
           (len(binder.get_markers_dict()) == 0)):
            # raise an error
            raise BinderError('binder does not have a set chromosome')
        # else check if pair does not have a chromosome, if it doesn't
        elif (len(binder.get_pairs_dict()) == 0):
            # then get markers dictionary
            chromosome = binder.get_markers_dict()
        # if pair does have elements (failing the above to if statements) then
        # get the pairs dictionary
        else:
            chromosome = binder.get_pairs_dict()
        # now have our chromosome, let's get the gender of the child
        gender = binder.get_sex()
        # before creating a child, we will check if self is a female and mate
        # is a male, any other case will raise an error saying that only female
        # and male can procreate
        if (type(self) != Female and type(mate) != Male):
            raise GenderError('only Female can procreate with Male')

        # now that we know that self is Female and mate is Male, we can go
        # ahead and get the chromosome for the child
        # get the key from the binder's dictionary and store the chromosome it
        # has, mother's chromosome, father's chromosome and the key.
        # we can have a marker or an integer. therefore check if the key is
        # str. If it is get the chromosome directly.
        for pair in chromosome:
            if (type(pair) is str):
                child_pair = pair
                binder_chromosome = chromosome.get(pair, '')
                mother_chromosome = self.get_by_marker(pair)
                father_chromosome = mate.get_by_marker(pair)
            # else if the type is int, then get the second dictionary and loop
            # through that dictionary to get the chromosome. Store the things
            # that were mentioned before
            elif (type(pair) is int):
                child_pair = pair
                for position in chromosome[pair]:
                    child_position = position
                    binder_chromosome = chromosome.get(position, '')
                    mother_chromosome = self.get_by_pos(pair, position)
                    father_chromosome = mate.get_by_pos(pair, position)
        # we now have everything to make the child's chromosome.
        # if the binder's chromosome is 'RM' then take father's left nucleotide
        # and mother's right nucleotide to make the child's chromosome
        if (binder_chromosome == 'RM'):
            child_chromosome = father_chromosome[0] + mother_chromosome[-1]
        # else if it is 'LM' then take the father's right nucleotide and
        # mother's left nucleotide to make the child's chromosome
        elif (binder_chromosome == 'LM'):
            child_chromosome = mother_chromosome[0] + father_chromosome[-1]
        # else raise a Chromosome error saying that the binder's nucleotide can
        # be either 'LM' or 'RM'
        else:
            error = 'binder can have either LM or RM as its '
            raise ChromosomeError(error + 'chromosome')

        # id algorithm: the child also needs to have an id. Thought about this
        # and found this to be the most creative way of coming up with an id
        # length of the dictionary + length of the chromosome: 1st digit
        # length of the dictionary - length of chromosome: 2nd digit
        # length of the dictionary * length of chromosome: 3rd digit
        # length of the dictionary // length of chromosome: 4th digit
        # convert them all to string and concatenate them to get the id. Yay!
        # ps: tell me if you found a better solution. I thought on this aspect
        # for way too long, trying to think of unique ways of getting a unique
        # id for the child.
        first_digit = str(len(chromosome) + len(child_chromosome))
        second_digit = str(len(chromosome) - len(child_chromosome))
        third_digit = str(len(chromosome) * len(child_chromosome))
        fourth_digit = str(len(chromosome) // len(child_chromosome))
        child_id = first_digit + second_digit + third_digit + fourth_digit
        # now we have the child's nucleotides and id ready, we can make the
        # child based on the gender we have recieved.
        # if it is F, then make a Female child at the key of the binder and
        # set it's id as the one we derived
        if (gender == 'F'):
            child = Female(child_id)
            # check if the pair is a str. If it is, call set_marker and set the
            # marker at 0, 0
            if type(child_pair) is str:
                child.set_marker(child_pair, 0, 0)
                child.set_by_marker(child_pair, child_chromosome)
            # if it is int then call set by pos and set the child's nucleotide
            # to that position
            elif type(child_pair) is int:
                child.set_by_pos(child_pair, child_position, child_chromosome)
        # if it is M, then make a Male child at the key of the binder and set
        # its's id to the one we derived
        elif (gender == 'M'):
            child = Male(child_id)
            # check if the pair is a str. If it is, call set_marker and set the
            # marker at 0, 0
            if type(child_pair) is str:
                child.set_marker(child_pair, 0, 0)
                child.set_by_marker(child_pair, child_chromosome)
            # if it is int then call set by pos and set the child's nucleotide
            # to that position
            elif type(child_pair) is int:
                child.set_by_pos(child_pair, child_position, child_chromosome)
        # return the child
        return child

    def test(self, query):
        ''' (Human, Query) -> bool
        Returns True if all the nucleotides in query are comparable to self's
        nucleotides. Returns False if:
        - self's nucleotide isn't equal to query's nucleotides
        - memory nucleotides (0-9) are not the same throughout
        - if the male sex chromosome is unknown i.e. it does not any
        information set to it
        REQ: query should have at least one nucleotide pair
        RAISES: QueryError when the query is empty
        '''
        # a query can be accepted in many ways but rejected in only a 3 ways
        # listed in docstrings. Thus, we want to check if any those conditions
        # fail. If they don't we accept the query, otherwise reject it.
        # get the pair and marker dictionary and see if both of them don't have
        # any elements. If they don't, then throw an exception
        if (len(query.get_pairs_dict() == 0) and
           len(query.get_markers_dict()) == 0):
            raise QueryError('can not compare an empty query')
        # we now know that either one of them is not empty, with that we can
        # figure out which one is and get our non-empty dictionary
        # check if get_pair is empty, if it is then get the marker dictionary
        elif(len(query.get_pair_dict()) == 0):
            genetic_code = query.get_markers_dict()
        # if get pair is not empty, then get that dictionary
        else:
            genetic_code = query.get_pairs_dict()
        # initialize a variable that will change if any one of the condition
        # is false
        is_valid = True
        # make an empty list for the keys
        keys = []
        # get all the keys from the dictionary we got
        for pair in genetic_code:
            # append the pair to keys. we will then loop through the keys in
            # our while loop to see if the chromosomes at that key match
            keys.append(pair)
        # set index to be 0
        index = 0
        while (not is_valid) and index < len(keys):
            # since we don't know which dict got returned, therefore we will
            # have to check for both possibilities.
            # check if the type is str, if true
            if type(key[index]) is str:
                # then get the chromosome at that marker in query and self
                # check if they're the same by comparing each index to the
                # other
                query_chromosome = query.get_by_marker(key[index])
                human_chromosome = self.get_by_marker(key[index])
                for count in range(len(query_chromosome)):
                    # check if the index is a digit and has been mapped
                    # in the memory nucleotide dict. If it has, the pop that
                    # element and insert the normal nucleotide into the list
                    if (query_chromosome[count].isdigit() and
                       query_chromosome[count] in self._memory_nucleotide):
                        query_chromosome.pop[index]
                        nucleotide = self._memory_nucleotides[
                            query_chromosome[count]
                        ]
                        query_chromosome.insert(count, nucleotide)
                    elif (human_chromosome[count].isdigit() and
                          human_chromosome[count] in self._memory_nucleotide):
                        human_chromosome.pop[count]
                        nucleotide = self._memory_nucleotides[
                                        human_chromosome[count]
                                     ]
                        human_chromosome.insert(index, nucleotide)
                    # check if the character is a digit; if it is, then map
                    # it to the nucleotide it is being compared against.
                    if (query_chromosome[count].isdigit()):
                        self._memory_nucleotides[query_chromosome[count]] = \
                            human_chromosome[count]
                    elif (human_chromosome[count].isdigit()):
                        self._memory_nucleotides[human_chromosome[count]] = \
                            query_chromosome[count]
                    # comparing it with each nucleotide in human chromosome
                    # if any one of them is not, then make is_valid False
                    if human_chromosome[count] != query_chromosome[count]:
                        is_valid = False
            # check if the type is int
            elif type(key[index]) is int:
                # then get the dictionary at the position and then get the
                # chromosome at that position. Do the same to get human's
                # chromosome
                for position in query[key[index]]:
                    query_chromosome = query.get_by_pos(key[index], position)
                    human_chromosome = self.get_by_pos(key[index], position)
                # we know have the human and query chromosomes, let's see if
                # they are comparable
                # check if the pair is 23, the instance is male
                if (key[index] == 23) and (type(self).__name__ == Male) and \
                   (human_chromosome == ''):
                    # and the chromosome at that point is unknown (empty).
                    # If it is then make is_valid false.
                    is_valid = False
                else:
                    for count in range(len(query_chromosome)):
                        # if the previous condition is false, then check if the
                        # character is a digit and has been mapped
                        # in the memory nucleotide dict. If it has, the pop
                        # that element and insert the normal nucleotide into
                        # the list
                        if (query_chromosome[count].isdigit() and
                           query_chromosome[count] in self._memory_nucleotide):
                            query_chromosome.pop[index]
                            nucleotide = self._memory_nucleotides[
                                    query_chromosome[count]
                                ]
                            query_chromosome.insert(count, nucleotide)
                        # do the same for human_chromosomes
                        elif (human_chromosome[count].isdigit() and
                              human_chromosome[count] in
                              self._memory_nucleotide):
                            human_chromosome.pop[count]
                            nucleotide = self._memory_nucleotides[
                                    human_chromosome[count]
                                 ]
                            human_chromosome.insert(index, nucleotide)
                        # check if the character is a digit; if it is, then map
                        # it to the nucleotide it is being compared against.
                        if (query_chromosome[count].isdigit()):
                            self._memory_nucleotides[query_chromosome[count]] \
                                = human_chromosome[count]
                        elif (human_chromosome[count].isdigit()):
                            self._memory_nucleotides[human_chromosome[count]] \
                                = query_chromosome[count]
                        # comparing it with each nucleotide in human chromosome
                        # if any one of them is not, then make is_valid False
                        if human_chromosome[count] != query_chromosome[count]:
                            is_valid = False
        index += 1
        return is_valid

    def __str__(self):
        ''' (Human) -> str
        Returns the instance of the object and the client id
        '''
        # make a string with the result that will be displayed when the
        # object is printed
        result = 'I am  a' + type(self).__name__ + 'with client id '
        # return the string
        return result + self._client_id


class Male(Human):
    ''' a class that represents a Male Human'''

    def __init__(self, client_id):
        ''' (Male, str) -> NoneType
        Returns None and initializes all variables that are needed to compute
        this class
        REQ: client_id can not be empty
        '''
        # initialize using client id Human's init
        Human.__init__(self, client_id)
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to pairs
        # loop 22 times to make 23 pairs of chromosomes for the human (b/c
        # humans have 23 chromosome pairs~ the handout)
        for index in range(Human.TOTAL_PAIRS):
            self._store_pair[index] = Chromosome()
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to markers
        self._store_marker = {}


class Female(Human):
    ''' a class that represents a Female Human'''

    def __init__(self, client_id):
        ''' (Female, str) -> NoneType
        Returns None and initializes all variables that are needed to compute
        this class
        REQ: client_id can not be empty
        '''
        # initialize using client id Human's init
        Human.__init__(self, client_id)
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to pairs
        # loop 22 times to make 23 pairs of chromosomes for the human (b/c
        # humans have 23 chromosome pairs)
        for index in range(Human.TOTAL_PAIRS):
            self._store_pair[index] = Chromosome()
        # create an empty dictionary that keeps track of all the chromosomes
        # mapped to markers
        self._store_marker = {}

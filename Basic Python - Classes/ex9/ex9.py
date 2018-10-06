import math


class Parallelogram():
    ''' A class that represents a parallelogram'''

    def __init__(self, base, side, theta):
        ''' (Parallelogram, float, float, float) -> NoneType
        Returns None and stores all the input parameters as class variables
        REQ: base, side and theta cannot be negative numbers
        REQ: theta has to be in degrees
        '''
        # set the input parameters as class variables
        self._base = base
        self._side = side
        self._angle = theta
        self._name = 'Parallelogram'

    def get_base(self):
        ''' (Parallelogram) -> float
        Returns the base of the shape
        '''
        # return the base length of the shape
        return self._base

    def get_side(self):
        ''' (Parallelogram) -> float
        Returns the side of the shape
        '''
        # return the side length of the shape
        return self._side

    def get_angle(self):
        ''' (Parallelogram) -> float
        Returns the angle of the shape
        '''
        # return the angle of the shape
        return self._angle

    def __str__(self):
        ''' (Parallelogram) -> str
        Returns a string that tells the user about the shape and its area
        '''
        # return the name of the shape along with the area (how name?)
        string = 'I am a ' + self._name + ' with area ' + str(self.area())
        return string

    def area(self):
        ''' (Parallelogram) -> float
        Returns the area of the shape
        '''
        # convert the angle into radian degrees
        radian_angle = math.radians(self._angle)
        # compute the area of the shape
        area = self._base * self._side * math.sin(radian_angle)
        # return the area
        return area

    def bst(self):
        ''' (Parallelogram) -> list of float
        Returns a list of float that has the base, side and angle of the shape
        in that order
        '''
        # Return the base, side and angle
        return [self._base, self._side, self._angle]


class Rectangle(Parallelogram):
    ''' A class that represents a rectangle '''
    def __init__(self, base, side):
        ''' (Rectangle, float, float) -> NoneType
        Returns None and stores all the input parameters as class variables
        REQ: base and side cannot be negative values
        '''
        Parallelogram.__init__(self, base, side, 90)
        self._name = "Rectangle"


class Rhombus(Parallelogram):
    '''A class that represents a rhombus'''
    def __init__(self, base, theta):
        ''' (Square, float) -> NoneType
        Returns None and stores all the input parameters as class variables
        REQ: side cannot be negative values
        '''
        Parallelogram.__init__(self, base, base, theta)
        self._name = 'Rhombus'


class Square(Rhombus, Rectangle):
    ''' A class that represents a square'''
    def __init__(self, side):
        ''' (Square, float) -> NoneType
        Returns None and stores all the input parameters as class variables
        REQ: side cannot be negative values
        '''
        Rhombus.__init__(self, side, 90)
        Rectangle.__init__(self, side, side)
        self._name = 'Square'

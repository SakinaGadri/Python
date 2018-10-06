def percent_to_gpv(percent_mark):
    ''' (int) -> float
    Returns the grade point value (gpv) for the input percent_mark
    REQ: percent_mark >=0
    REQ: percent_mark <=100
    >>> percent_to_gpv(0)
    0.0
    >>> percent_to_gpv(52)
    0.7
    >>> percent_to_gpv(56)
    1.0
    >>> percent_to_gpv(59)
    1.3
    >>> percent_to_gpv(62)
    1.7
    >>> percent_to_gpv(66)
    2.0
    >>> percent_to_gpv(69)
    2.3
    >>> percent_to_gpv(71)
    2.7
    >>> percent_to_gpv(73)
    3.0
    >>> percent_to_gpv(79)
    3.3
    >>> percent_to_gpv(84)
    3.7
    >>> percent_to_gpv(89)
    4.0
    >>> percent_to_gpv(100)
    4.0
    '''
    # initialize grade_point_value
    grade_point_value = 0.0
    # return the grade_point_value of the input percent_mark
    if (100 <= percent_mark or percent_mark >= 90):
        grade_point_value = 4.0
    elif (89 <= percent_mark or percent_mark >= 85):
        grade_point_value = 4.0
    elif (84 <= percent_mark or percent_mark >= 80):
        grade_point_value = 3.7
    elif (79 <= percent_mark or percent_mark >= 77):
        grade_point_value = 3.3
    elif (76 <= percent_mark or percent_mark >= 73):
        grade_point_value = 3.0
    elif (72 <= percent_mark or percent_mark >= 70):
        grade_point_value = 2.7
    elif (69 <= percent_mark or percent_mark >= 67):
        grade_point_value = 2.3
    elif (66 <= percent_mark or percent_mark >= 63):
        grade_point_value = 2.0
    elif (62 <= percent_mark or percent_mark >= 60):
        grade_point_value = 1.7
    elif (59 <= percent_mark or percent_mark >= 57):
        grade_point_value = 1.3
    elif (56 <= percent_mark or percent_mark >= 53):
        grade_point_value = 1.0
    elif (52 <= percent_mark or percent_mark >= 50):
        grade_point_value = 0.7
    elif (49 <= percent_mark or percent_mark >= 0):
        grade_point_value = 0.0
    return (grade_point_value)


def card_namer(card_value, card_suit):
    ''' (str, str) -> str
    Returns the full name of the card based on card_value and card_suit
    REQ: card_value and card_suit must be a single character
    >>> card_namer("A", "C")
    'Ace of Clubs'
    >>> card_namer("8", "H")
    '8 of Hearts'
    >>> card_namer('9', 'R')
    'CHEATER!'
    '''
    # initialize return_value and return_suit
    return_value = ""
    return_suit = ""
    # compare card_value and return the corresponding output
    if (card_value == 'A'):
        return_value = 'Ace of '
    elif (card_value == 'T'):
        return_value = '10 of '
    elif (card_value == 'J'):
        return_value = 'Jack of '
    elif (card_value == 'Q'):
        return_value = 'Queen of '
    elif (card_value == 'K'):
        return_value = 'King of '
    elif (card_value in ('2', '3', '4', '5', '6', '7', '8', '9')):
        return_value = (card_value + " of ")
    # compare card_suit and return a corresponding output or return 'CHEATER!'
    if (card_suit == 'D'):
        return_suit = 'Diamonds'
    elif (card_suit == 'C'):
        return_suit = 'Clubs'
    elif (card_suit == 'H'):
        return_suit = 'Hearts'
    elif (card_suit == 'S'):
        return_suit = 'Spades'
    else:
        return_suit = 'CHEATER!'
        return_value = ''
    return (return_value + return_suit)

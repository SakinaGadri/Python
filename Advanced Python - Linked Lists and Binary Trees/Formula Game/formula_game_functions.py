"""
# Copyright Nick Cheng, 2016, 2018
# Copyright Sakina Shabbir Gadriwala, 2018
# Student Number: 1004351051
# UTORid: gadriwa1
# Date of Submission: March 24th, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment.


def find_root(formula):
    ''' (str) -> int
    Returns where the index of the root is in the formula
    REQ: len(formula) >= 2
    >>> find_root('(a+b)')
    2
    >>> find_root('-a')
    0
    >>> find_root('a!b')
    None
    >>> find_root('(((a+b)+c)*c)')
    10
    '''
    # make a counter to loop through the string, another counter to keep track
    # of the brackets and a boolean variable that will exit the loop once
    # you find the root
    counter_str = 0
    counter_bracket = 0
    is_root = False
    index_root = None
    # make a while loop that checks if the root has been found and if we're
    # still in the string so that we don't get an index error. Also check
    # if the formula is starting with an open bracket or a negation sign. If
    # it does not, then either the formula is invalid or there is no root
    # in the formula (a leaf), therefore we return none
    while (counter_str < len(formula)) and (not is_root) and \
          (formula.startswith('(') or formula.startswith('-')):
        # check if the bracket is an open bracket, then add one to the
        # bracket counter
        if (formula[counter_str] == '('):
            counter_bracket += 1
        # check if the bracket is a closing bracket, then subtract one from
        # the closing counter
        elif (formula[counter_str] == ')'):
            counter_bracket -= 1
        # if the bracket counter is 1 (meaning we are in between the two
        # brackets) and the character in the string at the index
        # is either * or a +, then make the bool var true and make the index of
        # the root be the str counter
        elif (counter_bracket == 1) and (formula[counter_str] in ['*', '+']):
            is_root = True
            index_root = counter_str
        # else if its a not and counter brackets is 0 i.e. the Not is at the
        # starting of the string
        elif (counter_bracket == 0) and (formula[counter_str] == '-'):
            # then make the str counter equal to your root index and make the
            # bool variable True
            is_root = True
            index_root = counter_str
        # add one to the counter of the str every time to move forward
        counter_str += 1
    # return the index
    return index_root


def subtree_helper(formula):
    ''' (str, int) -> FormulaTree
    Returns the FormulaTree built for the formula <formula>
    REQ: length of the formula >= 1
    >>> subtree = subtree_helper('(a+b)')
    >>> print(subtree)
    'OrTree(Leaf('a'), Leaf('b'))'
    >>> subtree = subtree_helper('(-a)')
    >>> print(subtree)
    None
    >>> subtree = subtree_helper('(((a+b)+c)*c)')
    >>> print(subtree)
    AndTree(OrTree(OrTree(Leaf('a'), Leaf('b')), Leaf('c')), Leaf('c'))
    '''
    # initialize your tree as none
    tree = None
    # 4 base cases:
    # 1- if the formula length is 0
    if (len(formula) == 0):
        tree = None
    # 2- check if its a just a variable (and lower case). If it is, then make
    # that into a leaf
    elif (len(formula) == 1) and (formula[0].isalpha()) and \
         (formula[0].islower()):
        tree = Leaf(formula[0])
    # 3- if the formula doesn't start with a bracket or a
    # not operator (and isn't alpha + lower case either -> checked that in the
    # previous condition) then the tree is invalid -> return none
    elif not (formula.startswith('(') or formula.startswith('-')):
        tree = None
    # 4- check if its a negator. If it is, make a not tree and send the rest of
    # the string as a recursive call
    elif(formula[0] == '-'):
        # make the child of the Not Tree
        child = subtree_helper(formula[1:])
        # if the child is a valid formula, then make a Not tree, else make the
        # tree None since the child is an invalid sub tree
        if child:
            tree = NotTree(child)
        # else the child is invalid, therefore the whole tree becomes invalid
        else:
            tree = None
    # else if it starts with an open bracket and ends with a closed bracket
    # then we have an AND tree or an OR tree
    elif (formula[0] == '(') and (formula[-1] == ')'):
        # then find the root of the tree (find root checks if we have a valid
        # root, otherwise would return none)
        root_index = find_root(formula)
        # if the root exists in the formula
        if (root_index is not None):
            # then make the left sub tree by making a recursive call on
            # everything from the left +1 (not including the bracket) to the
            # root
            left_subtree = subtree_helper(formula[1:root_index])
            # similarly, make the right sub tree by making a recursive call on
            # everything from one character after the root till one index
            # before the string ends (we don't want the bracket, because it
            # will make the child invalid)
            right_subtree = subtree_helper(formula[root_index + 1:-1])
            # check if the sub trees are valid sub trees, if they are then
            if (left_subtree and right_subtree):
                # (finally!) make the tree. If the root is a + sign make an OR
                # tree using the subtrees we have made
                if (formula[root_index] == '+'):
                    tree = OrTree(left_subtree, right_subtree)
                # else if its a * sign make an add tree using the sub trees we
                # have made
                elif (formula[root_index] == '*'):
                    tree = AndTree(left_subtree, right_subtree)
                # if its neither (and we handled the case where we have -) then
                # the tree is invalid because of an invalid symbol or placing
                # an valid symbol some where wrong.
                # therefore the whole tree becomes invalid/none
                else:
                    tree = None
            # else the left and right sub trees are not valid sub trees. hence
            # making the entire tree invalid (aka none)
            else:
                tree = None
        # if the root does not exist, then there is no tree to make. Hence the
        # tree becomes none
        else:
            tree = None
    # else, the string is too complicated! just leave it as it is, and hope the
    # marker figures it out, lol
    # jk
    # else, the string is complicated.
    else:
        # so your find the root of the formula and split it from there.
        root_index = find_root(formula)
        # if there is a root in the formula
        if (root_index is not None):
            # make a recursive call on everything left from the root and
            left_subtree = subtree_helper(formula[:root_index])
            # make a recursive call on everything from the right of the root
            right_subtree = subtree_helper(formula[root_index+1:])
            # if the left and right sub trees are valid
            if (left_subtree and right_subtree):
                # then make the tree based on the root
                # if it is a +, then make an or tree
                if (formula[root_index] == '+'):
                    tree = OrTree(left_subtree, right_subtree)
                # else if its a *, then make an and tree
                elif(formula[root_index] == '*'):
                    tree = AndTree(left_subtree, right_subtree)
                # else the operator is invalid, hence making the entire tree
                # invalid/None
                else:
                    tree = None
            # else the left or right subtrees are invalid -> the whole tree is
            # invalid
            else:
                tree = None
        # if the root does not exist, then there is no tree to make. Hence the
        # tree becomes none
        else:
            tree = None
    # return the tree
    return tree


def build_tree(formula):
    ''' (str) -> FormulaTree
    Returns True if the <formula> is valid. Else returns False.
    How is a formula valid?
    > all the variable names should be lower case
    > there can be only be 26 unique varaibles, aka the total number of
    alphabets in english language
    > the only valid operators are the AND ('*'), the NOT ('-') and the
    OR ('+') operator.
    > when using the AND ('*') and OR ('+') operator, it is necessary to use
    parentheses. e.g. '(x*y)' is a valid formula, but 'x*y' is not a valid
    formula because it is missing parentheses
    > Parentheses are not needed when using the NOT ('-') operator. e.g. '-x'
    is a valid formula, but '-(x)' is not a valid formula because it has
    extraneous brackets
    > the simplest formula is of a string containing just one variable. e.g.
    'x' is the simplest formula
    Any formula that does not follow the above rules is an invalid formula
    REQ: <formula> can not be an empty string
    REQ: <formula> only has symbols '*', '-', '+' and all the lower case
    letters from a - z
    >>> build_tree('-x')
    NotTree(Leaf('x'))
    >>> build_tree('-(x)')
    None
    >>> build_tree('-(x*y)')
    NotTree(AndTree(Leaf('x'), Leaf('y')))
    >>> build_tree('x*y')
    None
    >>> build_tree('x')
    Leaf('x')
    '''
    # initialize an empty tree
    tree = None
    # find the root using the root helper function
    root_index = find_root(formula)
    # if the root exists,
    if root_index is not None:
        # then see if the root is an OR operator
        if (formula[root_index] == '+'):
            # make the left sub tree (everything from the start to one index
            # before the root
            left_tree = subtree_helper(formula[1:root_index])
            # make the right subtree (everything from one index after the root
            # to the end)
            right_tree = subtree_helper(formula[root_index + 1:-1])
            # if the left sub tree or the right sub tree is not empty (meaning
            # its not invalid), then make an OR tree
            if (left_tree and right_tree):
                tree = OrTree(left_tree, right_tree)
            # else, left sub tree or right sub tree is invalid and therefore
            # makes the entire tree invalid. Hence the tree is none
            else:
                tree = None
        # else check if the root is an AND operator
        elif (formula[root_index] == '*'):
            # make the left sub tree (everything from the start to one index
            # before the root
            left_tree = subtree_helper(formula[1:root_index])
            # make the right subtree (everything from one index after the root
            # to the end)
            right_tree = subtree_helper(formula[root_index + 1:-1])
            # if the left sub tree or the right sub tree is not empty (meaning
            # its not invalid), then make an OR tree
            if (left_tree and right_tree):
                tree = AndTree(left_tree, right_tree)
            # else, left sub tree or right sub tree is invalid and therefore
            # makes the entire tree invalid. Hence the tree is none
            else:
                tree = None
        # else if the root is a NOT operator
        elif (formula[root_index] == '-'):
            # make the sub tree (everything from the root_index + 1 to the end
            # since not only has one child/ excluding the not operator)
            child = subtree_helper(formula[root_index + 1:])
            # if the child is a valid tree
            if child:
                # then make a Not tree
                tree = NotTree(child)
            # else, the child is not valid, making the whole tree invalid/none
            else:
                tree = None
        # if the operator is not from +, -, *, then the operator is invalid
        # making the entire tree invalid
        else:
            tree = None
    # else if the str a lower case alphabet of len 1, then make it into a leaf
    # and return that as a tree
    elif (len(formula) == 1) and (formula.isalpha()) and (formula.islower()):
        tree = Leaf(formula)
    # else if the root does not exist, then the tree is invalid
    else:
        tree = None
    # return the tree that was built (or built but destroyed by the multiple
    # checks, oof!)
    return tree
print(build_tree('((x*y))'))

def help_draw_tree(root, depth):
    ''' (FormulaTree, int) -> str
    Returns a string representation of the <root> in the following format:
    > to see the root at the top, we need to rotate it 90 degrees
    > we draw them without lines/ arrows between the child and parent
    > in Python, child of the root will be indented 2 spaces and children of
    the child will be indented 4 spaces, and so on
    REQ: <root> can not be empty, i.e. the tree should at least have one
    element in it
    REQ: <root> is a valid formula
    REQ: <depth> >= 1
    >>> help_draw_tree(NotTree(OrTree(Leaf('x'), AndTree(Leaf('y'), \
    Leaf('y')))))
    '-
      +
        * y
          x
        x'
    >>> help_draw_tree(OrTree(Leaf('x'), Leaf('y')))
    '+ y
      x'
    '''
    # according to the guidelines provided to us in the handout, we see that
    # we read the root first, then the right child and then the left child
    # we can do that by accessing the get children method provided to us
    # so as long as the root is not empty, we will access the root, then the
    # right child and then the left child.
    # starting by initializing the result string
    result = ''
    # base cases: if the tree is empty or if the tree has one node. One node
    # can only exist if its a Leaf, so we check that
    # first base case: if the tree is empty
    if (root is None):
        # then the result should be an empty string
        result = ''
    # second base case: if there is one node in the tree
    elif (isinstance(root, Leaf)):
        # then the result should include the symbol/char that the node is
        # holding
        result = root.get_symbol()
    # else the tree has more than one node
    # check if the node is an + tree or * tree. If it is
    elif (isinstance(root, AndTree) or isinstance(root, OrTree)):
        # then add one to the depth
        depth += 1
        # get the left and right child. We know that get children returns us
        # a list. the syntax used below assigns the 0th element of the list
        # to first variable and the 1st element of the list to the 2nd var
        # here, the 0th element is the left child of the AND/OR tree and the
        # 1st element is the right child of the tree
        left, right = root.get_children()
        # get the character the root is holding using one of the getters
        symbol = root.get_symbol()
        # add the everything to get the result. By the guidelines provided to
        # us we know that the symbol comes first followed by a space and then
        # the right child. The left child goes on to a different row but stays
        # in the same column as the right child, therefore we add 2 spaces
        # before the left child. We multiply it with the depth of the tree
        # because if the depth is 1, then we only want one set of 2spaces
        # before it. If the depth is n, then we want n set of 2spaces before
        # the left child
        # since the left and child can be different sub trees on their own, we
        # make a recursive call on them
        result += symbol + ' ' + help_draw_tree(right, depth) + '\n' +\
            ('  ' * depth) + help_draw_tree(left, depth)
    # else check if the node is - tree. if it is,
    elif (isinstance(root, NotTree)):
        # increase the depth by 1
        depth += 1
        # get the child. Since we know that Not only has one child and get
        # children retruns a list of all the children. We want the child to
        # be the 0th element of the list, hence we get the list of children (in
        # this case, the len will always be 1, because not only has one child)
        # and access the 0th element of the list, hence the list notation
        child = root.get_children()[0]
        # get the character that the root is holding using one of the getters
        symbol = root.get_symbol()
        # same guidelines used here: the root's symbol and then the child
        # since the child can be an entire sub tree on its own, we make a
        # recursive call on it using the new depth and the child of the not
        # tree
        result += symbol + ' ' + help_draw_tree(child, depth)
    # return the string which holds the tree
    return result


def draw_formula_tree(root):
    ''' (FormulaTree) -> str
    Returns a string representation of the <root> in the following format:
    > to see the root at the top, we need to rotate it 90 degrees
    > we draw them without lines/ arrows between the child and parent
    > in Python, child of the root will be indented 2 spaces and children of
    the child will be indented 4 spaces, and so on
    REQ: <root> can not be empty, i.e. the tree should at least have one
    element in it
    REQ: <root> is a valid formula
    >>> draw_formula_tree(NotTree(OrTree(Leaf('x'), AndTree(Leaf('y'), \
    Leaf('y')))))
    '- + * y
        y
      x'
    >>> draw_formula_tree(OrTree(Leaf('x'), Leaf('y')))
    '+ y
      x'
    '''
    # call the helper method that will help build the formula tree
    # for simplicity sake, we assume that the depth of our tree is 0 and pass
    # that in as a param for the helper function
    tree = help_draw_tree(root, 0)
    # return that tree
    return tree


def evaluate(root, variables, values):
    '''(FormulaTree, str, str) -> int
    Returns a int that represents the truth value of the formula rooted at
    <root>, containing the variables <variables>, each having the value in
    <values>, respectively
    1 means True and 0 means False
    How the function evaluates each of the following?
    And: Evaluates 1 if both F1 and F2 have truth values 1, else evaluates 0
    Or: Evaluates 1 if either F1 or F2 have truth values 1, else evaluates 0
    Not: Evaluates 0 if F1 has the truth value of 1, and vice-versa
    REQ: <variables> have to lower case
    REQ: <values> can only consist of 0's and 1's
    REQ: <root> should not be empty
    REQ: number of <values> should be equal to number of <variables>
    REQ: <root> should have all the variables within <variables>
    >>> tree = OrTree(Leaf('x'), Leaf('y'))
    >>> evaluate(tree, 'xy', '10')
    1
    >>> tree = NotTree(AndTree(Leaf('x'), OrTree(Leaf('y'), NotTree(Leaf('z'))\
    )))
    >>> evaluate(tree, 'xyz', '111')
    0
    '''
    # initializing final answer as None
    fin_value = None
    # doing this with recursion
    # base case: if the root is a leaf, then get the corresponding value
    # of the variable from the variable string and store it in the variable
    if (isinstance(root, Leaf)):
        # get the symbol from the leaf node
        element = root.get_symbol()
        # now find the index of that element in the variable str
        ele_index = variables.find(element)
        # get the corresponding value of that element
        corr_value = values[ele_index]
        # make the corresponding value the final result of the leaf after
        # converting it into an int
        fin_value = int(corr_value)
    # else if it is a Not sign, then get the child and call evaluate on the
    # child. get the final result by subtracting one from the final result
    # (by the rules defined in the handout)
    elif (isinstance(root, NotTree)):
        # get the child of the tree. Since get_children returns us a list and
        # the not child is stored at the 0th element of the list, we access it
        # using the list notation
        child = root.get_children()[0]
        # evaluating the child's sub-tree, by the rules defined in the handout
        fin_value = 1 - evaluate(child, variables, values)
    # else if it an Or tree, then get the left and right child and call
    # evaluate on it. get the final answer using the max of the either left
    # and right sub tree (by the rules defined in the handout)
    elif (isinstance(root, OrTree)):
        # get the left subtree and right subtree of the tree
        left, right = root.get_children()
        # make the recursive call on the left and right sub trees
        left_value = evaluate(left, variables, values)
        right_value = evaluate(right, variables, values)
        # find the max of the either and make the that the final answer
        fin_value = max(left_value, right_value)
    # else if it is an and tree, then get the left and right child and call
    # evaluate on it. get the final answer using the min of the left
    # and right sub tree (by the rules defined in the handout)
    elif (isinstance(root, AndTree)):
        # get the left subtree and right subtree of the tree
        left, right = root.get_children()
        # make the recursive call on the left and right sub trees
        left_value = evaluate(left, variables, values)
        right_value = evaluate(right, variables, values)
        # find the min of the either and make the that the final answer
        fin_value = min(left_value, right_value)
    # return the final value
    return fin_value


def possible_solutions(variables):
    ''' (str) -> list of str
    Returns all possible values that variables can hold.
    All possible values only include 0's and 1's. The len of the output can be
    calculated as (2^{len(variables)})
    REQ: len(variables) >= 0
    >>> possible_solutions('abc')
    ['111', '011', '101', '001', '110', '010', '100', '000']
    >>> possible_solutions('ab')
    ['11', '01', '10', '00']
    '''
    # will do this recursively, woho!
    # initialize an empty list that will store all the perms we come up with
    possible_moves = []
    # base case: when the length of our variables is 1
    if (len(variables) == 1):
        # then the possible values that one var can hold is 1 and 0.
        # make them a string
        # append them to the list
        possible_moves.append(str(1))
        possible_moves.append(str(0))
    # else the input size is greater than 1
    else:
        # so we make a recursive call on the variables
        # assume we assigned a value to the first variable; make a recursive
        # call on the rest of the list
        first_call = possible_solutions(variables[1:])
        # once we get that back, loop through the list and add the value we
        # assigned (1 and 0) to each element of the list. append the
        # new value in it. Make the assigned value into a str
        for soln in first_call:
            possible_moves.append(str(1) + soln)
            possible_moves.append(str(0) + soln)
    # return the list
    return possible_moves


def helper_evaluator(root, variables, values, turns, assigned_value):
    ''' (FormulaTree, str, str, str, str) -> bool
    Returns the move that will lead to a win for the given formula at <root>
    with the given <variables>, <turns> and <assigned_value>
    REQ: <root> can not be empty, i.e. it should have at least one node
    REQ: <root> should have all the variables that <variables> contains
    REQ: <variables> should be lower case and be in <root>
    REQ: <values> should only consist of 1's and 0's
    REQ: <turns> should only consist of E's and A's
    REQ: <assigned_value> can be either 0 or 1
    REQ: number of <variables> should be equal to number of <turns>
    REQ: len(turns/variables) > len(values) i.e. there must be a next move
    >>> root = AndTree(Leaf('x'), Leaf('y'))
    >>> helper_evaluator(root, 'xy', '', 'EA', '1')
    False
    >>> root = OrTree(Leaf('x'), Leaf('y'))
    >>> helper_evaluator(root, 'xy', '', 'EA', '1')
    True
    >>> root = AndTree(NotTree(Leaf('a')), OrTree(NotTree(Leaf('b')), \
    Leaf('c')))
    >>> helper_evaluator(root, 'abc', '', 'AEA', '1')
    True
    '''
    # get all the perms possible for the variables and store them in a list
    possible_moves = possible_solutions(variables)
    # make a counter variable that will keep track of the index and a bool
    # variable that will change is any one of the perms returns the opposite
    # of the wanted result. We assume that there is a winning strategy. if
    # there is a result that opposes the winning strategy, we will make this
    # false
    list_index = 0
    is_winning = True
    # we know that the next player to play the move will be at the same index
    # as the len of values
    # get the player for which we are deciding the move for
    player = turns[len(values)]
    # these are the rules defined in the handout: E is trying to the formula
    # true(1) and A is trying to make the formula false(0). Assigning the
    # winning_outcome accordingly
    # if the player is E, make the winning_outcome 1
    if (player == 'E'):
        winning_outcome = 1
    # else the player is A, therefore make the winning_outcome 0
    else:
        winning_outcome = 0
    # now loop through each of the perms while the winning strategy assumption
    # is not false
    while (list_index < len(possible_moves)) and (is_winning):
        # get the perm at the current index
        perm = possible_moves[list_index]
        # spilt the perm to the len of the values + 1
        first_part = perm[:len(values) + 1]
        # combing the assigned variable and the move/values we have been given
        match_this = values + assigned_value
        # see if the perms first order is the same as the given moves/values to
        # us (that the moves/values that are given to us + the value we assign
        # to the variable is the same as the first part of the perm) if it is,
        if (match_this == first_part):
            # then evaluate the formula using the perm
            evaluated = evaluate(root, variables, perm)
            # check if evaluated is what the player wants, if its not, then
            # make the boolean variable false
            if (evaluated != winning_outcome):
                is_winning = False
            # this if statement has to be in this loop, because if the parts
            # don't match then evaluated will not have a value assigned to it
            # it will raise an error. Therefore the if statement stays; QED :D
        # increase the counter by 1
        list_index += 1
    # return the boolean variable
    return is_winning


def play2win(root, turns, variables, values):
    ''' (FormulaTree, str, str, str) -> int
    Returns a string representation of the truth value which is the next best
    move for the next player's turn. If choosing 1 or 0 leads to winning, then
    returns 1 if the next player is E and 0 if the next player is A
    Note: player A is trying to make the formula at <root> 0 (False) and
    player E is trying to make the formula at <root> 1 (True)
    REQ: <root> can not be empty, i.e. it should have at least one node
    REQ: <root> should have all the variables that <variables> contains
    REQ: <variables> should be lower case and be in <root>
    REQ: <values> should only consist of 1's and 0's
    REQ: <turns> should only consist of E's and A's
    REQ: number of <variables> should be equal to number of <turns>
    REQ: len(turns/variables) > len(values) i.e. there must be a next move
    >>> tree = AndTree(NotTree(Leaf('a')), OrTree(NotTree(Leaf('b')), \
    Leaf('c')))
    >>> play2win(tree, 'AEA', 'abc', '')  # here you are assigning for A
    1
    >>> tree = OrTree(NotTree(Leaf('x')), Leaf('y'))
    >>> play2win(tree, 'AE', 'xy', '1')  # here you are assigning for E
    1
    >>> tree = AndTree(OrTree(Leaf('x'), Leaf('y')), \
    NotTree(OrTree(NotTree(Leaf('y')), Leaf('x'))))
    >>> play2win(tree, "EA", "xy", "")
    1
    >>> tree = AndTree(Leaf('a'), Leaf('b'))
    >>> play2win(tree, "EA", "ab", "0")
    0
    '''
    # we will use the helper function to help us with this function
    # get the player that we are going to be deciding the move for (using the
    # same logic as we did in the helper)
    player = turns[len(values)]
    # if the player is E
    if (player == 'E'):
        # set the default move to 1, as said in the handout
        default_move = 1
        # use the helper function to evaluate if 1 works for all possible
        # values. Do the same with 0 and store all of this information in bool
        # variables
        evaluate_one = helper_evaluator(root, variables, values, turns, '1')
        evaluate_zero = helper_evaluator(root, variables, values, turns, '0')
        # if the evaluation of 1 is T and 0 is F,
        if (evaluate_one is True) and (evaluate_zero is False):
            # then make the winning move 1
            winning_move = 1
        # elif the evaluation of 0 is T and 1 is F,
        elif (evaluate_zero is True) and (evaluate_one is False):
            # then make the winning move 0
            winning_move = 0
        # else both of them are either True or False. In this case, we return
        # the default move. since we know that the player is E, we return its
        # default move
        else:
            winning_move = default_move
    # else we know that the player is A, hence we do the same checks again
    else:
        # set the default move to 0, as said in the handout
        default_move = 0
        # then use the helper function to evaluate if 1 works for all possible
        # values. Do the same with 0 and store all of this information in bool
        # variables
        evaluate_one = helper_evaluator(root, variables, values, turns, '1')
        evaluate_zero = helper_evaluator(root, variables, values, turns, '0')
        # if the evaluation of 1 is T and 0 is F,
        if (evaluate_one is True) and (evaluate_zero is False):
            # then make the winning move 1
            winning_move = 1
        # elif the evaluation of 0 is T and 1 is F,
        elif (evaluate_zero is True) and (evaluate_one is False):
            # then make the winning move 0
            winning_move = 0
        # else both of them are either True or False. In this case, we return
        # the default move. since we know that the player is A, we return its
        # default move
        else:
            winning_move = default_move
    # return the winning move
    return winning_move
    # Quod Erat Demonstrandum

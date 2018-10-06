"""
Name: Sakina Shabbir Gadriwala
UTORid: gadriwa1
Student Number: 1004351051
Date: Feb 24th, 2017
# Copyright Nick Cheng, 2018
# Copyright Sakina Shabbir Gadriwala, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from wackynode import WackyNode

# Do not add import statements or change the one above.
# Write your WackyQueue class code below.


class WackyQueue:
    ''' a sequence of objects that have integer priority i.e. the more
    positive the object, the higher the priority, and the more negative
    the object the lesser the priority '''

    def __init__(self):
        ''' (WackyQueue) -> None
        Returns None and initializes all the instance variables needed for the
        class
        '''
        # Representation Invariant:
        # > what are the instances used and what data structure is used for
        # them?
        # _even_list is a linked list
        # _odd_list is a linked list
        # > what are the things inside of this data structure?
        # items inside _even_list and _odd_list are stored as WackyNodes
        # > what is the arrangement of these items, if they follow a specific
        #   pattern
        # _even_list stores all the objects that are inserted in even insertion
        # numbers (0, 2, 4...)
        # _odd_list stores all the objects that are inserted in odd insertion
        # numbers (1, 3, 5...)

        # initialize the lists with a nodes aka head
        self._odd_list = WackyNode(None, None)
        self._even_list = WackyNode(None, None)

    def loop_even(self):
        ''' (WackyQueue) -> int
        Returns the size of the even linked list
        '''
        # initialize a counter
        size = 0
        # initialize the current node as head
        curr = self._even_list.get_next()
        # loop through the list till you're at the end of the list
        # how do you know that end? The current will point to None. You want to
        # stop as soon as current points to none
        while curr is not None:
            # in the loop, increase the counter by 1 and get the next element
            # set curr equal to that next element
            size += 1
            curr = curr.get_next()
        # return the counter (because the counter will be the size of the list)
        return size

    def loop_odd(self):
        ''' (WackyQueue) -> int
        Returns the size of the odd linked list
        '''
        # initialize a counter
        size = 0
        # initialize the current node as head
        curr = self._even_list.get_next()
        # loop through the list till you're at the end of the list
        # how do you know that end? The current will point to None. You want to
        # stop as soon as current points to none
        while curr is not None:
            # in the loop, increase the counter by 1 and get the next element
            # set curr equal to that next element
            size += 1
            curr = curr.get_next()
        # return the counter (because the counter will be the size of the list)
        return size

    def find_by_pri(self, priority):
        ''' (WackyQueue, int) -> WackyNode, WackyNode, WackyNode
        Returns a wacky node that points to the node with priority
        <priority> we are looking for, the node previous to it, and the node
        after it. (previous, current, after). If <priority> is not found,
        then previous will point to the last node of the list and
        current and after will point to None.
        REQ: <item> with <priority> has to be in the wacky queue
        REQ: wacky queue can not be empty
        '''
        # we want to alternate between our lists. Therefore, we need 3 pointers
        # one that points to the current node, one that points to the node
        # previous to it, and one that points to the previous of previous
        # (2 away from the current node). Why do we need so many pointers?
        # we want to keep track of the previous nodes. Since we're alternating
        # between lists, we want the third pointer to be pointing to the
        # previous list we checked, so that we can go back to that one again.

        # initialize all my pointers. curr will be head of the odd list, since
        # we start inserting from the odd list. prev and second_last will be
        # None
        second_last = None
        prev = None
        curr = self._odd_list
        # we need something to alternate lists. From Piazza, we can do this:
        # x, y = y, x. Setting our lists to variables
        curr_list, next_list = self._odd_list, self._even_list
        # while we are not at the end of the list and we haven't found the
        # priority yet
        while (curr is not None) and (curr.get_priority() is not priority):
            # change the lists (to alternate the lists)
            curr_list, next_list = next_list, curr_list
            # make second last point to where previous is pointing
            second_last = prev
            # then make the previous point to where current is pointing
            prev = curr
            # then make the current point to the next node in this list, which
            # is the one from the even list
            curr = curr_list.get_next()
        # two things will get you out of the loop: if the pri is found or if
        # curr is None which means that we've hit the end of our list
        # if curr is None, then everything else will be None too
        if curr is None:
            after = None
        else:
            after = curr_list.get_next()
        # return the nodes
        return prev, curr, after

    def find_by_item(self, item):
        ''' (WackyQueue, obj) -> WackyNode, WackyNode, WackyNode
        Returns a pointer to the node that contains the object <item>. If
        <item> is not in the list, None will be returned
        REQ: WackyQueue should have the item in it already
        '''
        # the algorithm is similar to find by pri, but instead of looking for
        # the pri, we are looking for the item
        # we will again need 3 pointers, for the same reasons as above (should
        # I just copy past my algorithm here, lol?) here:

        # initialize all my pointers. curr will be head of the odd list, since
        # we start inserting from the odd list. prev and second_last will be
        # None
        second_last = None
        prev = None
        curr = self._odd_list
        # we need something to alternate lists. From Piazza, we can do this:
        # x, y = y, x. Setting our lists to variables
        curr_list, next_list = self._odd_list, self._even_list
        # while we are not at the end of the list and we haven't found the
        # priority yet
        while (curr is not None) and (curr.get_item() is not item):
            # change the lists (to alternate the lists)
            curr_list, next_list = next_list, curr_list
            # make second last point to where previous is pointing
            second_last = prev
            # then make the previous point to where current is pointing
            prev = curr
            # then make the current point to the next node in this list, which
            # is the one from the even list
            curr = curr_list.get_next()
        # two things will get you out of the loop: if the item is found or if
        # curr is None which means that we've hit the end of our list
        # if curr is None, then everything else will be None too
        if curr is None:
            after = None
        else:
            after = curr_list.get_next()
        # return the nodes
        return prev, curr, after

    def reverse_list(self, linked_list):
        ''' (WackyQueue, WackyQueue) -> WackyNode
        Returns None and reverses the <linked_list> s.t. the head is the new
        tail and the tail is new head
        REQ: linked_list can not be empty
        '''
        # the algorithm is simple. initialize 3 pointers: before, current and
        # after where before is pointing to the node before current (i.e. None)
        # current is pointing to the the node whose pointer are being changed
        # and after is the pointer after the current node
        before = None
        curr = linked_list
        after = linked_list.get_next()
        # while we are not at the end of the list i.e. current is not None
        while (curr is not None):
            # set the pointer of the current node equal to previous
            curr.set_next(before)
            # make the previous pointer point to where current is pointing
            before = curr
            # make current point to where after is pointing
            curr = after
            # make after point to the next node to current
            after = curr.get_next()

    def negator(self, linked_list):
        ''' (WackyQueue, WackyQueue) -> None
        Negates the priorities of the <linked_list>
        REQ: linked_list is not empty
        '''
        # this one is fairly simple:
        # set curr to the head of the list
        curr = linked_list
        # loop through the list till you reach the end aka none
        while (curr is not None):
            # get each elements priority
            pri = curr.get_priority()
            # and negate it
            pri = - pri
            # then set the elements priority as it should be
            curr.set_priority(pri)
            # get the next element
            curr = curr.get_next()

    def insert(self, item, priority):
        ''' (WackyQueue, obj, int) -> None
        Returns None and inserts the object <item> at the given <priority>
        User can have duplicate objects at the same or at different priorities
        '''
        # in all scenarios we have to make a new node. Making a new wacky node
        # that points to none. We then have to assign new pointers to it and
        # make it part of the linked list family
        new_node = WackyNode(item, priority)
        # here comes the hard part! The part where pictures came in handy
        # thanks Nick for the drawing tip! Also, pri = priority in short :)
        # initialize curr to the head of the odd list
        curr = self._odd_list.get_next()
        after = self._even_list.get_next()
        # if curr is none, that is the odd list is empty
        if (curr is None):
            # then make the odd list point to the new node
            self._odd_list.set_next(new_node)
        # else if after in None, that is the even list is empty
        elif (after is None):
            # then add the new node to the even list
            self._even_list.set_next(new_node)
        # have a while loop that loops through the entire queue and looks
        # if the pri fits any of these case
        while (curr is not None) and (after is not None):
            # four cases:
            # 1- the general case, curr > insert > after
            if (curr.get_priority() > priority) and \
               (priority > after.get_priority()):
                # then curr and after don't get changed
                curr = curr # this is causing the infinite loop
                after = after
                # the insert pointer algorithm: tho this will be repeated many
                # times in this function, only one of them will be executed
                # because of the elif structure
                # make curr point to the new node
                curr.set_next(new_node)
                # make after point to curr.next
                after.set_next(curr.get_next())
                # make new node point to after.next
                new_node.set_next(after.get_next())

            # 2- edge case: insert > curr
            elif (priority > curr.get_priority()):
                # then set after to be curr
                after = curr
                # and curr to be None
                curr = None
                # here our insert pointer algorithm will not work, because
                # None.any_method() will raise an exception
                # so here's the modified version of it:
                # since we're inserting at the head of the list, it will always
                # be inserted at the head of the odd list
                # make the head of the odd list point to the new node
                self._odd_list.set_next(new_node)
                # make head of the even point to the first node of odd
                self._even_list.set_next(after)
                # make the new node point to the first node of even
                new_node.set_next(after.get_next())

            # 3- multiple entries of the same pri
            elif (priority == curr.get_priority()):
                # this is super messy, but let's do it! find a priority that
                # is less than the one we have
                while not (after.get_priority() < priority): # crashes whn\en after becomes None
                    # set curr = after and after to the next node after curr
                    curr, after = after, curr.get_next()

            # 4- edge case: curr = None
            elif (curr is None):
                # then insert the new node at the end
                curr.set_next(new_node)
            # if they fit none of these cases, get new currs and afters
            else:
                curr, after = after, curr.get_next()

    def extracthigh(self):
        ''' (WackyQueue) -> obj
        Removes and returns the first object in the wacky queue
        REQ: Wacky Queue must have at least one item in it
        '''
        # initialize item to be None
        item = None
        # ^why? because if both the lists are empty, then item will be None and
        # the program won't crash
        size_odd = self.loop_odd()
        size_even = self.loop_even()
        # the case where we will only have one item in our list: then the size
        # of odd will be 1 and the size of even will 0. If this is the case,
        # then we will get the first item and make the odd_list point to none
        if (size_odd == 1 and size_even == 0):
            # get the item that is stored in the first node
            item = self._odd_list.get_item()
            # set the odd_list's head to None
            self._odd_list.set_next(None)
        # since the first object that we're inserting goes in the odd list
        # we will only use the odd list for this purpose
        # check if the odd list is not empty (if this is false, then the entire
        # list is empty and we can't do anything there)
        elif (self._odd_list is not None) and (self._even_list is not None):
            # get the first node, get the obj stored in it and store it in a
            # var to return that
            item = self._odd_list.get_item()
            # then rearrange the pointers s.t. you isolate the top most element
            # this will delete the element under the lense
            # for that, get the new head for the odd list and get the new head
            # for the even list
            # the odd head is the same as the even's current head
            new_odd_head = self._even_list.get_next()
            # the new even head is the same as the 2nd element in the odd list
            # step 1 to isolate the first node in the odd list (hence
            # extracting the high in the list)
            new_even_head = self._odd_list.get_next().get_next()
            # we now have both our heads; let's draw our connectors!
            # make the odd_list point to the new odd head
            self._odd_list.set_next(new_odd_head)
            # make the even_list point to the new even head
            self._even_list.set_next(new_even_head)
        # return the obj that was stored in that node
        return item

    def isempty(self):
        ''' (WackyQueue) -> bool
        Returns True if the wacky queue is empty. Otherwise, returns False.
        '''
        # get the sizes of both the lists using the helper methods
        odd_size = self.loop_odd()
        even_size = self.loop_even()
        # set up a bool statement s.t. if the addition == 0, then it evaluates
        # to True. Otherwise, evaluates to False
        is_empty = (odd_size + even_size) == 0
        # return the boolean variable
        return is_empty

    def changepriority(self, item, new_pri):
        ''' (WackyQueue, obj, int) -> None
        Returns None and changes the priority of the first occurence of the
        object <item> to the new priority <new_pri>. If <item> is not found,
        or already has the priority set to <new_pri>, then WackyQueue remains
        unchanged
        '''
        # use the find method to find the item
        (prev, curr, after) = self.find_by_item(item)
        # once we have the item, we can change its priority using
        # the wacky node methods
        curr.set_priority(new_pri)
        # we then need to rearrange the object to its new position aka delete
        # that node and then insert it again
        # to delete this node, we make the prev point to the after. We will
        # not lose the node that has to be rearranged, because curr is pointing
        # to it
        prev.set_next(after)
        # then to insert curr back into the list, use the insert function
        # this way, we will know that curr is in the right position i.e. our
        # priority queue still has order in it
        self.insert(curr)

    def negateall(self):
        ''' (WackyQueue) -> None
        Returns None and negates the priority of every object in the wacky
        queue. This also reverses the the order of insertion time. Hence
        reverses the order of objs with equal priority.
        '''
        # this one is fairly simple:
        # call the negator function on each list
        self.negator(self._odd_list)
        self.negator(self._even_list)
        # call the reverse function and reverse each list independantly
        # why independantly? because we know that the list is in order
        # and negating each element will make the priority reversed. We want
        # our list to be in the same priority that nick set. Hence the easy
        # solution: Reverse it!
        self.reverse(self._odd_list)
        self.reverse(self._even_list)
        # QED! :D

    def getoddlist(self):
        ''' (WackyQueue) -> WackyNode
        Returns the pointer to a linked list of wacky nodes with every other
        object in wacky queue starting from the first object i.e. the list
        must contain every odd indexed object.
        If there is no first object, then an empty list will be returned.
        '''
        # return the odd list
        return self._odd_list

    def getevenlist(self):
        ''' (WackyQueue) -> WackyNode
        Returns the pointer to a linked list of wacky nodes with every other
        object in wacky queue starting from the second object i.e. the list
        must contain every even indexed object.
        If there is no second object, then an empty list will be returned.
        '''
        # return the even list
        return self._even_list

    def __str__(self):
        curr = self._odd_list
        after = self._even_list
        output = ''
        while (curr is not None) and (after is not None):
            output += str(curr) + ' '
            curr, after = after, curr.get_next()
        return output

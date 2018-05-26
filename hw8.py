''' Homework 8 - DSC 20, W18'''


##############################################################################
# Problem 1.1
##############################################################################

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __str__(self):
        """Returns a human-readable string representation of the Link

        >>> s = Link(1, Link(2, Link(3, Link(4))))
        >>> str(s)
        '<1 2 3 4>'
        >>> str(Link(1))
        '<1>'
        >>> str(Link.empty)  # empty tuple
        '()'
        """
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def digits(n):
    """Return the digits of n as a linked list.

    >>> digits(0) is Link.empty
    True
    >>> digits(543)
    Link(5, Link(4, Link(3)))
    """
    s = Link.empty
    while n > 0:
        n, last = n // 10, n % 10
        #Your Code Here#
    return s


##############################################################################
# Problem 1.2
##############################################################################

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        #Your Code Here#
        new_Fib = Fib(self.value)
        new_Fib.previous = self.value
        if self.value == 0:
            new_Fib.value = 1
            return new_Fib
        else:
            new_Fib.value = self.previous + self.value
        return new_Fib

    def __repr__(self):
        return str(self.value)

##############################################################################
# Problem 1.3
##############################################################################


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    #Your Code Here#


##############################################################################
# Problem 2
##############################################################################


##############################################################################
# Problem 3
##############################################################################

def clip_list(s, index):
    """
    >>> s1 = Link (1 , Link (2 , Link (3)))
    >>> clip_list ( s1 , 0)
    Link(2, Link(3))
    >>> s1
    Link(1)
    >>> s2 = Link (1 , Link (2 , Link (3)))
    >>> clip_list ( s2 , 2) == Link . empty # No elements after index 2
    True
    >>> s2
    Link(1, Link(2, Link(3)))
    >>> s3 = Link (1 , Link (2 , Link (3))) 
    >>> try:clip_list ( s3 , 3) #no index 3 available
    ... except(IndexError):
    ...   print("good job")
    ...
    good job
    """
    #Your Code Here#


##############################################################################
# Problem 4
##############################################################################
import numpy as np
# Q 4.1: Custom Queue Implementation

#Your Code Here#


# Q 4.2: Cursed Carousel

def cursed_carousel(n, m):
    '''
    m is the number of customers in line
    n is the number of customers sent to the back of the line
    return the number of the customer which is last to be served
    >>> cursed_carousel(10,2)
    2
    4
    6
    8
    10
    3
    7
    1
    9
    5
    >>> cursed_carousel(4,7)
    3
    4
    1
    2
    >>> cursed_carousel(5,1)
    1
    2
    3
    4
    5
    '''
    #Your code here#

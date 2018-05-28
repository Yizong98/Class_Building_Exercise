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

    assert isinstance(n, int), "n must be integer"

    assert(n >= 0), "n must be non-negative integer"

    s = Link.empty

    while n > 0:

        n, last = n // 10, n % 10

        #Your Code Here#

        s = Link(last, s)

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
    depo = 0
    stock = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def vend(self):
        if self.stock == 0:
            return "Machine is out of stock."
        elif self.depo < self.price:
            return 'You must deposit ${0} more.'.format(self.price - self.depo)
        else:
            self.stock -= 1
            change = self.depo - self.price
            self.depo = 0
            if change == 0:
                return 'Here is your {0}.'.format(self.name)
            return 'Here is your {0} and ${1} change.'.format(self.name, change)

    def deposit(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)
        else:
            self.depo = self.depo + amount
            return 'Current balance: ${0}'.format(self.depo)

    def restock(self, number):
        self.stock += number
        return 'Current {0} stock: {1}'.format(self.name, self.stock)


##############################################################################
# Problem 2
##############################################################################
class Beverage:

    def __init__(self, name, hot):
        self.name = name
        self.hot = hot

    def __str__(self):
        if self.hot:
            return "Hot {0}".format(self.name)
        else:
            return "Cold {0}".format(self.name)


class Coffee(Beverage):
    Beverage.hot = True

    def __init__(self, sugars, cream):
        assert isinstance(sugars, int), "sugars must be integer"
        assert isinstance(cream, int), "cream must be integer"
        self.sugars = sugars
        self.cream = cream
        self.ingredients = {"sugars": sugars, "creams": cream}

    def __str__(self):
        return 'Coffee with {0} sugars and {1} creams'.format(self.sugars, self.cream)


class Soda(Beverage):
    Beverage.hot = False

    def __init__(self, is_carbonated):
        self.is_carbonated = is_carbonated

    def __str__(self):
        return 'Cold Soda'


class Coke(Soda):
    Soda.hot = False
    Soda.is_carbonated = True

    def __init__(self, my_favorite):
        self.my_favorite = my_favorite

    def __str__(self):
        if self.my_favorite:
            return 'Cold Coke is my favorite'
        else:
            return 'Could not care less for Coke'

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
    #raise IndexError('Index not available')
    if s == Link.empty:
        raise IndexError('Index not available')
    if index == 0:
        rest, s.rest = s.rest, Link.empty
        return rest
    else:
        return clip_list(s.rest, index - 1)


def remove_last_occurrence(lst, elem):
    """
    >>> l2 = Link('a', Link('b', Link('c', Link('d'))))
    >>> remove_last_occurrence(l2, 'b')
    >>> l2
    Link(a, Link(c, Link(d)))

    >>> remove_last_occurrence(l2, 'd')
    >>> l2
    Link(a, Link(c))

    >>> l3 = Link.empty
    >>> remove_last_occurrence(l3, 'delete_me')
    >>> l3 == Link.empty
    True

    >>> l4 = Link('b', Link('a', Link('b', Link('a', Link('b')))))
    >>> remove_last_occurrence(l4, 'a')
    >>> l4
    Link(b, Link(a, Link(b, Link(b))))
    """
    """YOUR CODE GOES HERE"""
    if lst == Link.empty:
        return
    else:
        i = lst
        index = 0
        found_idx = None
        while i != Link.empty:
            if i.first == elem:
                found_idx = index
            index += 1
            i = i.rest
        if found_idx == None:
            return "No occurence found!"

    def delete_at(s, idx):
        if idx == 0:
            return s.rest
        else:
            return Link(s.first, delete_at(s.rest, idx - 1))
    lst.rest = delete_at(lst, found_idx).rest


##############################################################################
# Problem 4
##############################################################################
import numpy as np
# Q 4.1: Custom Queue Implementation

#Your Code Here#


class Queue:

    def __init__(self, front, rear, num_elems=0, capacity=5):
        self.front = front
        self.rear = rear
        self.num_elems = num_elems
        self.capacity = capacity
        self.data = np.array([None] * capacity, dtype=object)

    def dequeue(self):
        elem = self.data[self.front]
        assert(elem != None), "cannot remove empty elements"
        self.data[self.front] = None
        self.front = self.front + 1
        if (self.front == len(self.data)):
            self.front = 0
        self.num_elems -= 1
        return elem

    def enqueue(self, elem):
        double = 2
        self.data[self.rear] = elem
        self.num_elems += 1
        self.rear = self.rear + 1
        if (self.rear == len(self.data)):
            self.rear = 0
        if self.is_full():
            self.capacity *= double
            new_data = np.array([None] * self.capacity, dtype=object)
            new_data[0:(len(self.data))] = self.data
            self.data = new_data

    def is_full(self):
        if self.num_elems == self.capacity:
            return True
        return False

    def is_empty(self):
        if self.num_elems == 0:
            return True
        return False

    def print_queue(self):
        if self.is_empty():
            print([])
            return
        print('[|' + '|'.join("{}".format(k) for k in self.data) + '|]')
        return


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
    carousel = Queue(0, 0, capacity=n + 1)
    for i in (np.arange(n) + 1):
        carousel.enqueue(i)
    while carousel.num_elems > 0:
        for i in range(m):
            if i != (m - 1):
                carousel.enqueue(carousel.dequeue())
            else:
                print(carousel.dequeue())

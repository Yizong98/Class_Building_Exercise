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
    >>> digits(7777)
    Link(7, Link(7, Link(7, Link(7))))
    >>> digits(678)
    Link(6, Link(7, Link(8)))
    >>> digits(000) == Link.empty
    True
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
    >>> start.next().next().next().next().next().next().next()
    13
    >>> start.next().next().next().next().next().next().next().next()
    21
    >>> start.next().next().next().next().next().next().next().next().next()
    34
    """

    def __init__(self, value=0):
        """
        >>> start = Fib()
        >>> start.value
        0
        >>> start = Fib(2)
        >>> start.value
        2
        >>> start = Fib(3)
        >>> start.value
        3
        """
        self.value = value

    def next(self):
        #Your Code Here#
        """
        >>> start = Fib()
        >>> start
        0
        >>> start.next()
        1
        >>> start.next().next()
        1
        >>> start.next().next().next()
        2
        """
        assert isinstance(self.value, int), "value must be int"
        new_Fib = Fib(self.value)
        new_Fib.previous = self.value
        if self.value == 0:
            new_Fib.value = 1
            return new_Fib
        else:
            new_Fib.value = self.previous + self.value
        return new_Fib

    def __repr__(self):
        """
        >>> start = Fib()
        >>> repr(start)
        '0'
        >>> repr(start.next())
        '1'
        >>> repr(start.next().next())
        '1'
        """
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

    >>> w = VendingMachine('soda', 3)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(3)
    'Current balance: $3'
    >>> w.vend()
    'Here is your soda.'

    >>> w = VendingMachine('coke', 5)
    >>> w.restock(3)
    'Current coke stock: 3'
    >>> w.restock(3)
    'Current coke stock: 6'
    >>> w.deposit(5)
    'Current balance: $5'
    >>> w.vend()
    'Here is your coke.'

    >>> w = VendingMachine('pepsi', 4)
    >>> w.restock(3)
    'Current pepsi stock: 3'
    >>> w.restock(3)
    'Current pepsi stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'You must deposit $2 more.'
    >>> w.deposit(2)
    'Current balance: $4'
    >>> w.vend()
    'Here is your pepsi.'
    """
    #Your Code Here#
    depo = 0
    stock = 0

    def __init__(self, name, price):
        """
        >>> v = VendingMachine('candy', 10)
        >>> v.name
        'candy'
        >>> v.price
        10
        >>> v = VendingMachine('coke', 2)
        >>> v.name
        'coke'
        """
        assert isinstance(name, str), "name should be string"
        assert isinstance(price, (int, complex, float)
                          ), "price should be a valid number"
        self.name = name
        self.price = price

    def vend(self):
        """
        >>> v = VendingMachine('candy', 10)
        >>> v.vend()
        'Machine is out of stock.'
        >>> v.deposit(10)
        'Machine is out of stock. Here is your $10.'
        >>> v.restock(1)
        'Current candy stock: 1'
        >>> v.deposit(10)
        'Current balance: $10'
        >>> v.vend()
        'Here is your candy.'
        >>> v = VendingMachine('coke', 10)
        >>> v.vend()
        'Machine is out of stock.'
        """
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
        """
        >>> v = VendingMachine('candy', 10)
        >>> v.vend()
        'Machine is out of stock.'
        >>> v.deposit(10)
        'Machine is out of stock. Here is your $10.'
        >>> v.deposit(100)
        'Machine is out of stock. Here is your $100.'
        >>> v.deposit(20)
        'Machine is out of stock. Here is your $20.'
        """
        assert isinstance(amount, int), "amount should be int"
        assert(amount >= 0), "amount should be non-negative"
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)
        else:
            self.depo = self.depo + amount
            return 'Current balance: ${0}'.format(self.depo)

    def restock(self, number):
        """
        >>> w = VendingMachine('pepsi', 4)
        >>> w.restock(3)
        'Current pepsi stock: 3'
        >>> w.restock(3)
        'Current pepsi stock: 6'
        >>> w.restock(3)
        'Current pepsi stock: 9'
        """
        assert isinstance(number, int), "number should be int"
        self.stock += number
        return 'Current {0} stock: {1}'.format(self.name, self.stock)


##############################################################################
# Problem 2
##############################################################################
class Beverage:

    def __init__(self, name, hot):
        """
        >>> bev = Beverage('Coco', True)
        >>> bev.name = 'Coco'
        >>> bev.hot = True
        >>> bev = Beverage('Coke', False)
        >>> bev.name = 'Coke'
        """
        assert isinstance(name, str), "name should be string"
        assert isinstance(hot, bool), "hot should be boolean"
        self.name = name
        self.hot = hot

    def __str__(self):
        """
        >>> bev = Beverage('Coco', True)
        >>> print(bev)
        Hot Coco
        >>> bev = Beverage('Pepsi', True)
        >>> print(bev)
        Hot Pepsi
        >>> bev = Beverage('Coke', False)
        >>> print(bev)
        Cold Coke
        """
        if self.hot:
            return "Hot {0}".format(self.name)
        else:
            return "Cold {0}".format(self.name)


class Coffee(Beverage):
    Beverage.hot = True

    def __init__(self, sugars, cream):
        """
        >>> coff = Coffee(2, 3)
        >>> coff.sugars = 2
        >>> coff.cream = 3
        >>> coff.ingredients = {"sugars": 2, "creams": 3}
        """
        assert isinstance(sugars, int), "sugars must be integer"
        assert isinstance(cream, int), "cream must be integer"
        self.sugars = sugars
        self.cream = cream
        self.ingredients = {"sugars": sugars, "creams": cream}

    def __str__(self):
        """
        >>> coff = Coffee(2, 3)
        >>> print(coff)
        Coffee with 2 sugars and 3 creams
        >>> coff = Coffee(4, 3)
        >>> print(coff)
        Coffee with 4 sugars and 3 creams
        >>> coff = Coffee(5, 6)
        >>> print(coff)
        Coffee with 5 sugars and 6 creams
        """
        return 'Coffee with {0} sugars and {1} creams'.format(self.sugars, self.cream)


class Soda(Beverage):
    Beverage.hot = False

    def __init__(self, is_carbonated):
        """
        >>> soda = Soda(False)
        >>> soda.is_carbonated
        False
        >>> soda = Soda(True)
        >>> soda.is_carbonated
        True
        >>> soda1 = Soda(False)
        >>> soda1.is_carbonated
        False
        """
        assert isinstance(
            is_carbonated, bool), "is_carbonated should be boolean"
        self.is_carbonated = is_carbonated

    def __str__(self):
        """
        >>> soda = Soda(True)
        >>> print(soda)
        Cold Soda
        >>> soda = Soda(False)
        >>> print(soda)
        Cold Soda
        >>> soda1 = Soda(False)
        >>> print(soda1)
        Cold Soda

        """
        return 'Cold Soda'


class Coke(Soda):
    Soda.hot = False
    Soda.is_carbonated = True

    def __init__(self, my_favorite):
        """
        >>> cola_coke = Coke(True)
        >>> cola_coke.my_favorite
        True
        >>> co_coke = Coke(True)
        >>> co_coke.my_favorite
        True
        >>> col_coke = Coke(False)
        >>> col_coke.my_favorite
        False
        """
        assert isinstance(
            my_favorite, bool), "is_carbonated should be boolean"
        self.my_favorite = my_favorite

    def __str__(self):
        """
        >>> cola_coke = Coke(True)
        >>> print(cola_coke)
        Cold Coke is my favorite
        >>> pep_coke = Coke(True)
        >>> print(pep_coke)
        Cold Coke is my favorite
        >>> huk_coke = Coke(False)
        >>> print(huk_coke)
        Could not care less for Coke
        """
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
    >>> s4 = Link (1 , Link (2 , Link (3))) 
    >>> try:clip_list ( s4 , 30) #no index 30 available
    ... except(IndexError):
    ...   print("good job")
    ...
    good job
    >>> s5 = Link(2,Link (1 , Link (2 , Link (3))))
    >>> clip_list ( s5 , 3) == Link . empty # No elements after index 3
    True
    >>> clip_list ( s5 , 0)
    Link(1, Link(2, Link(3)))
    >>> s5
    Link(2)
    """
    #Your Code Here#
    #raise IndexError('Index not available')
    assert isinstance(index, int), "index should be int"
    assert(index >= 0), "index should be non-negative"
    assert (type(s) == Link or s == Link.empty), "s should belong to Link class"
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

    >>> l5 = Link('b', Link('c', Link('b', Link('a', Link('b')))))
    >>> remove_last_occurrence(l5, 'c')
    >>> l5
    Link(b, Link(b, Link(a, Link(b))))


    >>> l6 = Link('a', Link('a', Link('a', Link('a', Link('a')))))
    >>> remove_last_occurrence(l6, 'a')
    >>> l6
    Link(a, Link(a, Link(a, Link(a))))


    >>> l7 = Link('b', Link('c', Link('b', Link('a', Link('b')))))
    >>> remove_last_occurrence(l7, 'a')
    >>> l7
    Link(b, Link(c, Link(b, Link(b))))
    """

    """YOUR CODE GOES HERE"""
    assert (elem is not None), "elem cannot be Nonetype"
    assert (type(lst) == Link or lst ==
            Link.empty), "lst should belong to Link class"
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
        """
        >>> l7 = Link('b', Link('c', Link('b', Link('a', Link('b')))))
        >>> delete_at(l7, 0)
        Link(c, Link(b, Link(a, Link(b))))
        >>> l8 = Link('b', Link('c', Link('b', Link('a', Link('b')))))
        >>> delete_at(l8, 1)
        Link(b, Link(b, Link(a, Link(b))))
        >>> l9 = Link('b', Link('c', Link('b', Link('a', Link('b')))))
        >>> delete_at(l9, 2)
        Link(b, Link(c, Link(a, Link(b))))
        """
        assert (type(s) == Link or s ==
                Link.empty), "s should belong to Link class"
        assert isinstance(idx, int), "idx should be int"
        assert(idx >= 0), "idx should be non-negative"
        try:
          if idx == 0:
              return s.rest
          else:
              return Link(s.first, delete_at(s.rest, idx - 1))
        except:
          return "idx out of bounds!"
    lst.rest = delete_at(lst, found_idx).rest


##############################################################################
# Problem 4
##############################################################################
import numpy as np
# Q 4.1: Custom Queue Implementation

#Your Code Here#


class Queue:

    def __init__(self, front, rear, num_elems=0, capacity=5):
        """
        >>> Q1 = Queue(2,3,4)
        >>> Q1.front
        2
        >>> Q1.rear
        3
        >>> Q1.num_elems
        4
        >>> Q1.capacity
        5
        >>>
        array([None, None, None, None, None, None, None], dtype=object)

        >>> Q2 = Queue(2,3,4,6)
        >>> Q2.front
        2
        >>> Q2.rear
        3
        >>> Q2.num_elems
        4
        >>> Q2.capacity
        6
        >>>
        array([None, None, None, None, None, None, None, None], dtype=object)

        >>> Q1 = Queue(2,3,capacity=6)
        >>> Q1.front
        2
        >>> Q1.rear
        3
        >>> Q1.num_elems
        0
        >>> Q1.capacity
        6
        >>>
        array([None, None, None, None, None, None, None, None], dtype=object)

        """
        assert isinstance(front, int), "front should be int"
        assert isinstance(rear, int), "rear should be int"
        assert isinstance(num_elems, int), "num_elems should be int"
        assert isinstance(capacity, int), "capacity should be int"
        assert (front >= 0), "front should be non-negative"
        assert (rear >= 0), "rear should be non-negative"
        assert (num_elems >= 0), "num_elems should be non-negative"
        assert (capacity >= 0), "capacity should be non-negative"
        self.front = front
        self.rear = rear
        self.num_elems = num_elems
        self.capacity = capacity
        self.data = np.array([None] * capacity, dtype=object)

    def dequeue(self):
        """
        >>> Q1 = Queue(0,0,capacity=7)
        >>> for i in (np.arange(6)+1): Q1.enqueue(i)
        >>> Q1.data
        array([1, 2, 3, 4, 5, 6, None], dtype=object)
        >>> Q1.dequeue()
        1
        >>> Q1.dequeue()
        2
        >>> Q1.dequeue()
        3
        """
        elem = self.data[self.front]
        assert(elem != None), "cannot remove empty elements"
        self.data[self.front] = None
        self.front = self.front + 1
        if (self.front == len(self.data)):
            self.front = 0
        self.num_elems -= 1
        return elem

    def enqueue(self, elem):
        """
        >>> Q1 = Queue(0,0,capacity=7)
        >>> Q1.enqueue(1)
        >>> Q1.data
        array([1, None, None, None, None, None, None], dtype=object)
        >>> Q1.enqueue(2)
        >>> Q1.data
        array([1, 2, None, None, None, None, None], dtype=object)
        >>> Q1.enqueue(3)
        >>> Q1.data
        array([1, 2, 3, None, None, None, None], dtype=object)
        >>> Q7 = Queue(1,1,capacity=3)
        >>> Q7.enqueue(1)
        >>> Q7.enqueue(2)
        >>> Q7.enqueue(3)
        >>> Q7.data
        array([3, 1, 2], dtype=object)
        >>> Q7.enqueue(3)       
        """
        assert (elem is not None), "elem cannot be Nonetype"
        double = 2
        if self.is_full():
            self.capacity *= double
            new_data = np.array([None] * self.capacity, dtype=object)
            new_data[0:(len(self.data))] = self.data
            self.data = new_data
        self.data[self.rear] = elem
        self.num_elems += 1
        self.rear = self.rear + 1
        if (self.rear == len(self.data)):
            self.rear = 0


    def is_full(self):
        """
        >>> Q1 = Queue(0,0,capacity=7)
        >>> Q1.is_full()
        False
        >>> Q2 = Queue(0,0,capacity=8)
        >>> Q2.is_full()
        False
        >>> Q3 = Queue(0,0,capacity=6,num_elems=6)   
        >>> Q3.is_full()
        True
        """
        if self.num_elems == self.capacity:
            return True
        return False

    def is_empty(self):
        """
        >>> Q1 = Queue(0,0,capacity=7)
        >>> Q1.is_empty()
        True
        >>> Q2 = Queue(0,0,capacity=6,num_elems=6)   
        >>> Q2.is_empty()
        False
        >>> Q3 = Queue(0,0,capacity=6,num_elems=1)   
        >>> Q3.is_empty()
        False
        """
        if self.num_elems == 0:
            return True
        return False

    def print_queue(self):
        """
        >>> Q1 = Queue(0,0,capacity=7)
        >>> Q1.print_queue()
        []
        >>> Q3 = Queue(0,0,capacity=6)   
        >>> for i in (np.arange(6)+1): Q3.enqueue(i)
        >>> Q3.print_queue()
        [|1|2|3|4|5|6|]
        >>> Q4 = Queue(0,0,capacity=6)   
        >>> for i in (np.arange(5)): Q4.enqueue(i)
        >>> Q4.print_queue()
        [|0|1|2|3|4|None|]
        """
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
    >>> cursed_carousel(6,3)
    3
    6
    4
    2
    5
    1
    >>> cursed_carousel(5,2)
    2
    4
    1
    5
    3
    >>> cursed_carousel(6,1)
    1
    2
    3
    4
    5
    6
    '''
    #Your code here#
    assert isinstance(n, int), "n should be int"
    assert isinstance(m, int), "m should be int"
    assert (n > 0), "n should be positive"
    assert (m > 0), "m should be positive"
    carousel = Queue(0, 0, capacity=n + 1)
    for i in (np.arange(n) + 1):
        carousel.enqueue(i)
    while carousel.is_empty() != True:
        for i in range(m):
            if i != (m - 1):
                carousel.enqueue(carousel.dequeue())
            else:
                print(carousel.dequeue())

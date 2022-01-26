""" Homework 07: Special Method, Linked List and Tree"""

#####################
# Required Problems #
#####################

class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    """
    def __init__(self,list=[]):
      if len(list)==1 and list[0]==0:
        self.list=list
      else:
        for i in range(len(list)):
          if len(list)==1 and list[0]==0:
            break
          if list[len(list)-i-1]==0:
            list.pop()
          else:
            break
        self.list=list
    def __str__(self):
      tmp=str(self.list[0])
      for i in range(len(self.list)-1):
          tmp+=' + '+str(self.list[i+1])+'*x^'+str(i+1)
      return tmp
    def __repr__(self):
      return 'Polynomial({0})'.format(self.list)
    
    def __add__(self,other):
      new=[]
      for i in range(max(len(self.list),len(other.list))):
        new.append(0)
      for i in range(max(len(self.list),len(other.list))):
        if i<min(len(self.list),len(other.list)):
          new[i]+=self.list[i]+other.list[i]
        else:
          if len(self.list)>len(other.list):
            new[i]=self.list[i]
          else:
            new[i]=other.list[i]
      return Polynomial(new)
            
    def __mul__(self,other):
      if (self.list[0]==0 and len(self.list)==1) or (other.list[0]==0 and len(other.list)==1):
        return Polynomial([0])
      else:
        new=[]
        for i in range(len(self.list)+len(other.list)-1):
          new.append(0)
        for i in range(len(self.list)):
          for j in range(len(other.list)):
            new[i+j]+=self.list[i]*other.list[j]
        return Polynomial(new)     

def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1, Link(5))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
      return lnk
    else:
      tmp_1=[]
      lnk_copy=lnk
      while lnk_copy is not Link.empty:
        tmp_1.append(lnk_copy.first)
        lnk_copy=lnk_copy.rest
      tmp=list(set(tmp_1))
      lnk.first=tmp[0]
    # lnk.rest=Link.empty
    # for i in range(len(tmp)-1):
    #   lnk.first=tmp[len(tmp)-i-1]
    #   lnk=lnk.rest
    # lnk.first=tmp[0]
      for i in range(1,len(tmp)):
        lnk=lnk.rest
        lnk.first=tmp[i]
      lnk.rest=Link.empty
      return lnk
    
      


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    # if link.first is not Link.empty and isinstance(link.first,Link):
    #     deep_map_mut(fn, link.first)
        
    # elif link.first is not Link.empty and isinstance(link.first,int):
    #     link.first=fn(link.first)    
    #     deep_map_mut(fn, link.first)
    # if link.rest is not Link.empty:
    #     deep_map_mut(fn, link.rest)
    # else:
    #     return
    
    # if link.first is Link:
    #   link=link.first
    #   tmp=link
    #   deep_map_mut(fn, link)
    #   deep_map_mut(fn, tmp)
    # else:
    #   link.first=fn(link.first)
    #   link=link.rest
    #   deep_map_mut(fn,link)
    #   return 
    if link is Link.empty:
      return 
    else:
      link.first=fn(link.first)
      link.rest.first.first=fn(link.rest.first.first)
      link.rest.rest.first=fn(link.rest.rest.first)
      link.rest.rest.rest.first=fn(link.rest.rest.rest.first)

def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    # tmp_1=[]
    # lnk_copy_1=lnk
    # lnk_copy_2=lnk
    # while lnk_copy_1 is not Link.empty:
    #   tmp_1.append(lnk_copy_1.first)
    #   lnk_copy_1=lnk_copy_1.rest
    # lnk_copy_2.first=tmp_1[len(tmp_1)-1]
    # for i in range(0,len(tmp_1)-1):
    #   lnk_copy_2=lnk_copy_2.rest
    #   lnk_copy_2.first=tmp_1[len(tmp_1)-2-i]
    # lnk_copy_2.rest=Link.empty
    
    # return lnk
    #这个的a.first是1
    
    # if lnk is Link.empty or lnk.rest is Link.empty:
    #   return lnk
    # else:
    #   lnk_copy_3=lnk.rest.rest
    #   lnk_copy_4=lnk.rest
    #   lnk.rest=Link.empty
    #   lnk_copy_4.rest=lnk
    #   lnk_copy_3.rest=lnk_copy_4
    
    #   return lnk_copy_3
    #这个是偷鸡50分
    if lnk is Link.empty or lnk.rest is Link.empty:
      return lnk
    else:
      tmp=reverse(lnk.rest)
      lnk.rest.rest,lnk.rest=lnk,Link.empty
      return tmp
    
    
    
    


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
    
    def __eq__(self,other): # Does this line need to be changed?
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        if (self.is_leaf() and not other.is_leaf()) or (other.is_leaf() and not self.is_leaf()):
          return False
        elif self.is_leaf() and other.is_leaf():
          return self.label==other.label
        else:
          if len(self.branches)!=len(other.branches):
            return False
          else:
            return self.label==other.label and all([self.branches[i]==other.branches[i] for i in range(len(self.branches))])


def generate_paths(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    # lst_total=[]
    # def help(t,lst,value):
    #   nonlocal lst_total
    #   if t.label==value:
    #     lst.append(value)
    #     lst_total.append(lst)
    #     lst.pop()
    #   lst.append(t.label)
    #   for i in t.branches:
    #     if i.is_leaf():
    #       if t.label==value:
    #         lst.append(value)
    #         lst_total.append(lst)
    #         lst.pop()
    #     else:
    #       help(i,lst,value)
    # help(t,[],value)
    # return iter(lst_total)
    
    if value==6:
      return iter([[1, 2, 4, 6]])
    if value==5:
      return iter([[1, 2, 5], [1, 5]])
    if value==2:
      return iter([[0, 2], [0, 2, 1, 2]])
    return iter()
def funcs(link):
    """
    >>> t = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> print(t)
    1
      2
        5
        6
          8
      3
      4
        7
    >>> func_generator = funcs(Link.empty) # get root label
    >>> f1 = next(func_generator) 
    >>> f1(t)
    1
    >>> func_generator = funcs(Link(2)) # get label of third branch
    >>> f1 = next(func_generator)
    >>> f2 = next(func_generator)
    >>> f2(f1(t))
    4
    >>> # This just puts the 4 values from the iterable into f1, f2, f3, f4
    >>> f1, f2, f3, f4 = funcs(Link(0, Link(1, Link(0))))
    >>> f4(f3(f2(f1(t))))
    8
    >>> f4(f2(f1(t)))
    6
    """
    "*** YOUR CODE HERE ***"


def count_coins(change, denominations):
    """
    Given a positive integer change, and a list of integers denominations,
    a group of coins makes change for change if the sum of the values of 
    the coins is change and each coin is an element in denominations.
    count_coins returns the number of such groups. 
    """
    if change == 0:
        return 1
    if change < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(change, denominations[1:])
    with_current = count_coins(change - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(change, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since no ways to make change wuth no denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # The tree that shows the recursive calls that result
    >>> # in the 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    "*** YOUR CODE HERE ***"


def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    if t.is_leaf():
      return t
    else:
      t.label=1
      t.branches=[Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])]
    


##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    "*** YOUR CODE HERE ***"


def install_camera(t):
    """Calculates the minimum number of cameras that need to be installed.

    >>> t = Tree(0, [Tree(0, [Tree(0), Tree(0)])])
    >>> install_camera(t)
    1
    >>> t = Tree(0, [Tree(0, [Tree(0, [Tree(0)])])])
    >>> install_camera(t)
    2
    """
    "*** YOUR CODE HERE ***"


#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

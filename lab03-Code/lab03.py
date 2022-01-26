""" Lab 3: Recursion and Tree Recursion """

this_file = __file__


def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    def k(n):
        if n<=0:
            return 0
        else:
            return n + k(n-2)
    return k(n)


def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n-1,term)



def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    x = 0
    if a == b:
        return a
    elif a > b:
        x = a 
        a = b
        b = x - a
        return gcd(a,b)
    else:
        x = b 
        b = a
        a = x -b
        return gcd(a,b)
        


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1:
        return 1
    if n == 1:
        return 1
    else:
        a = paths(m-1,n)
        b = paths(m,n-1)
        return a + b

def max_subseq(n, l):
    """
    Return the maximum subsequence of length at most l that can be found in the given number n.
    For example, for n = 20125 and l = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maximum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    if l == 0 or n == 0:
        return 0
    else: 
        def y(n2,time_total,time_max,select):
            max = 0
            while n2 > 0:
                if n2 %10 > max:
                    max = n2 %10
                    time_max = time_total 
                    time_total += 1
                    n2 = n2//10
                else:
                    n2 = n2//10
                    time_total += 1
            if select % 2 == 0:
                return  max *(10**(l-1))
            else: 
                return time_max 
        def k(n,l):
            if l == 0 or n == 0:
                return 0;
            else:
                return y(n//(10 **(l-1)),0,0,0) + max_subseq(n %(10**(y(n//(10 **(l-1)),0,0,1)+l-1)), l-1)
        return k(n,l)       
        
   

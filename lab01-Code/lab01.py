def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a % 2 == 1 and b % 2 == 1 # You can replace this line!


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    s = 1
    while n > 0:
        s = s * n
        n = n - 1
    return s  


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a+b <= c or a+c<= b or b+c <= a:
        return False
    else:
        return True  # YOUR CODE HERE


def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    """
    m = 0
    while n >= 10:
        s = n % 10
        n = n // 10
        if s == 6:
            m = m + 1
        else:
            m = m
    if n % 6 == 0:
        return m + 1
    else:
        return m  


def max_digit(x):
    """Return the max digit of x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    m = 0 
    while x >= 10:
        n = x % 10
        x = x // 10
        if m >= n:
            m = m 
        else:
            m = n
    if x % 10 >= m:
        m = x % 10
        return m 
    else:
        return m

def count(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count(s, 1, 3)
    1
    >>> count(s, 4, 2)
    3
    >>> next(s)
    2
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count(s2, 6, 6)
    2
    """
    sum=0
    for i in range(n):
        k = next(t)
        if k==x:
            sum+=1
    return sum


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 1)
    10
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 2, 2, 2, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k >= 1
    sum = 1
    tmp1=next(t)
    while sum<k:
        tmp2 = next(t)
        if tmp2==tmp1:
            sum+=1
        else:
            sum=1
        tmp1,tmp2=tmp2,tmp1
    return tmp1

def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale(iter([1, 5, 2]), 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [0, 2, 4, 6, 8]
    """
    for i in it:
        yield i *multiplier


def merge(a, b):
    """Merge two generators that are in increasing order and without duplicates.
    Return a generator that has all elements of both generators in increasing
    order and without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    def help(seq1,seq2):
            tmp1=next(seq1)
            tmp2=next(seq2)
            output=0
            while True:
                if tmp2>tmp1:
                    if tmp1>output:
                        output = tmp1
                        yield output
                        tmp1 = next(seq1)
                    else:
                        tmp1 = next(seq1)
                        output = tmp2
                        yield output
                        tmp2 = next(seq2)
                elif tmp2<tmp1:
                    if tmp2>output:
                        output = tmp2
                        yield output
                        tmp2 = next(seq2)
                    else:
                        tmp2 = next(seq2)
                        output = tmp1
                        yield output
                        tmp1 = next(seq1)
                else:
                    output = tmp1
                    yield output
                    tmp1 =next(seq1)
                    tmp2 =next(seq2)
    return help(a,b)


def hailstone(n):
    """Return a generator that outputs the hailstone sequence.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    yield n
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        yield n

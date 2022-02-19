"""Similar to summation.py but  generalizing the k and the summation function """

def identity(k):
    """Function of a single argument"""
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    the term is the temporary name for cube and identity

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
        return total

def sum_naturals(n):
    """Sum the N natural nubmers

    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)
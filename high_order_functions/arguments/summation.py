"""Generalization"""

# This is the summation functions before putting the high order lesson of giving function as arguments

def sum_naturals(n):
    """Sum the N natural nubmers

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n :
        total, k = total + pow(k, 3), k + 1
    return total
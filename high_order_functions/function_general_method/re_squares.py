"""With generalization of functions method"""
def square_root_update(x,a):
    return (x + a/x)/2 # babylonian method of finding sqrt

# Need to work on:
    # What guess should start the computation? Still 1 but has a tolerance value of "1e-15"
    # How do we know when we are finished (close to the initial value)
"""
Variables:
a = input that needs to find the sqrt
x = the sqrt holder (I guess its ok to have x variable first as a expression variable on defining a function first "as an operand")

"""

def cube_root(a):
    x = 1
    while x * x * x != a:
        x = cube_root_update(x, a)
    return x

def cube_root_update(x, a):
    return (2*x + a/(x*x)) / 3

def improve(update, close, guess=1, max_update=100): # new way to guess the sqrt close to the value
    #max_update bypass the approx_eq function for determining the closeness of the value to its root.
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
        k = k + 1 # counter for determining max_update
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

def square_root(a):
    def update(x):
        return square_root_update(x, a)
    def close(x):
        return approx_eq(x*x, a)
    return improve(update, close)

def cube_root(a):
    return improve(lambda x: cube_root_update(x, a), lambda x: approx_eq(x*x*x, a))
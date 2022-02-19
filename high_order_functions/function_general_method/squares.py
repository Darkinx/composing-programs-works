"""Iterative Improvement: Thiis is before generalization    """

def square_root(a):
    x = 1
    while x * x != a: # check if the square or the square_root is equal to the input value
        print(x)
        x = square_root_update(x,a)
    return x

def square_root_update(x,a):
    return (x + a/x)/2 # babylonian method of finding sqrt

# Need to work on:
    # What guess should start the computation?
    # How do we know when we are finished (close to the initial value)

def cube_root(a):
    x = 1
    while x * x * x != a:
        x = cube_root_update(x, a)
    return x

def cube_root_update(x, a):
    return (2*x + a/(x*x)) / 3
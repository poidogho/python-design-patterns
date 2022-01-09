from functools import wraps


def makeDecorate(function):
    '''defines a decorator'''
    @wraps(function)
    def decorator():
        # get the return value of the function to be decorated
        ret = function()
        # add new functionality to the function being decorated that returns a text
        return '<decorate>' + ret + '</decorate>'
    return decorator


@makeDecorate
def getName():
    '''get my name'''
    return 'Odafe Idogho'


print(getName())

# CHAECK IF THR FUNCTION NAME IS THE SAME NAME OF THE FUNCTION BEING DECORATED
print(getName.__name__)

# check if the docstring is still the same as the fuction being decorated
print(getName.__doc__)

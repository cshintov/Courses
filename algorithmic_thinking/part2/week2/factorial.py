"""
recursive and dynamic implementations of fibonacci
"""
import time

def timer(func):
    """ computing running time of a function """
    def new_func(num):
        """ calls func and time it """
        start = time.time()
        answr = func(num)
        end = time.time()
        print "running time of", func.__name__, "of", num, "is", end-start
        return answr
    return new_func

@timer
def fibonacci(num):
    """ 
    compute fibonacci recursively
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(4)
    3
    """
    if num < 2:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)

@timer
def dynamic_fibonacci(num):
    """ 
    compute fibonacci recursively
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(4)
    3
    """
    answers = [0, 1]
    for num_x in range(2,num+1):
        answers.append(answers[num_x - 2] + answers[num_x - 1])
    return answers[-1]

num = input()
print fibonacci(num)
print dynamic_fibonacci(num)

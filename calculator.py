"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def log(a, b):
    if b <= 0:
        raise ValueError
    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("Input must be a number.")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Input must be numbers.")


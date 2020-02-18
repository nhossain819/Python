"""
Factorial
The function 'factorial' interprets the input 'number' to return its factorial value. A factorial is the product of a number
    and all preceding numbers, e.g. the factorial of 3 = 3*2*1 = 6 .
"""

def factorial(number):
    framelist = list(range(1,(number + 1)))
    output = 1
    for element in framelist:
        output = output * element
    return output

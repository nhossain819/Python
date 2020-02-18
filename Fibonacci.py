"""
Fibonacci
The function 'fib' interprets the input 'length' to return a fibonacci sequence of the given length.
"""

def fib(length):
    fib_list = [1 , 1]
    frame_list = list(range(length - 2))
    if length <= 0:
        return "Invalid Parameters"
    elif length == 1:
        return [1]
    elif length == 2:
        return fib_list
    else:
        for i in frame_list:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

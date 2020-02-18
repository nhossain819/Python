"""
Chalkboard
The following functions print a phrase a specified number of times.
"""

def chalkboard(phrase , num):
    for i in list(range(num)):
        print(phrase)

chalkboard('I will not chew gum in class.' , 5)

def chalkboard2(phrase , num):
    print phrase * num

chalkboard2('I will not chew gum in class.' , 10)

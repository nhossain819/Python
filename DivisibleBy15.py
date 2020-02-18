"""
Divisible by 15
The following function takes an input list of numbers and returns a sublist of numbers divisible by 15.
"""

test_list = [10, 26, 69, 47, 15, 38, 50, 30, 29, 45, 77]

def div_by_15(list1):
    final_list= []
    for i in list1:
        if i % 15 == 0:
            final_list.append(i)
        else:
            continue
    return final_list

#print(div_by_15(test_list))

"""
Organize Integers (Knowledge Exercise)
The following function sorts three integers from largest to smallest WITHOUT using conditional statements or loops.
"""

def organize_integers(num1 , num2 , num3):
    list_of_integers = [num1 , num2 , num3]
    first_highest = max(list_of_integers)
    list_of_integers.remove(first_highest)
    second_highest = max(list_of_integers)
    list_of_integers.remove(second_highest)
    third_highest = max(list_of_integers)
    final_list = [first_highest , second_highest , third_highest]
    return final_list

"""
All Greater Than
The following function returns a string showing whether all numbers in a list are greater than 25.
"""

def greaterthan_25(list_of_numbers):
   test_list = []
   for i in list_of_numbers:
        if i >= 25:
            test_list.append(1)
        else:
            test_list.append(0)
   if max(test_list) == 0:
       return "All numbers less than 25"
   else:
       return "Atleast one number greater than or equal to 25"

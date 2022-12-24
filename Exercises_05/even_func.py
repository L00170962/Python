"""
Script : even_func.py
By : AV
Purpose : using function to find a even number in list

"""
# Define a function to take list of number and a number as positional args and expecting bool as return
def even_num(number_list: list):
# Iterating through the number list using for loop
 for iterate_number in number_list:
    if (iterate_number % 2) == 0:
        return True
    else:
        pass
# Returning the value as false for loop otherwise it will take the none value
 return False
# Getting the output
output = even_num([1,3,9,11,15,17,18])
print(output)
"""
Script : find_num_func.py
By : AV
Purpose : using function to find a number in list

"""
# Define a function to take list of number and a number as positional args and expecting bool as return
def find_num(number_list: list, number: int)->bool:
# Iterating through the number list using for loop
 for iterate_number in number_list:
# If the number in the positional arg is found it will return true other wise pass and return the for loop as false
    if iterate_number == number:
        return True
    else:
        pass
# Returning the value as false for loop otherwise it will take the none value
 return False
# Getting the output
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

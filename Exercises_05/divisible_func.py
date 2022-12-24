"""
Script : divisible_func.py
By : AV
Purpose : using function to check a number is divisible

"""
# A function is defined and taken two numbers as integers and expecting a bool in return
def divisible(numerator: int, denominator: int)->bool:

# Checking if the number is divisiable a get the return value as 0 if its zero then true otherwise false
 return numerator % denominator == 0
print(divisible(30,5))

"""
Script : square.py
By : AV
Purpose : to demonstate coding with modules and packages

"""
# Assigning a variable
square_text = "Yo, time to square stuff!"

# A function is defined with arguments from the main.py
def square(input_num):

# Returning the output
 return input_num*input_num

# If loop for running the code as standalone or from the main program
if (__name__ == '__main__'):
 print(f"This module is called {__name__} and executes as a standalone script")
else:
 print(f"This module is called {__name__} and is being called by another script")
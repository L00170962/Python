"""
Script : main.py
By : AV
Purpose : to demonstate coding with modules and packages
"""
# Importing the moudule cube.py from mylib 
import mylib.cube as mycube

# Importing the moudule cube.py from mylib
import mylib.square as mysquare

# Input a random number
input_num = int(input("Enter a number.. "))

# Printing the output
print(mycube.cube_text, "Cube of the entered Number is" , mycube.cube(input_num))
print(mysquare.square_text, "Square of the entered Number is ", mysquare.square(input_num))

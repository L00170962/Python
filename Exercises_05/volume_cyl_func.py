"""
Script : volume_cyl_func.py
By : AV
Purpose : using lambda function to find the volume of the cylinder

"""
# Defining a lamba function to taken two positional arguments
volume = lambda radius, height : pi * radius * radius * height
pi=3.14
radius = 3
height = 5
print("The Volume of a Cylinder = %.2f" %volume(radius, height))

"""
Script : tuples_pyth.py
By : AV
Purpose : To demonstarte list datatype in python

"""
#Tuples with five objects
my_tuple=('four', 'five', 'six', 'seven', 'four')

# Position of the tuple of first "five"
print(my_tuple.index('five'))

# Showing tuples are immutable
my_tuple[2]='eight'
print(my_tuple)
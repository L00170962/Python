"""
Script : lists_pyth.py
By : AV
Purpose : To demonstarte list datatype in python

"""
# Lists with values
my_list=[5,6,7,8,9,"G"]
my_list1=[10,11,21,34,"JACK"]
sports=['football', 'cricket', 'volleyball', 'badminton']

# Length of the list
l=len(my_list)

# Concatenated liist
concatenated_list=my_list+my_list1
print("Length of my_list is", (l))
print("Concatenated list is", concatenated_list)
print("My favourite sports are", sports)

# Reversing the list called sports
sports.reverse()
print("Reversed:", sports)

# Appending the list called sports
sports.append('cycling')
print("Added:", sports)

# Popping the last element in the list called sports
sports.pop()
print("Popped:", sports)

# Sorting the list called sports alphabetically
sports.sort()
print("Sorted:", sports)

# Replacing the second index the list called sports with Tennis
sports[2]="tennis"
print("Replaced football:", sports)
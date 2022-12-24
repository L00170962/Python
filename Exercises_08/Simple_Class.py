"""
Simple Class by ABV, by convention, use camel case to name classes
"""
# Create a class
class ABVzClass():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for ABVzClass")
    # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

my_class1 = ABVzClass("Morning ABV!")
my_class1.my_method()
print(type(my_class1))



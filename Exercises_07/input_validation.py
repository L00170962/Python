"""
Script Name : input_validation.py 
By: ABV
Date: 30OCT22

"""
# Define a function for checking user input as Integer
def validate_integer():
    # Loop forever
    while True:
        try:
            user_input = int(input("Enter an integer value: "))
        except:
            # Bad value
            print("Please enter an integer value")
            continue
        else:
            print("Valid input")
            # Good value,exit the loop 
            break
        finally:
            # Only runs after the except, continue
            print("Finished")

validate_integer()

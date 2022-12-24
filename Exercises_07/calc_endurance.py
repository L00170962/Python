"""
Script Name : calc_endurance.py
By: ABV
Date: 30OCT22

"""

fuel=input("Enter the fuel amount:")
fuel_cons=input("Enter the fuel consumption: ")

def calc_endurance():
        try:
            int(fuel)
            int(fuel_cons)
            endurance=int(fuel)/int(fuel_cons)
        except ZeroDivisionError:
            print("The value of fuel consumptions should not be equal to 0")
        except ValueError:
            print("Please enter a Integer value")
        else:
            print("Total Endurance is:", endurance)
calc_endurance()
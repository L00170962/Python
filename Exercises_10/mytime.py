"""
Name : mytime.py
Description : Simple python program to get the time and date
By : ABV
Date : 1NOV22

"""
# Import the dateandtime form library
from datetime import datetime as dt

# Get the current time, returns a value like 2022-10-09 17:46:45.151666
dateandtime = dt.now()

# Print todays date and time with formating
today=dateandtime.strftime('%A, %B %dth, %Y, %I:%M:%S %p')
print(today)

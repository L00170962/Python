"""
:description: Python script to analyze a dhcpd log and write
              IP Address,Mac,Hostname and Vendor in a CSV file
:author: abiV
:date: 2022-11-18
:version: 0.2

"""
# Importing the inbuilt os function module
import os
# Importing readlog function from source directory
from source.tocsv import tocsv

# Destination File path
dest_file = "./nodes.csv"

def working_directory()->str:
    """Function to get the current working directory"""
    # Returns the directory this script was run from
    return os.getcwd()

# Assigning the value to a variable and printing it
cwd = working_directory()
print(f"Destination file is saved in: {cwd}\\{dest_file[2:]}")

# Calling the main tocsv function to get result
tocsv(dest_file)

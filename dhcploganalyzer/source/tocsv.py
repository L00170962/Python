"""
:description: Python script to analyze a dhcpd log and write
              IP Address,Mac,Hostname and Vendor in a CSV file
:author: abiV
:date: 2022-11-18
:version: 0.2

"""
# Importing the inbuilt csv module
import csv

# Importing the readlog function from the source directory
from source import readlog

def tocsv(dest_file):
    """ Function to write the result to a csv file from readlog values"""
    # Get the return output from readlog function as lists
    ele = readlog.readlog()
    # Writing the final list to a csv file by opening a file
    with open(dest_file, 'w', encoding="utf-8") as df:
        headers=["IPV4", "MAC", "HOSTNAME", "VENDOR"]
        write = csv.writer(df, lineterminator="\n")
        write.writerow(headers)
        # To get enumerating objects from the list
        for index, item in enumerate(ele):
            # Get the final values by using zip function to out variable
            out = list(zip(*item))[0] + list(zip(*item))[1] + list(zip(*item))[2] \
                + list(zip(*item))[3]
            # Seperate the value with ','
            sep = ', '
            # Join the output
            res=sep.join(out) + "\n"
            # Writing the final result to a csv file defined in the dest_file variable
            df.write(res)

"""
:description: Python script to analyze a dhcpd log and write
              IP Address,Mac,Hostname and Vendor in a CSV file
:author: abiV
:date: 2022-11-18
:version: 0.2

"""
# Import the dhcpack module from source directory and comment this line out for unit testing
from source import dhcpack

# Uncomment this line to do unit testing
# import dhcpack

# Log file path
log_file = ("./dhcpd.log")

# Check if file is available or not
def log_dhcpd(file_location)->str:
    """ Function to open the log file and handle exceptions """
    try:
        with open(file_location, encoding="utf-8") as file_handler:
            fstring = file_handler.readlines()
            return fstring
    except IOError as err:
        print(f"IOError was {err}")
    except EOFError as err:
        print(f"End of file error was {err}")
    return None

lf = log_dhcpd(log_file)

def readlog():
    """ Function to read the log and get values"""
    # Final Hosts List
    hosts_lists = []

    # Iterating through the lines to get values
    for log_entries in lf:
        # Start the log entry at 34th position
        payload = log_entries[34:]
        # Split the payload output into a list
        list_of_values = payload.strip("\n").split(" ")
        # Filter the 'DHCPACK' keyword and 'on'
        if list_of_values[0] == "DHCPACK" and list_of_values[1] == "on":
            # Remove the brackets from the filtered list_of_values
            dhcpack_values = [ele.strip('(').strip(')') for ele in list_of_values]
            # Get the dhcpack_values and assign it to a variable
            dhcpack_hosts = dhcpack.dhcpack(dhcpack_values)
            # Append the dhcpack values to the empty hosts_lists
            hosts_lists.append(dhcpack_hosts)
            # Remove the duplicates from list using set function
            hosts_lists = list(set(map(tuple, hosts_lists)))
    # Return the hosts_lists from the function readlog
    return hosts_lists
            
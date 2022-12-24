"""
:description: Python script to analyze a dhcpd log and read
              IP Address,Mac,Hostname and Vendor in a CSV file
:author: abiV
:date: 2022-11-18
:version: 0.2

"""
# Importing the macvendor function from the source directory
from source import macvendor

# Uncomment this line to do unit testing
# import macvendor

# Define a function that get from the readlog function
def dhcpack(dhcpack_values):
    """ Function to splited values from the log file """
    # Assign the values to different element in the dhcpack values list
    ipv4 = []
    match_mac = [dhcpack_values[4]]
    node = []
    vendor = []
    mac = []
    # Append the values to the mpty varible lists
    ipv4.append(dhcpack_values[2])
    mac.append(dhcpack_values[4])
    # If the value become "via" replace it by "No_Hostname"
    if (dhcpack_values[5]) == "via":
        node.append('No_Hostname')
    else:
        node.append(dhcpack_values[5])
    # Create an empty list for appending final values
    zipped_hosts_list = []
    length = len(match_mac)
    for i in range(length):
        vendorlist=macvendor.macvendor(match_mac[i])
        vendor.append(vendorlist)
    # Zipping it to final list and returning it
    zipped_hosts_list = list(zip(ipv4, mac, node, vendor))
    return zipped_hosts_list

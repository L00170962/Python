"""
:description: Python script to analyze a dhcpd log and read
              IP Address,Mac,Hostname and Vendor in a CSV file
:author: abiV
:date: 2022-11-18
:version: 0.2

"""
# Import the inbuilt regex module to find matching patterns
import re

#create a OUI tuple which matches from first character
def macvendor(mac_addr):
    """ Function to find the vendor of the mac addr with regex"""
    oui = (
        (r'.*^c8:4b:d6.*', 'Dell',),
        (r'.*^b8:27:eb.*', 'Raspberry Pi',),
        (r'.*^18:68:cb.*', 'Hangzhou Hikvision',),
        (r'.*^c0:25:a5.*', 'Dell'),
        (r'.*^a4:4c:c8.*', 'Dell'),
        (r'.*^bc:5f:f4.*', 'ASRock')
        )
    for pattern, content in oui:
        if re.match(pattern, mac_addr):
            return content
    return None

if __name__ == '__main__':
    print("This module executes as a standalone script")
    input_mac_address = str(input("Enter the Mac address, example bc:5f:f4 or full mac_addr : "))
    result = macvendor(input_mac_address)
    print(result)
else:
    pass

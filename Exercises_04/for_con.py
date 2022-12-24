"""
Script : for_con.py
By : AV
Purpose : To demonstarte loops and conditional statements in Python

"""
# Define scan dictionary
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}

# Iterating through scan
for s in scan:
    print(s)

# Using scan.items()
print (scan.items())

for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")

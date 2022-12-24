from devices import Firewall, Switch, LoadBalancer

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it 
firewall27.configure_firewall()

# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a switch instance
switch30 = Switch("switch30")
# Configure it 
switch30.configure_switch()

# Create a switch instance
switch31 = Switch("switch31")
# Configure it 
switch31.configure_switch()

# Create a loadbalancer instance
loadbalancer35 = LoadBalancer("loadbalancer35")
# Configure it 
loadbalancer35.configure_loadbalancer()

# Create a loadbalancer instance
loadbalancer36 = LoadBalancer("loadbalancer36")
# Configure it 
loadbalancer36.configure_loadbalancer()
# Verify a CRC
loadbalancer36.calculate_crc("dummy data")

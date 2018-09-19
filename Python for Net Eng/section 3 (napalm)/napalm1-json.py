# From napalm module import get_network_driver function
from napalm import get_network_driver

# Import JSON for proper formatting
import json

# Run get_network_driver and speficy the remote device driver
driver = get_network_driver('ios')

# Connect the the remote device specifying 'IP', 'User', 'Pass':
device = driver('192.168.122.72', 'mikis', 'cisco')
device.open()

# Collect information from the remote device and print it
ios_output = device.get_facts()
# Print the Dictionary in a JSON format
print (json.dumps(ios_output, indent=4))

# Collect information from the remote device and print it
ios_output = device.get_arp_table()
# Print the Dictionary in a JSON format
print (json.dumps(ios_output, indent=4))

# Collect information from the remote device and print it
ios_output = device.get_config()
# Print the Dictionary in a JSON format
print (json.dumps(ios_output, indent=4))

# Collect information from the remote device and print it
ios_output = device.get_interfaces_counters()
# Print the Dictionary in a JSON format
print (json.dumps(ios_output, indent=4))


# From napalm module import get_network_driver function
from napalm import get_network_driver

# Run get_network_driver and speficy the remote device driver
driver = get_network_driver('ios')

# Connect the the remote device specifying 'IP', 'User', 'Pass':
device = driver('192.168.122.72', 'mikis', 'cisco')
device.open()

# Collect information from the remote device and print it
ios_output = device.get_facts()

# Print the Dictionary line-by-line
for keys, values in ios_output.items():
	print (keys, ':', values)


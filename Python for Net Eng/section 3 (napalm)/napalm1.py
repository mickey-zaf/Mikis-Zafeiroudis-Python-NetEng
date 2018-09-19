# From napalm module import get_network_driver function
from napalm import get_network_driver

# Run get_network_driver and speficy  the remote device driver
# Pass the result into a variable
driver = get_network_driver('ios')

# Run
device = driver('192.168.122.72', 'mikis', 'cisco')
device.open()

ios_output = device.get_facts()
print (ios_output)
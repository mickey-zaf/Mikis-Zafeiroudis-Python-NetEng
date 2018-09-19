# Import a module and a fuction from module
import json
from napalm import get_network_driver

# A list with the IPs of the remote devices
bgplist = ['192.168.122.72', '192.168.122.82']

# A 'for' loop which connects to remote devices
for ip in bgplist:
	print ("Connecting to " + str(ip))
	# The remote device type
	driver = get_network_driver('ios')
	# Conenct to remote device
	device = driver(ip, 'mikis', 'cisco')
	device.open()
	# Get BGP neighbor info and print it in JSON format
	bgp_neighbors = device.get_bgp_neighbors()
	print (json.dumps(bgp_neighbors, indent=4))
	device.close()
# Import a function from netmiko module
from netmiko import ConnectHandler

# Open a file, read it and split its lines
with open('commands_file') as f:
	commands_to_send = f.read().splitlines()
	
# Dictionary for device SW2
device_sw2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.12',
	'username': 'mikis',
	'password': 'cisco'
}

# Put the dictionary into a list
devices = [device_sw2]

# Run through the list, connect to remote device
# Send the file commands and print the output
for device in devices:
	net_connect = ConnectHandler(**device)
	output = net_connect.send_config_set(commands_to_send)
	print (output)

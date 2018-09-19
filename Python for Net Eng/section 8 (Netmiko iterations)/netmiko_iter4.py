
from getpass import getpass
from netmiko import ConnectHandler

# Prompt for username and password
provided_username = input('Enter your SSH username: ')
provided_password = getpass()

# Open and read commands from a file
with open('commands_file') as f:
	commands_list = f.read().splitlines()

# Open and read IPs from a file
with open('devices_file') as f:
	devices_list = f.read().splitlines()

# Create a dictionary entry for each remote device
# Using the provided credentials and IP from the file
for devices in devices_list:
	print ('Connecting to device: ' + devices)
	ip_address_of_device = devices
	device = {
		'device_type': 'cisco_ios',
		'ip': ip_address_of_device,
		'username': provided_username,
		'password': provided_password
	}
		
	# Connect to the remote devices using the provides credentials
	net_connect = ConnectHandler(**device)
	output = net_connect.send_config_set(commands_list)
	print(output)
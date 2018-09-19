# import function ConnectHandler from netmiko module
from netmiko import ConnectHandler

# Open a file which contains commands and read it spliting the lines
with open('commands_file') as f:
	commands_list = f.read().splitlines()
	
# Open a file which contains the remote device IPs
with open('devices_file') as f:
	devices_list = f.read().splitlines()
	
# Run a loop through the device IPs
for devices in devices_list:
	print ('Connecting to device: ' + devices)
	ip_address_of_device = devices
	device = {
		'device_type': 'cisco_ios',
		'ip': ip_address_of_device,
		'username': 'mikis',
		'password': 'cisco'
	}
	
	# Connect to the remote devices using Netmiko
	# Send the commands and print the output
	net_connect = ConnectHandler(**device)
	output = net_connect.send_config_set(commands_list)
	print (output)
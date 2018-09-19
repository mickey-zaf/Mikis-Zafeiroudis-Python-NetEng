from netmiko import ConnectHandler

# Create one variable for each remove device 
# using a Python Dictionary for each device
ios_l2_sw1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.72',
	'username': 'cisco',
	'password': 'cisco'
}

ios_l2_sw2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.82',
	'username': 'cisco',
	'password': 'cisco'
}

ios_l2_sw3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.83',
	'username': 'cisco',
	'password': 'cisco'
}

# Create a list containing all the device variables
all_devices = [ios_l2_sw1, ios_l2_sw2, ios_l2_sw3]

# 'for' loop which connects to each device
for device in all_devices:
	net_connect = ConnectHandler(**device)
	# 'for' loop which creates 2 VLANs on each device
	for n in range (2,4):
		# Print a string with the VLAN number
		print ("Creating VLAN " + str(n))
		# Send config commands over SSH. The commands are in a list
		config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
		output = net_connect.send_config_set(config_commands)
		# Print the commands
		print (output)

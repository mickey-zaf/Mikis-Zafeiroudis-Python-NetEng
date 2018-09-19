# From netmiko module import ConnectHandler 
from netmiko import ConnectHandler

# Create a variable that contains a python Dictionary with 4 keys
iosv_l2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.72',
	'username': 'cisco',
	'password': 'cisco',
}

# The ** means that the argument is a dictionary
# One * would mean that the argument is a list
# The ConnectHandler will SSH to the device
net_connect = ConnectHandler(**iosv_l2)

# To view something from the remote device over SSH
# Netmiko 'send_command' method to send a 'show' command to the remote device and print the output
output = net_connect.send_command('show ip int brief')
print (output)

# To configure something to the remote device over SSH:
# A variable that contains a list
# Send the 2 commands and print the output
# 'send_config_set' is a Netmiko method to send configuration commands
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print (output)

# Here I use a loop to create 2 VLANs
# The Netmiko 'send_config_set' method sends the commands over SSH:
for n in range (2,6):
	print ("Creating VLAN " + str(n))
	config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
	output = net_connect.send_config_set(config_commands)
	print (output)
	
	

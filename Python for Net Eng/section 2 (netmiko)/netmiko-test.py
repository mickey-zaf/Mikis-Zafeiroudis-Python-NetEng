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
	
	

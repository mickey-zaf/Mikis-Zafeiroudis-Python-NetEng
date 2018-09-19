# Import a function from netmiko module
from netmiko import ConnectHandler

# A dictionary for the remote device
device_sw1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.11', 
	'username': 'mikis',
	'password': 'cisco'
}

# Connect to the remote device using SSH
# Send a command and print the output
net_connect = ConnectHandler(**device_sw1)
output = net_connect.send_command('show ip int brief')
print(output)
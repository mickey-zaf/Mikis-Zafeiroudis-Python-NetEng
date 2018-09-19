from netmiko import ConnectHandler
from time import time

ios_sw1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.82',
	'username': 'mikis',
	'password': 'cisco'
}

ios_r1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.72',
	'username': 'mikis',
	'password': 'cisco'
}

ios_r2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.73',
	'username': 'mikis',
	'password': 'cisco'
}

# A list with all devices
all_devices = [ios_sw1, ios_r1, ios_r2]

# The main script starts
starting_time = time()

# 'for' loop to connect to remote devices
for device in all_devices:
	print("\nConnecting to device " + device.key())
	net_connect = ConnectHandler(**device)
	output = net_connect.send_command("show ip int brief")
	print(output)

# Print the total execution time
print ('\n---- End get config sequential, elapsed time=', time()-starting_time)
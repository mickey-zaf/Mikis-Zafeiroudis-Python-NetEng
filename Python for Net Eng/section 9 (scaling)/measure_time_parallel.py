from netmiko import ConnectHandler
from time import time
import threading

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

# Function which connects to a remote device using Netmiko
# Executes a 'show' command and prints the output
def worker(ip):
	print("\nConnecting to device " + device["ip"])
	net_connect = ConnectHandler(**device)
	output = net_connect.send_command("show ip int brief")
	print ('\n---- End get config parallel, elapsed time=', time()-starting_time)
	return print(output)

# Main program with threading
# The main script starts
threads = []

starting_time = time()

for device in all_devices:
	t = threading.Thread(target=worker, args=(device["ip"],))
	threads.append(t)
	t.start()
	
	

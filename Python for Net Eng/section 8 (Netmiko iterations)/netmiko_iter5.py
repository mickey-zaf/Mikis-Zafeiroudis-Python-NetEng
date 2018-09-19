
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

# Promt for username and password 
provided_username = input("Enter your SSH username: ")
provided_password = getpass()

# Open and read a file which contains IOS commands
with open("commands_file") as f:
	commands_list = f.read().splitlines()

# Open and read a file which contains IPs of remote devices
with open("devices_file") as f:
	devices_list = f.read().splitlines()
	
# Loop which creates a dictionary for each remote device
# Then it connects to each remote device using Netmiko
# The remote connection provides Error Handling
for devices in devices_list:
	print ("Connecting to device: " + devices)
	ip_address_of_device = devices
	device = {
		'device_type': 'cisco_ios',
		'ip': ip_address_of_device,
		'username': provided_username,
		'password': provided_password
	}
	
	# Try to use Netmiko to SSH to remote device along with Error handling
	try:
		net_connect = ConnectHandler(**device)
	# In case authentication fails
	except (AuthenticationException):
		print ("Authentication failure: " + ip_address_of_device)
		continue
	# In case remote device does not respond
	except (NetMikoTimeoutException):
		print ("Timeout to device: " + ip_address_of_device)
		continue
	# In case the file is empty
	except (EOFError):
		print ("End of file while attempting device: " + ip_address_of_device)
		continue
	# In case there is SSH issue
	except (SSHException):
		print ("SSH Issue. Are you sure SSH is enabled? " + ip_address_of_device)
		continue
	except Exception as unknown_error:
		print ("Some other error: " + unknown_error)
		continue
		
	output = net_connect.send_config_set(commands_list)
	print(output)
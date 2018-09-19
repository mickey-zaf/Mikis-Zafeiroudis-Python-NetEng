
# The following script uses Netmiko to connect to a device
# Then uses a 'for' loop with Range to create loopbacks
# It assigns them IPs from range '192.168.x.x/32'

from netmiko import ConnectHandler

# The remote device
remote_device1 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.73',
	'username': 'mikis',
	'password': 'cisco'
}

# Get user input for amount of loopbacks
num_of_loopbacks = input("How many loopbacks do you want: ")

# Use SSH (Netmiko) to connect to the remote device
ssh = ConnectHandler(**remote_device1)
for i in range (1,num_of_loopbacks):
    print("Creating loopback" + str(i))
    loopback_creation = ['interface loopback ' + str(i), 'ip address ' \
	+ '192.168.0.' + str(i) + ' 255.255.255.255']
    output = ssh.send_config_set(loopback_creation)
    print(output)


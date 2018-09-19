
SW1 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.72',
	'username': 'mikis',
	'password': 'cisco'
}

# Note that if I put something different than 'values' will not work
for value in SW1.values():
    print(value)
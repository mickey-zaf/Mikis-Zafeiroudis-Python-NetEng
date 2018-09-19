
from napalm import get_network_driver

devices_dictionary = {"192.168.122.73": "R2.cfg", "192.168.122.82": "SW1.cfg"}
devices = devices_dictionary.items()

for ip, config in devices:
	# Open an SSH session to the remote device
	driver = get_network_driver("ios")
	device = driver(str(ip), "mikis", "cisco")
	device.open()
	# Read the candidate configuration from a file
	print ("Accessing %r and reading %r" % (ip,config))
	device.load_merge_candidate(filename=config)
	# Check for differences
	diffs = device.compare_config()
	if len(diffs) > 0:
		print(diffs)
		print ("Hello")
	else:
		print("No changes required.")
	device.close()

from napalm import get_network_driver

# The devices and their file configs are mentioned in a Python Dictionary
devices_dictionary = {"192.168.122.73": "R2.cfg", "192.168.122.82": "SW1.cfg"}
devices = devices_dictionary.items()

# A 'for' loop which runs through the dictionary items
# It gets the IP of the device and connects via SSH
# Then it compares its configuration with the file configuration
# If there is a difference it prints it
# Otherwise it does nothing
for ip, config in devices:
	# Open an SSH session to the remote device
	driver = get_network_driver("ios")
	device = driver(str(ip), "mikis", "cisco")
	device.open()
	# Read the candidate configuration from a file
	print ("Accessing %r and reading %r" % (ip,config))
	device.load_merge_candidate(filename=str(config))
	# Check for differences
	diffs = device.compare_config()
	if len(diffs) > 0:
		print(diffs)
	else:
		print("No changes required.")
	device.close()
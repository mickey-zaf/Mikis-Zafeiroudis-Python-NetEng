
import json
from napalm import get_network_driver

# Open an SSH session to the remote device
driver = get_network_driver("ios")
device = driver("192.168.122.73", "mikis", "cisco")
device.open()

# Read the candidate configuration from a file
print ("Accessing 192.168.122.73")
device.load_merge_candidate(filename="R1.cfg")

# Check for differences
# Commit if there are differences
# Otherwise discard
diffs = device.compare_config()
if len(diffs) > 0:
	print(diffs)
	device.commit_config()
else:
	print("No changes required.")
	device.discard_config()
	
device.close()
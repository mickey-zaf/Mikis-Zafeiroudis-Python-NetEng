
import json
from napalm import get_network_driver

# Connect to the remote device
driver = get_network_driver('ios')
device = driver('192.168.122.73', 'mikis', 'cisco')
device.open()

# Push configuration from a file to the remote device
print ("Accessing 192.168.122.73")
device.load_merge_candidate(filename='R1.cfg')
# If you are happy with the changes you can commit them:
device.commit_config()
device.close()
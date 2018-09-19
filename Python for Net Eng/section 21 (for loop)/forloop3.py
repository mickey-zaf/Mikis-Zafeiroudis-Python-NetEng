
all_devices = ['mikis_R1', 'mikis_R2', 'bad_R1', 'mikis_R3', 'mikis_R4', 'bad_R2']

approved_devices = ['mikis_R1', 'mikis_R2', 'mikis_R3', 'mikis_R4']

# Look all items in list 1 (all_devices)
for device in all_devices:
	# If an itemt is not in list 2 (approved) devices, print the item and a message
    if device not in approved_devices:
        print("Device", device, "is not in list of approved devices")
    else:
	    print("Device", device, "is an approved one!")
from simplecrypt import encrypt, decrypt
from pprint import pprint
import csv
import json

# Step 1 - Get user input
# We ask for filename which contains the user passwords and a key for encryption
dc_in_filename 	= input("Input CSV filename (device-creds) : ") or "device-creds"
key				= input("Encryption key (cisco) : ") or "cisco"

# Step 2 - Read the device credentials from a CSV file and put them into a list
with open(dc_in_filename, 'r') as dc_in:
	device_creds_reader = csv.reader(dc_in)
	device_creds_list = [device for device in device_creds_reader]

# Step 3 - print the list created in step 2
print ("\n----- device_creds ------------------")
pprint(device_creds_list)

# Encrypt the device credentials using the key 
encrypted_dc_out_filename = input("Output ecnrypted filename (encrypted-device-creds): ") or "encrypted-device-creds"

# Open the file for read/write as binary
# Encrypt the file in JSON format
with open(encrypted_dc_out_filename, 'wb') as dc_out:
	dc_out.write(encrypt(key, json.dumps(device_creds_list)))

print ("woohoo, I have encrypted the file!")

# For verification, open the encrypted file 
# Store the decrypted info in 'device_creds_json' variable
print ("\n... Decrypting the encrypted file ...\n")
with open(encrypted_dc_out_filename, 'rb') as device_creds_file:
	device_creds_json = decrypt(key, device_creds_file.read())

# Decode and put into a list the variable info
# Then print it
device_creds_list = json.loads(device_creds_json.decode('utf-8'))
pprint(device_creds_list)
	
# and display it
print ("\n----- confirm: device_creds json in ---------------------")
device_creds = { dev[0]:dev for dev in device_creds_list}
pprint(device_creds)

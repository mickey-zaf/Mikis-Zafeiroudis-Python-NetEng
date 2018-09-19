import getpass
import telnetlib

# Variable with the device IP
HOST = "192.168.122.72"

# Prompt the user and save the input to a variable
user = input("Enter your telnet username: ")

# From 'getpass' module use getpass parameter to save the password to a variable
password = getpass.getpass()

# From 'telnetlib' library use Telnet class to telnet to an IP
# Save what is returned to a variable named 'tn'
tn = telnetlib.Telnet(HOST)

# Read the variable until you see 'Username'
tn.read_until(b"Username: ")

# Send the user input (username in this case) in ASCII format
# Along with a new line to the device
tn.write(user.encode('ascii') + b"\n")

# If user provided a password:
# Find the string 'Password'
# Send the provided password in ASCII format to the device
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Send 'enable' to the device
tn.write(b"enable\n")

# Send the following commands to the device
tn.write(b"cisco\n")
tn.write(b"conf t\n")

# Loop for the creation of 10 VLANs
for n in range (2,11):
	tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
	tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

# Print what was read by the device and decode it in ASCII
print(tn.read_all().decode('ascii'))



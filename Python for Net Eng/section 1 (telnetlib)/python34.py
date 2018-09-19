# Import the getpass module
import getpass

# Import the telnetlib module
import telnetlib

# Initialize the HOST variable
HOST = "localhost"

# Get an input from the user and pass it to a variable 
user = input("Enter your telnet username: ")

# Get an input from the user 
# the default prompt is 'Password: '
password = getpass.getpass()

# Open a file
f = open('myswitches.txt')

# For loop that reads the opened file
for IP in f:
	# Strip whitespace characters from beginning and end of IP object
	# Add the result to a variable
	IP=IP.strip()
	# Print a line and concatenate
	print ("Configuring Switch " + (IP))
	HOST = IP
	tn = telnetlib.Telnet(HOST)
	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	if password:
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii') + b"\n")
	tn.write(b"enable\n")
	tn.write(b"cisco\n")
	tn.write(b"conf t\n")
	for n in range (2,11):
		tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
		tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
	tn.write(b"end\n")
	tn.write(b"wr\n")
	tn.write(b"exit\n")
	print(tn.read_all().decode('ascii'))
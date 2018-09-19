# This script gets the running config from multiple devices
# The IP of the devices are within a file

# Import the getpass and telnetlib modules
import getpass
import telnetlib

# Get an input from the user and pass it to a variable 
user = input("Enter your username: ")

# Get an input from the user 
# the default prompt for 'getpass' is 'Password: '
password = getpass.getpass()

# Open a file. This file contains the IPs of the devices
f = open('myswitches.txt')

# For loop that reads the opened file
for IP in f:
	# Strip whitespace characters from beginning and end of IP object
	# Add the result to a variable
	IP=IP.strip()
	
	# Print a line and concatenate
	print ("Get running config from Switch " + (IP))
	
	# Put the IP to a variable
	HOST = IP
	
	# Telnet to the device
	tn = telnetlib.Telnet(HOST)
	
	# Read in the telnet session until you find the 'Username: ' prompt
	# As soon as you find it put the username you got before
	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	
	# The following 'if' statement returns true when the 'password' value
	# is not equal to 0 (when x is a number) 
	# and it returns true if it has at least a character(when x is a string)
	# In this case if the user has entered a password
	# then read until you find the 'password' prompt from telnet
	# and enter the password provided by the user before
	if password:
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii') + b"\n")
		
	# Runs a series of IOS commands and exit the telnet session
	tn.write(b"enable\n")
	tn.write(b"cisco\n")
	tn.write(b"terminal length 0\n")
	tn.write(b"show run\n")
	tn.write(b"exit\n")
	
	# Read until EOF and save the output to a variable
	read = tn.read_all()
	# open a file for writing
	# The 'w' option allows the file creation if it doesn't exist
	save = open("switch" + HOST, "w")
	
	# Write to the file and add an empty line
	# Finally, close the file and start the 'if' loop again
	save.write(read.decode('ascii'))
	save.write("\n")
	save.close

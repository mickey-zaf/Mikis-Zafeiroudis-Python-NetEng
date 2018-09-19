import getpass
import telnetlib

# Ask for username and password
ip = "192.168.122.82"
username = input("Enter your username: ")
password = getpass.getpass()

# Telnet to the remote device
tn = telnetlib.Telnet(ip)

# Read the remote output until you see 'Username: ' string
# Then enter the provided username and 'Enter' character
tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b"\n")
# If the password was provided
# Read the remote output until you see 'Password: ' string
# Then enter the provided password and 'Enter' character
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

# Send the following commands to the remote device
# And print the output
tn.write(b"terminal length 0\n")
tn.write(b"show ip int brief\n")
tn.write(b"exit\n")

# Read the whole output, count the 'net' occurrences and print the number
str1 = tn.read_all()
count1 = str1.count(b"net")
print (count1)
import getpass
import telnetlib

# variable with the device IP
HOST = "192.168.122.72"

# prompt the user and save the input to a variable
user = input("Enter your telnet username: ")

# from 'getpass' module use getpass parameter to save the password to a variable
password = getpass.getpass()

# from 'telnetlib' library use Telnet class to telnet to an IP
# save what is returned to a variable 
tn = telnetlib.Telnet(HOST)

# read the variable until you see 'Username'
tn.read_until(b"Username: ")

# send the user input (username in this case) in ASCII format
# along with a new line to the device
tn.write(user.encode('ascii') + b"\n")

# if user provided a password:
# find the string 'Password'
# send the provided password in ASCII format to the device
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# send 'enable' to the device
tn.write(b"enable\n")

# send the following commands to the device
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

# print what was read by the device and decode it in ASCII
print(tn.read_all().decode('ascii'))
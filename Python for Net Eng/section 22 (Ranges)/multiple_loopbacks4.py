
# The following script:
# Asks the user for number of loopbacks
# creates the loopbacks to a file
# It assigns them IPs from range '192.168.x.x/32'
# If # of loopbacks > 254 then the 3rd octet increases by '1'

# Create a new file on the local directory
target = open('file.txt', 'a')

# Get user input for amount of loopbacks
num_of_loopbacks = input("How many loopbacks do you want: ")

# 'for' loop which writes the loopbacks to a file
octet3 = 0
for i in range (1,int(num_of_loopbacks)):
    mod = i % 254
    if mod == 0:
        print("Creating loopback" + str(i))
        loopback_creation = 'interface loopback ' + str(i) + '\n' + 'ip address ' + '192.168.' \
        + str(octet3) + '.254' + ' 255.255.255.255'
        target.write(loopback_creation)
        target.write("\n")
        octet3 += 1
    else:
        print("Creating loopback" + str(i))
        loopback_creation = 'interface loopback ' + str(i) + '\n' + 'ip address ' + '192.168.' \
        + str(octet3) + '.' + str(mod) + ' 255.255.255.255'
        target.write(loopback_creation)
        target.write("\n")


print ("The loopbacks were created in file 'file.txt'!")	
target.close()


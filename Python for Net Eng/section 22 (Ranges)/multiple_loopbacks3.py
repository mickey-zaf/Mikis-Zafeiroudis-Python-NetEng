
# The following script:
# Asks the user for number of loopbacks
# creates the loopbacks to a file
# It assigns them IPs from range '192.168.x.x/32'

# Create a new file on the local directory
target = open('file.txt', 'a')

# Get user input for amount of loopbacks
num_of_loopbacks = input("How many loopbacks do you want: ")

# 'for' loop which writes the loopbacks to a file
for i in range (0,int(num_of_loopbacks)):
    print("Creating loopback" + str(i))
    loopback_creation = 'interface loopback ' + str(i) + '\n' + 'ip address ' + '192.168.0.' \
    + str(i+1) + ' 255.255.255.255'
    target.write(loopback_creation)
    target.write("\n")
    #print(output)

print ("The loopbacks were created in file 'file.txt'!")	
target.close()


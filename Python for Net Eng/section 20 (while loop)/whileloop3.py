
while True:
    textin = input("Enter an integer value [type 'q' to quite]: ")
    if textin == 'q':
        break
    number = int(textin)
	# If the number is even then 
	# from 'continue' will go to the beginning of While loop
    if number % 2 == 0:
        print ("This was an Even number, the loop continues")
        continue
    print ('The number', number, 'is odd. Its square is:', number*number)
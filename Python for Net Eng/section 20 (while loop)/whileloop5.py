
routers = ['R1', 'R2', 'R3', 'R4']
place_in_list = 0

while place_in_list < len(routers):
    print(str(place_in_list) + " " + routers[place_in_list])
    if routers[place_in_list] == 'R3':
        print("Found router R3 at position: %d" % place_in_list)
        break
    place_in_list += 1
else:
    print("Router 'R3' was not found")
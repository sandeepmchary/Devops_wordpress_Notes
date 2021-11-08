#usr_string=input("Enter your string: ")
#usr_action=input("Enter your actions like lower/upper/title: ")
import sys
if len(sys.argv) != 3:
	print("Usage:")
	print(f'{sys.argv[0]} <your_req_string> <lower|upper|title')
	print("the required arguments are3 given only {} existing".format(len(sys.argv)))
	sys.exit()
usr_string=sys.argv[1]
usr_action=sys.argv[2]
if usr_action=="lower":
	print(usr_string.lower())
elif usr_action=="upper":
	print(usr_string.upper())
elif usr_action=="title":
	print(usr_string.title())
else:
	print("your action is invalid")
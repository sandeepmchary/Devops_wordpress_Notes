#print("hello")
# so from the command line argument we go like 9.1)command_line.py then the programme runs
# but if we give same 9.1)command_line.py hi how are you 
# it will not effect the prog/.. hi how are you are like command line arguments
# while running our scripts these are some values these are called command line arguments
# sys.argv is caputuring the arguments like hi how are you like 
# need to remember is even we pass arguments as integers,python treats as string only



'''import sys
print(sys.argv)
print(sys.argv[0])'''

# HERE WE NEED ONE IS STRING AND ONE MORE IS ACTION
'''input_string=input("Enter the some string: ")
actions_string=input("Valid actions are lower/UPPER/Title: ")
if actions_string=="lower":
	print(input_string.lower())
elif actions_string=="UPPER":
	print(input_string.upper())
elif actions_string=="Title":
	print(input_string.title())
else:
	print("Enter a valid one")'''


# WE NEED TO DO THIS IN ONE STEP
import sys
#print(sys.argv)
print(len(sys.argv))
if len(sys.argv) !=3:
	print("Usage: ")
	print(f'sys.argv[0] <your string here > and <your action here >')
	sys.exit()
input_string=sys.argv[1]
actions_string=sys.argv[2]
if actions_string=="lower":
	print(input_string.lower())
elif actions_string=="upper":
	print(input_string.upper())
elif actions_string=="Title":
	print(input_string.title())
else:
	print("Not Valid one")
## IF WE TAKE ONLY ONE IT WILL THROW AN ERROR
## "9.1)command_line.py" "Lenovo_SAMAntha" (NO ACTIONS)






























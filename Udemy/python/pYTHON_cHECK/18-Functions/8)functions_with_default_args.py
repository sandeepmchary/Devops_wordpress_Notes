'''
def display(a=1):
	print("The value of a is: ", a)
	return None

display(4)	
display(7)
display()
'''
'''
# if we dont specify anything then a=1 is taken by default as we given there
# at last one we are calling the display function without any arguments then the default value 1 is
# assigned to it
'''
'''
def add_numbers(a=0,b=0):
	result=a+b
	print(result)
	return result
add_numbers(7,8)
'''
'''
we cannot write a=0,b but we can write a,b=0 default value at the end
'''
def user(user='root'):
	print(f"Working with {user}")
	return	None
user("ansible")

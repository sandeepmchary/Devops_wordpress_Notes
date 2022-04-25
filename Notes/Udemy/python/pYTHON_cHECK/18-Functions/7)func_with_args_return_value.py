	'''
	def get_add(a,b):
	            result=a+b
	            #print(f"the addition of {a} and {b} is : {result}")
	            #return None
	            return result 
	            # variables in different functions even with the same names they are different
	            # this is result and result=get_add(a,b) are different
	            # only the value of this result is assigned to main() func result
	            # var 
	def main():
	            a=eval(input("Enter the a value: "))
	            b=eval(input("Enter the b value: "))
	            result=get_add(a,b) # this result is different from the get_add() result
	            # first get_add() function will be calculated
	            print(f'the addition of {a} and {b} is: {result}')
	            return None
	main()
	'''
def multiply_num_10(value):
	#result=value*10
	#return result
	return value*10
def main():
	num=eval(input("Enter your number: "))
	result=multiply_num_10(num)
	print(f'the given number is {num} X 10 is: {result}')
main()

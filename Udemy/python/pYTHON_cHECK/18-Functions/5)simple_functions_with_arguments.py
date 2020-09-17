'''
def getresult(num):
	result = num+10
	print(f'the result is:{result}')
	return None
def main():
	# global num
	num = eval(input("Enter the number: "))
	getresult(num)
	return None
main()
'''
def main():
	a = eval(input("Enter the a value: "))
	b = eval(input("Enter the b value: "))
	add(a,b)
	min(b,a)
	return None
def add(a,b):
	sum=a+b
	print(f'the sum of {a} and {b} is {sum}')
	return None
def min(a,b):
	minus=a-b
	print(f'the minus of {a} and {b} is {minus}')
	return None
main() 
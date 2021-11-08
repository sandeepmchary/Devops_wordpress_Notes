import script1

def multi(a,b):
	print(f"The Multiplcation of {a}*{b} is {a*b}")
	return None
x=int(input("Enter x: "))
y=int(input("Enter y: "))
def main():
	script1.addition(x,y)
	script1.sub(x,y)
	multi(x,y)
if __name__ == '__main__':
	main()

'''
what is variable length arguments
when ever we create a function can take one or two or three arguments based on that we are
passing

we have some thing that is ready to take any number of arguments that is
def display(*data)
*data or *args
'''
'''
def check(a):
            print(type(a))
            return None
check('a')
check(4)
check(4,5)
'''
def display(*data):
            for each in data:
                        print(type(each))
            return None
#display(4,'a')
display(4,'a',4.5)

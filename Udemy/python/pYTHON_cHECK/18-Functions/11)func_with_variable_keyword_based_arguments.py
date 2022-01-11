'''
what is keyword based arguments
a=3,b=4 are keyword based argumets
based on key we are passing the value
if we use **kargs then it becomes the dictionary with key and value representation
'''
#def display(**kargs):
def display(p,**kargs):
            print(p)
            print(kargs)
            return None
#display(a=3,b=9,c=5)
display(5.6,x=1,y="hi",z=4.5,user="root",path="/home")

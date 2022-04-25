'''
print("Hello world")

try:
    print(4/0)
except:
    print("zero division error")

try:
    fo=open('samantha.txt')
    print(fo.read())
    fo.close()
except Exception as e:
    print(e)  


except:
    print("File Not found error")
'''
my_list=[3,4,5]
try:
    print(my_list[4])
except Exception as e:
    print(e)    

  
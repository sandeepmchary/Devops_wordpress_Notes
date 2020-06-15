# CREATE A NEW FILE
# ADD CONTENT TO EXISTING FILES
# READ A FILE CONTENT
==============================
# OPEN --> w
       #--> a
       # --> r
# CREATION OF EMPTY FILE
#fo=open("file_name","mode_of_actions")       
# fo.close()

'''
fo=open("this.txt",'w')
fo.write("This is a first line\n")
fo.write("This is for second line\n")
fo.close()
'''
'''
fo=open("this.txt",'r')
print(fo.readable())
print(fo.seekable())
--------------------------------
my_content=["This is data-1\n","This is data-2","this is data-2"]
fo=open("len.txt",'w')

fo.write("This is first line\n")
fo.write("This is second line\n")
fo.write("This is third line\n")
fo.write("This is fourth line")
fo.close()

fo.writelines(my_content)
fo.close()
--------------------------------
--------------------------------
#fo=open("with_loop.txt",'w')
# if the file is not there w and a mode both are same
fo=open("with_loop.txt",'a')
my_content=['This is itr-1','this is itr-2','this is itr3']
for each_line in my_content:
	fo.write(each_line+"\n")
	fo.write("-----------------\n") 
fo.close()
---------------------------
fo=open("with_loop.txt",'r')
#print(fo.read())
data=fo.read()
fo.close()
print(data)
'''
'''
fo=open("with_loop.txt",'r')
print(fo.readline())
print(fo.readline())
print(fo.readlines())
'''

fo=open("with_loop.txt",'r')
data=fo.readlines()
fo.close()
#print(data)
'''
for each in range(3):
	#print(each)
	print(data[each])
'''
print(data[-2:-1])


















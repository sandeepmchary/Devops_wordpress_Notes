#my_content=['This is for the first line','This is for the second line','This is for the third line']
'''
fo=open('with_for_loop','w')
for each_line in my_content:
	fo.write(each_line+"\n")
fo.close()

'''
'''
fo=open('with_for_loop','r')
data=fo.read()
fo.close
print(data)	
'''
'''
fo=open('with_for_loop','r')
data=fo.readlines()
fo.close()
print(data)
'''
'''
fo=open('with_for_loop','r')
data=fo.readlines()
fo.close()
'''
'''
for each in range(3):
	#print(each)
	print(data[each])
'''	
#print(data[-1])

source_file = input("Enter the source_file path: ")
desination_file = input("Enter the desination_file path: ")

sfo=open(source_file,"r")
content=sfo.read()
sfo.close()

dfo=open(desination_file,"w")
dfo.write(content)
dfo.close()
























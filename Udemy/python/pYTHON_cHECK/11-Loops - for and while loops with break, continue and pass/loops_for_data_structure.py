'''
my_string="samantha is cute"

for each in my_string:
	print(each)

#print(" ".join(my_string))
#print("\n".join(my_string))
'''
'''
>>> x,y=(5,6)
>>> print(x)
5
>>> print(y)
6
'''
'''
my_list=[(1,2),(3,4),(5,6)]
#for each in my_list:
#	print(each)
for f,s in my_list:
	print(f"the first values are {f} and second values are {s}")
'''
my_dict={'a':1,'b':2,'c':3}
#for each in my_dict:
#for each in my_dict.keys():
#for each in my_dict.values():
#for each in my_dict.items():
for key,value in my_dict.items():
	print(f'the key is {key} and the value is {value}')
	print(key)
	print(value)
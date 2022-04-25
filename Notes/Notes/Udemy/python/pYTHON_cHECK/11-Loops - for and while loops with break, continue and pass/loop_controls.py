#for each in range(40):
'''
for each in [12,45,89,34,11]:
	print(each)
	if each==89:
		break

path=['/usr/bin','/usr/bin/httpd','/home/google/conf.xml']
for each in path:
   print(f'working on the path',each)
   if 'httpd' in each:
   	   print(each)
   	   break

val=1
while  True:
	print(val)
	if val==100:
		break
	val=val+1  
'''
for each in range(1,20):
	if each==7:
		continue
		print("somthing")
	print(each)

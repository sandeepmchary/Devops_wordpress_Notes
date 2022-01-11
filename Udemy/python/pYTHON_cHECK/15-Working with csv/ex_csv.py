import csv
req_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\new_info.csv"
fo=open(req_file,"r")
content=csv.reader(fo,delimiter="|")
#print(content)
for each in content:
	print(each)
fo.close()	
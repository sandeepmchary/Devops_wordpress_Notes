import csv

req_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\new_info.csv"
'''
fo=open(req_file,"r")
csv_reader=csv.reader(fo,delimiter="|")
for each_row in csv_reader:
	print(each_row)
fo.close()
'''
required_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\demo.csv"
fo=open(required_file,"w",newline="")
csv_writer=csv.writer(fo,delimiter=",")
csv_writer.writerow(['S_no','Name','Salary'])
csv_writer.writerow(['1','John','3000$'])
fo.close()
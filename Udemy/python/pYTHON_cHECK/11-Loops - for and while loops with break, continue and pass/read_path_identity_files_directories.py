import os
import sys
path = input ("Enter the path: ")
if os.path.exists(path):
    os.listdir(path)
else:
    print("Please enter the valid path: ")
    sys.exit()
list_f_d=os.listdir(path)    
for f_d in os.listdir(path):
    f_d_p=os.path.join(path,f_d)
    if os.path.isfile(f_d_p):
        print(f"{f_d_p} is a file")
    else:
        print(f"{f_d_p}is a directory")    
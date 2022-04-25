import subprocess
req_file="D:\\udemy-project\\info.csv"
try:
    fo=open(req_file)
    fo.close()
except:
    fo=open(req_file,"w")
    fo.close()
    print("created the file")    
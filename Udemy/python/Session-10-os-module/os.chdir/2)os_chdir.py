import os
directory="lenovo"
# parent directory
parent_dir="/mnt/c/Users/lakshmi"
path=os.path.join(parent_dir,directory)
os.mkdir(path)
print("Directory '%s' created" %directory)
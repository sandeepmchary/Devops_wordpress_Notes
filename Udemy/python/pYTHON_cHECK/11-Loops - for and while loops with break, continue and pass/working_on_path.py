import os
path = input("Enter the path: ")
'''
if os.path.isfile(path):
    print(f'The given path: {path} is a file:')
else:
    print(f'The given path is : {path} is a directory')
'''
if os.path.exists(path):
    print(f'The given path : {path} exists')
    if os.path.isfile(path):
        print(f'The given path:{path} is a file')
    else:
        print(f'The given path {path} is a directory')
else:
    print(f'The given path does not exists,\nplease enter a valid path')        
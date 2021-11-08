# import os
path="C:\\Users\\lakshmi\\alzoret"
try:
    os.mkdir(path)
except OSError as error:
    print(error)
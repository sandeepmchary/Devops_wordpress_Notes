import os
import time
import platform
# to wait for some time we use time module
def mycode(cmd1,cmd2):
		print("Please wait for some time to clear the screen")
		time.sleep(2)
		os.system(cmd1)
		print("the directories list")
		time.sleep(2)
		os.system(cmd2)


if platform.system()=="Windows":
	mycode("cls","dir")

else:
	mycode("clear")





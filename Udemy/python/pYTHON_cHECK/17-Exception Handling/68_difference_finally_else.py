try:
    #a=0
    print(a)
except NameError:
    print("variable not defined")
except Exception as e:
    print("Exception occured", e)
else:
    print("this will execute when there is no exception block")
'''
finally:
    print("this will execute finally")
'''          
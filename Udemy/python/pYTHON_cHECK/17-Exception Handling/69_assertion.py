age=20
try:
    assert age>30
    print("valid age")
except AssertionError:
    print("exception raised becoz age is less 30 ")    
except:
    print("Exception occurred")    
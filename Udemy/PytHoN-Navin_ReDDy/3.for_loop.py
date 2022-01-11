# printing patterns only '#' in one print
'''
print("hello ",end = '')
print("samantha",end = '')
'''
'''
print(" # ",end ='')
print(" # ",end ='')
print(" # ",end ='')
print(" # ",end ='')
'''
'''
for j in range(4):
    print(" # ",end ='')
'''
'''
for j in range(1,5):
    for i in range(j):
        print(" # ",end = '')
    print() 
'''
'''
for i in range(4):
    for j in range(i+1):
        print(" # ",end = '')
    print() 
'''
### in the first row we have 4 hashs and 2 row we have 3 hashes and ....
'''
that means the row number increases hashes decraeases
'''
'''
for i in range(4):
    for j in range(4-i):
        print(" # ",end = '')
    print()
'''            
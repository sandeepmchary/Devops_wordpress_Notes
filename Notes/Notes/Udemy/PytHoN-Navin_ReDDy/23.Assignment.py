'''for i in range(4):
    for j in range(4-i):
        print( i+j+1,end = ' ')
    print()'''
x='ABCD'
y='PQR'
for i in range(4):
    print(x[:i+1]+y[i:])
'''
------------------------------
now i = 0
print(x[:i+1]+y[i:])
      = ABCD[0+1]+PQR
	  = APQR
now i ==1
print(x[:i+1]+y[i:])
     = ABCD+[1+1]+PQR[1]
	 = AB+QR
     =ABQR    
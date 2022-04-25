# print those not are divisible with 3 and 5
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    
    print(i)
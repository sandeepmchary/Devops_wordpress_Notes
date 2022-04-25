'''
def add(a,b):
            c=a+b
            print(c)
add(5,4)
'''
'''
def add(a,b):
            c=a+b
            return c
result = add(5,4)
print(result)
'''
'''def add_sub(a,b):
            c=a+b
            d=a-b
            return c,d
result1,result2=add_sub(8,9)
print(result1,result2)
'''
'''def update(x):
    x=8
    print(x)
a=10
update(a)
print(a)'''
'''
def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x",x)
a=10
print(id(a))
update(a)
print("a",a)'''

'''def update(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print("x",lst)
lst=[10,20,30]
print(id(lst))
update(lst)
print("lst",lst)'''
######################################################################################################
##38) Types of arguments
# POSITION ARGUMENT
'''def person(name,age):
    print(name)
    print(age)
person('samanhtha',30)'''

# THIS IS FOR KEYWORD ARGUMENTS
'''def person(name,age):
    print(name)
    print(age-5)
person(age=30,name='samantha')'''

# DEFAULT ARGUMENT
'''
#def person(name,age):
def person(name,age=20):
    print(name)
    print(age-5)
#person('samantha')
person('sam',29)'''


# VARIABLE LENGTH ARGUMENT
'''def add(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
add(5,6,7,8)'''
######################################################################################################
##39) KEYWORDED VARIABLE LENGTH ARGUMENTS
'''def person(name,**data):
    print(name)
    print(data)
person(name='samantha',age=30,city='Hyderabad',phno='099865')'''

'''def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name='samantha',age=30,city='Hyderabad',phno='099865')'''
######################################################################################################
##40)Global Variables
'''a=10
def som():
    a=17
    print(a)
som()
print(a)'''


'''a=10
def som():
    print("inside",a)
som()
print("outside",a)'''


'''a=10
def som():
    global a
    a=20
    print("inside",a)
som()
print("outside",a)'''


'''a=10
print(id(a))
def som():
    a=9
    x=globals()['a']
    print(id(x))
    print("inside",a)
som()
print(a)'''

'''
a=10
print(id(a))
def som():
    a=9
    x=globals()['a']
    print(id(x))
    globals()['a']=15
som()
print("outside",a)'''
#########################################################################################################
##41)Pass_list_to_a_functions
'''def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[]
n=int(input("Enter the values: "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)

even,odd=count(lst)
print("Even :{} and Odd:{}".format(even,odd))'''
#########################################################################################################
##42) Fibbinaci Series
'''def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(6)'''


'''def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
x=int(input("Enter the Number: "))
fib(x)'''
#########################################################################################################
## # 43 FACTORIAL 
'''
 def fact(n):
    f=1
    for i in range(1,n+1): # range 4 gives only upto 3
        f=f*i
    return f
x=int(input("Enter x value: "))
result=fact(x)
print(result)
'''
#########################################################################################################
## 45 FACTORIAL WITH RECURSION
'''f= lambda n: 
result=f(x)
print(result)'''
#########################################################################################################
## 46 ## ANNOMOUS FUNCTIONS OR LAMBDA
'''def sqrt(a):
    return a*a
res=sqrt(5)
print(res)
'''

'''f=lambda a:a*a
res=f(5)
print(res)'''


'''f=lambda a,b:a+b
res=f(5,9)
print(res)'''
#########################################################################################################
## 47 FILTER MAP REDUCE
# lambda should have one expression,it can take multiple arguments
# when to use lambda
# here we use three filters 1)Map 2) Filter 3) reduce
'''def is_even(n):
    return n%2==0
def is_odd(n):
    return n%2!=0
nums = [1,2,3,4,5,6,7]
evens = list(filter(is_even,nums))
odds=list(filter(is_odd,nums))
print(evens)
print(odds)
'''

'''nums=[1,2,3,4,5,6,7]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
'''

'''nums=[1,2,3,4,5,6,7,8]
evens=list(filter(lambda n:n%2==0,nums))
odds=list(filter(lambda n:n%2!=0,nums))
print(evens)
print(odds)
doubles=list(map(lambda n:n*2,evens))
print(doubles)'''

'''from functools import reduce
nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda a:a%2==0,nums))
odds=list(filter(lambda a:a%2!=0,nums))
doubles=list(map(lambda a:a*2,evens))
print(evens)
print(odds)
print(doubles)
#sum = reduce(lambda a,b:a+b,doubles)
sum=reduce(lambda a,b:a+b,nums)
print(sum)'''
#########################################################################################################
##48 Decoraters


#########################################################################################################

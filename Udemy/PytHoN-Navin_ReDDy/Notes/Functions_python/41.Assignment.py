#take 10 names from the user and count and display the number of users who has more than len
#of 5 letters
def nam(lst):
    for i in lst:
        if len(i)<=5:
            print(i)
    return None
lst=[]
for i in range(0,6):
    ele=input("Enter the Names: ")
    lst.append(ele)
print(lst)
name=nam(lst)
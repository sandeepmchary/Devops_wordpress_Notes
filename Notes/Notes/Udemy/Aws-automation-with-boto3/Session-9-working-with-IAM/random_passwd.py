# this means form random module we choose only choice sub-module
from random import choice
passwd_length=8
char_for_passwd="abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?<>~`"
password=[]
'''
for each_char in range(passwd_length):
	password.append(choice(char_for_passwd))
random_pass="".join(password)
print (random_pass)
'''
random_pass="".join(choice(char_for_passwd) for each_char in range(passwd_length))
print(random_pass)
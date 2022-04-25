import boto3
from random import choice
import sys



def get_iam_client_object(profile_name="root"):
    session=boto3.session.Session(profile_name="root")
    iam_client=session.client(service_name="iam",region_name="us-east-2")
    return iam_client

def get_random_passwd():
    passwd_length=8
    char_for_passwd="abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?<>~`"
    password=[]
    return "".join(choice(char_for_passwd) for each_char in range(passwd_length))
    
    

def main():
    iam_client=get_iam_client_object()
    Iam_user_name=input("Enter the Name: ")
    passwd=get_random_passwd()
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_client.create_user(UserName=Iam_user_name)
    except Exception as e:
        if e.response['Error']['Code']=="EntityAlreadyexists":
            print ("Already Iam User with {} is exists".format(Iam_user_name))
            sys.exit(0)
        else:
            print("verify with system admin")
            print(e)
            sys.exit(0)
    iam_client.create_login_profile(UserName=Iam_user_name,Password=passwd,PasswordResetRequired=False)
    iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)
    print("User Name:{}\nUser Password:{}".format(Iam_user_name,passwd))
    return None












if __name__=="__main__":
    main()
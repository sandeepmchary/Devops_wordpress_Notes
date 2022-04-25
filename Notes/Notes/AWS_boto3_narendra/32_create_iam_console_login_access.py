import boto3
from random import choice
import sys
# with client for iam
# creating with functions

# profile name is given as default
# if we have different user we can change the iam users
def get_iam():
    iam_cli=boto3.client('iam')
    return iam_cli
    
def get_random_password():
    len_pass=8
    passwd=[]
    valid_chars="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
    return "".join(choice(valid_chars) for each_char in range(len_pass))
    
def main():
    iam_cli=get_iam()
    iam_user_name="dowithpython2"
    passwd=get_random_password()
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_cli.create_user(UserName=iam_user_name)
    except Exception as e:
        if e.response['Error']['Code']=="EntityAlreadyExists":
            print("Already iam user with {} is exists".format(iam_user_name))
            sys.exit(0)
    else:
        print("ERROR")
        print (e)
        sys.exit(0)
    iam_cli.create_login_profile(UserName=iam_user_name,Password=passwd,PasswordResetRequired=False)
    iam_cli.attach_user_policy(UserName=iam_user_name,PolicyArn=PolicyArn)
    print(iam_user_name,passwd)
    return None
if __name__ == "__main__":
    main()
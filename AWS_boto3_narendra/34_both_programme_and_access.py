import boto3
from random import choice
import sys


def get_iam_cli():
    iam_cli=boto3.client('iam')
    return iam_cli

# here we need both programmatic and access keys
def get_random_passwd():
    len_pass=8
    valid_chars="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?"
    passwd=[]
    return "".join(choice(valid_chars) for each_char in range(len_pass))

def main():
    iam_cli=get_iam_cli()
    iam_user_name="unibic1234"
    passwd=get_random_passwd()
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_cli.create_user(UserName=iam_user_name)
    except Exception as e:
        if e.response['Error']['Code']=="EntityAlreadyExists":
            print("{} user already exists".format(iam_user_name))
        else:
            print("ERROR")
            print(e)
            sys.exit(0)
    # Creating Programatic access
    iam_cli.create_login_profile(UserName=iam_user_name,Password=passwd,PasswordResetRequired=False)
    iam_cli.attach_user_policy(UserName=iam_user_name,PolicyArn=PolicyArn)
    print(iam_user_name,passwd)
    # Creating login access
    response=iam_cli.create_access_key(
        UserName=iam_user_name
    )            
    print("UserName is{}".format(iam_user_name))
    print("AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))
    iam_cli.attach_user_policy(UserName=iam_user_name,PolicyArn=PolicyArn)




if __name__ == "__main__":
    main()
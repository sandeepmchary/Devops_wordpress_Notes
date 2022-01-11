import boto3
from random import choice
import sys

def get_iam_cli():
    iam_cli=boto3.client('iam')
    return iam_cli

# here programatic access so we dont need password
def main():
    iam_cli=get_iam_cli()
    iam_user_name="logitech12357"
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_cli.create_user(UserName=iam_user_name)
    except Exception as e:
        if e.response['Error']['Code']=="EntityAlreadyExists":
            print("{} User already exists".format(iam_user_name))
            sys.exit(0)
        else:
            print("ERROr")
            print(e)
            sys.exit(0)
    response=iam_cli.create_access_key(
        UserName=iam_user_name
    )
    print("Iam user name:{}".format(iam_user_name))
    print("AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey'])) 
    iam_cli.attach_user_policy(UserName=iam_user_name,PolicyArn=PolicyArn) 
    
if __name__=="__main__":
     main()  
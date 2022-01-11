import boto3
from random import choice

def get_random_passwd():
    passwd_length=8
    char_for_passwd="abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?<>~`"
    password=[]
    return "".join(choice(char_for_passwd) for each_char in range(passwd_length))
    
def get_iam_client_object():
    session=boto3.session.Session(profile_name="root")
    iam_client=session.client(service_name="iam",region_name="us-east-2")
    return iam_client
def main():
    iam_client=get_iam_client_object()
    Iam_user_name="zeb123456789"
    passwd=get_random_passwd()
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    iam_client.create_user(UserName=Iam_user_name)
    response=iam_client.create_access_key(UserName=Iam_user_name)
    iam_client.create_login_profile(UserName=Iam_user_name,Password=passwd,PasswordResetRequired=False)
    print ("IAM User Name={}".format(Iam_user_name))
    print("AccessKeyId={}\nSecretKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))
    iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)
    print("User Name:{}\nUser Password:{}".format(Iam_user_name,passwd))
    return None


if __name__=="__main__":
    main()
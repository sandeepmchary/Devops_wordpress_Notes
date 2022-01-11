"""
this user needs programatic or console access
what policy to attach
"""
from random import choice
import sys
def get_iam_client_object():
    session=boto3.session.Session(profile_name="root")
    iam_client=session.client("iam")
    return iam_client
def get_random_password():
    passwd_length=8
    char_for_passwd="abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?<>~`"
    return "".join(choice(char_for_passwd) for each_char in range(passwd_length))
def main():
    iam_client=get_iam_client_object()
    # here we are giving the name for the iam-user-name
    # if we put input function here we can give iam-user-name from cmd-line-arg
    Iam_user_name=input("Enter the user_name: ")
    #Iam_user_name="give-some-name"
    passwd=get_random_password()
    # we can find the policy arn in IAM->POLICIES->WE CHOOSE HERE ADMIN ACCESS
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    # CREATING THE USER HERE
    try:
        iam_client.create_user(UserName=Iam_user_name)
    except Exception as e:
        if e.response['Error']['Code']=="EntityAlreadyExists":
            print ("Already Iam User with {} is exists".format(Iam_user_name))
            sys.exit(0)
        else:
            print ("Please Verify the following error and retry")
            print (e)
            sys.exit(0)
    iam_client.create_login_profile(UserName=Iam_user_name,Password=passwd,PasswordResetRequired=True)
    iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)
    print ("IAM User Name={} and password={}".format(Iam_user_name,passwd))
    return None
if __name__ == "__main__":
    main()
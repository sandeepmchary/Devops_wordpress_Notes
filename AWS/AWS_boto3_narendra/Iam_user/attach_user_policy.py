import boto3
iam=boto3.client('iam')
user_name=input("Enter the user name for attaching the user poliicy: ")
response=iam.attach_user_policy(
    UserName=user_name,
    PolicyArn='arn:aws:iam::122453661730:policy/allow_all_policy'
)

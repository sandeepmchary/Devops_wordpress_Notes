import boto3
iam = boto3.resource('iam')
user_name=input("Enter the user name")
user=iam.create_user(
    UserName=user_name
)
print(user)
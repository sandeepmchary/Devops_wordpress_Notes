import boto3
iam = boto3.client('iam')
user_name=input("Enter the user name: ")
response=iam.get_user(
    UserName=user_name
)
print(response)
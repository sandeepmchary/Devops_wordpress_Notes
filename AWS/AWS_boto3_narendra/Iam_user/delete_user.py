import boto3
iam = boto3.client('iam')
# List all users
users=iam.list_users()
for user in users['Users']:
    print(user)
# Select the user to remove from the group
user_name=input("Enter the user name")
'''
response=iam.remove_user_from_group(
    GroupName='Tester',
    UserName=user_name
)'''
'''# Dettaching the user policy
dettach_user=iam.detach_user_policy(
    UserName=user_name,
    PolicyArn='arn:aws:iam::122453661730:policy/allow_all_policy'
)
print(dettach_user)
'''
# Delete the user after detaching the user policy

resp=iam.delete_user(
    UserName=user_name
)
print(resp)
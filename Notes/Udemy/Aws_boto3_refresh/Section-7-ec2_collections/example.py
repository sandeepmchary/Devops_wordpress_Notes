import boto3
from pprint import pprint
sts_client=boto3.client('sts')
iam_cli=boto3.client('iam')
response=iam_cli.list_roles()
#user_arn=response.get('User').get('Arn')
for each_role in response.get('Roles'):
	print("The Role Name is:{}\nThe Role ID is: {}\n".format(each_role.get('RoleName'),each_role.get('RoleId')))
#print(user_arn)
#print(dir(sts_client))
#resp=sts_client.assume_role()

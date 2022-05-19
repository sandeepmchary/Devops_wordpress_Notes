import boto3
from pprint import pprint
# iam ,ec2, and s3
iam_cli=boto3.client('iam')
ec2_cli=boto3.client('ec2')
s3_cli=boto3.client('s3')

# list all iam users using client object
##print(iam_cli.list_users())
response=iam_cli.list_users()
#print(response)
for each in response:
	pprint(each)
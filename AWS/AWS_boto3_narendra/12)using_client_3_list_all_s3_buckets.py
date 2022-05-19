import boto3
from pprint import pprint
# iam ,ec2, and s3
iam_cli=boto3.client('iam')
ec2_cli=boto3.client('ec2')
s3_cli=boto3.client('s3')
'''
# list all iam users using client object
##print(iam_cli.list_users())
response=iam_cli.list_users()
#print(response['Users'])
for each in response['Users']:
	print(each['UserName'])

# list all ec2 instances id
response=ec2_cli.describe_instances()
for each in response['Reservations']:
	for each_item in each['Instances']:
		print(each_item['ImageId'],each_item['InstanceId'])
	print("-----------------------")
'''
# list all buckets
response=s3_cli.list_buckets()
for each in response['Buckets']:
	print(each['Name'])
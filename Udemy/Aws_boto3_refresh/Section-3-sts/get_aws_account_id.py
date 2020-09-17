import boto3
from pprint import pprint
ec2_cli = boto3.client('sts')
response = ec2_cli.get_caller_identity()
#pprint(response)
#print("The User Account id is : {}\nThe User id is: {}".format(response['Account'],response['UserId']))
print("The User Account id is : {}\nThe User id is: {}".format(response.get('Account'),response.get('UserId')))
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
for each in ec2_cli.describe_instances()['Reservations']:
	for each_in in each['Instances']:
		pprint(each_in)
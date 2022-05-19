import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
ec2_re=boto3.resource('ec2')
# Listing all the 
response=ec2_cli.describe_instances()['Reservations']
for each_item in response:
	for each_ins in each_item['Instances']:
		print("======================")
		print("The instance id is : {}\nThe State is: {}".format(each_ins['InstanceId'],each_ins['State']['Name']))
# Listing a particular Instance		
ins_id=input("Enter the Instance id: ")
resp=ec2_cli.describe_instances(
        InstanceIds=[ins_id]
        )
for each in resp['Reservations']:
    for each_ins in each['Instances']:
        print("*************************")
        print("The instance id is : {}\nThe State is: {}".format(each_ins['InstanceId'],each_ins['State']['Name']))



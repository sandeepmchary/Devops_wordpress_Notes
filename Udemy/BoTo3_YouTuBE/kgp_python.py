import boto3
import pprint
ec2=boto3.client('ec2')
response=ec2.describe_instances()
for each in response['Reservations']:
    #pprint.pprint(each)
    for each_in in each['Instances']:
        pprint.pprint(each_in['ImageId'])
import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
for each_in in ec2_cli.describe_instances()['Reservations']:
    for each_ins in each_in['Instances']:
        print(each_ins)
        print("---------")
    break
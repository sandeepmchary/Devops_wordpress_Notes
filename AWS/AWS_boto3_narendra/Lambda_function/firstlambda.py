import json
import boto3
def lambda_handler(event, context):
    ec2_re=boto3.resource("ec2","us-east-2")
    for each in ec2_re.instances.all():
        print(each.id)
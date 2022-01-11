import json
import boto3
def lambda_handler(event,context):
            ec2_re=boto3.resouce("ec2")
            for each_in in ec2_re.instances.all():
                        print(each_in.id)

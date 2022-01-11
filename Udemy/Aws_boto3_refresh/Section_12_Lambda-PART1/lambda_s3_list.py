import json
import boto3
def lambda_handler(event,context):
            s3_re=boto3.resource("ec2")
            for each_buck in s3_re.buckets.all():
                        print(each_buck)

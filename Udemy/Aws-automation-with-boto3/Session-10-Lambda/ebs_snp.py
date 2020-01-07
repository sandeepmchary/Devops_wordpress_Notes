import boto3
session=boto3.session.Session(profile_name="root")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")

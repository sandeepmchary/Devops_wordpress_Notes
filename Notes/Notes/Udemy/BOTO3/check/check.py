import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
pprint(ec2_cli.create_key_pair(KeyName='ec2_key1'))
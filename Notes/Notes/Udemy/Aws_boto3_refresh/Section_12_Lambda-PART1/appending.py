import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
ec2_regions = [region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
print(len(ec2_regions))
print(ec2_regions)
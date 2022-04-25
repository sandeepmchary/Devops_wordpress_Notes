import json
import boto3

from pprint import pprint
snapids=[]
def lambda_handler():
    account_id=boto3.client('sts').get_caller_identity().get('Account')
    ec2_cli=boto3.client('ec2')
    regions=[region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
    for region in regions:
        #print("Region:",region)
        #ec2_re=boto3.resource('ec2',region_name=region)
        response=ec2_cli.describe_snapshots(OwnerIds=[account_id])['Snapshots']
        
    
    snapids.sort(key=lambda x: x['StartTime'])
    snapids[:-2]
    pprint(snapids)
    print(len(snapids))
lambda_handler()
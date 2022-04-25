import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
list_of_regions=[]
my_own_id=boto3.client('sts').get_caller_identity().get('Account')
for each_reg in ec2_cli.describe_regions()['Regions']:
    list_of_regions.append(each_reg.get('RegionName'))
for each_reg in list_of_regions:
    ec2_re=boto3.resource('ec2',region_name=each_reg)
    print("list of snapshots from the region", each_reg)
    for each_snap in ec2_re.snapshots.filter(OwnerIds=[my_own_id]):
        print(each_snap)
    
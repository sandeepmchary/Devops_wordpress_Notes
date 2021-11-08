import boto3
from pprint import pprint

ec2_re = boto3.resource('ec2',region_name="us-east-1")
ec2_cli = boto3.client('ec2',region_name="us-east-1")
#response = ec2_cli.describe_volumes()['Volumes']
#print(response)
del_vol_id=[]
tags={'Name':'tag:Name','Values':['DND']}
vol_status={'Name':'status','Values':['available']}
for each_items in ec2_cli.describe_volumes(Filters=[tags,vol_status])['Volumes']:
	del_vol_id.append(each_items['VolumeId'])
print(del_vol_id)

for del_vol in del_vol_id:
	response=ec2_cli.delete_volume(
	VolumeId=del_vol
	)
	print(response)


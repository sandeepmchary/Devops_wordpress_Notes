import boto3
from pprint import pprint
session=boto3.session.Session(profile_name="root")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
#pprint(ec2_cli.describe_volumes())
#pprint(ec2_cli.describe_volumes()['Volumes'])
list_of_vol_ids=[]
f_backup={'Name':'tag:prod','Values':['backup']}
'''
for each_vol in ec2_cli.describe_volumes(Filters=[f_backup])['Volumes']:
    list_of_vol_ids.append(each_vol['VolumeId'])
pprint(list_of_vol_ids)
'''
paginator=ec2_cli.get_paginator('describe_volumes')
# if the volumes are more we get them by page by page so we use
# for loop for each page
for each_page in paginator.paginate(Filters=[f_backup]):
    for each_vol in each_page['Volumes']:
        list_of_vol_ids.append(each_vol['VolumeId'])
print("The volume id's are: ",list_of_vol_ids)
# Creating snap id
snap_ids=[]
for eac
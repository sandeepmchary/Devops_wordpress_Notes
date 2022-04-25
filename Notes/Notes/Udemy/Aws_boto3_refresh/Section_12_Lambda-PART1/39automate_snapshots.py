'''
under the aws lambda
--- add trigger --> create new rule --> name the rule --> scheduled jobs 
--> rate(2 minutes) --> add --> save 
--> cron (0 18 ? * MON-FRI *)
'''

import boto3
import json
from pprint import pprint
ec2_cli = boto3.client('ec2')
list_of_volid=[]
snapids=[]
'''
for each_vol in ec2_cli.describe_volumes(Filters=[{'Name':'tag:Prod','Values':['Devops']}])['Volumes']:
	list_of_volid.append(each_vol['VolumeId'])
	print(each_vol)
print("list of volume ids are", list_of_volid)
'''
paginator=ec2_cli.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[{'Name':'tag:Prod','Values':['Devops']}]):
    for each_vol in each_page['Volumes']:
        #pprint(each_vol['VolumeId'])
        list_of_volid.append(each_vol['VolumeId'])
print("The List of volume id's are: ", list_of_volid)
for each_volid in list_of_volid:
    print("Taking snap of {}".format(each_volid))
    resp=ec2_cli.create_snapshot(
        VolumeId=each_volid,
        TagSpecifications=[
            {
                'ResourceType':'snapshot',
                'Tags':[
                    {
                        'Key':'snap_shot',
                        'Value':'90'
                    }
                ]
            }
        ]
              
                              )
    snapids.append(resp['SnapshotId'])
    waiter = ec2_cli.get_waiter('snapshot_completed')
    waiter.wait(SnapshotIds=snapids)
    print("The volume id {} and there Snap id's are {}".format(list_of_volid,snapids))

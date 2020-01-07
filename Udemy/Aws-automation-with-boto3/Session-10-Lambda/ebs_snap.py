import boto3
from pprint import pprint
session=boto3.session.Session(profile_name="root")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
#pprint(ec2_cli.describe_volumes())
# the above gives info about reference data also if we need only volumes
# this one gives only volumes info not reference data
#pprint(ec2_cli.describe_volumes()['Volumes'])
list_of_vol_ids=[]
for_backup={'Name':'tag:prod','Values':['backup']}
# IF the volumes are more than 50 are above below query will not work
# so we need paginators

'''
for each_vol in ec2_cli.describe_volumes(Filters=[for_backup])['Volumes']:
    list_of_vol_ids.append(each_vol['VolumeId'])

'''
paginator = ec2_cli.get_paginator('describe_volumes')
# if the volumes are more we get them by page by page so we use
# for loop for each page
for each_page in paginator.paginate(Filters=[for_backup]):
    for each_vol in each_page['Volumes']:
        list_of_vol_ids.append(each_vol['VolumeId'])
print("The volumes id's are :",list_of_vol_ids)
snapids=[]
for each_vol_ids in list_of_vol_ids:
        print("Taking the snap of {}".format(each_vol_ids))
        res=ec2_cli.create_snapshot(
                Description="Taking snapshot",
                VolumeId=each_vol_ids,
                TagSpecifications=[
                        {
                                'ResourceType':'snapshot',
                                'Tags':[
                                        {
                                                'Key':'Delete-on',
                                                'Value':'90'
                                        }
                                ]
                        }
                ]
        )
        snapids.append(res.get('SnapshotId'))
        print("The collected snapid's are: ",snapids)
        waiter = ec2_cli.get_waiter('snapshot_completed')
        waiter.wait(SnapshotIds=snapids)
        print("Successfully snaped for the the volumes of {}".format(list_of_vol_ids))
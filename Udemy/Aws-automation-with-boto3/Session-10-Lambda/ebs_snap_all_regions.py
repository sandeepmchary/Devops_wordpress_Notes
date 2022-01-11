import boto3
session=boto3.session.Session(profile_name="root")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
all_regions=[]
for each_region in ec2_cli.describe_regions()['Regions']:
    all_regions.append(each_region.get('RegionName'))
for each_region in all_regions:
    print("Working on {}".format(each_region))
    ec2_cli=session.client(service_name="ec2",region_name=each_region)
    list_of_vol_ids=[]
    f_backup={'Name':'tag:prod','Values':['backup']}
    paginator=ec2_cli.get_paginator('describe_volumes')
    for each_page in paginator.paginate(Filters=[f_backup]):
        for each_vol in each_page['Volumes']:
            list_of_vol_ids.append(each_vol['VolumeId'])
    print("The Volume id's are: ",list_of_vol_ids)
    # Creating snapids
    if bool(list_of_vol_ids)==False:
        continue
    snap_ids=[]
    for each_vol_id in list_of_vol_ids:
        print("Taking Snap of {}".format(each_vol_id))
        res=ec2_cli.create_snapshot(
            Description='Taking snapshot',
            VolumeId=each_vol_id,
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
        snap_ids.append(res.get('SnapshotId'))
        print("The collected snapid's are: ",snap_ids)
        waiter = ec2_cli.get_waiter('snapshot_completed')
        waiter.wait(SnapshotIds=snap_ids)
        print("Successfully snaped for the the volumes of {}".format(list_of_vol_ids))

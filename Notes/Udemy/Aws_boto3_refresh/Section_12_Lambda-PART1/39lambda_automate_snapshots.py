import json
import boto3

def lambda_handler(event, context):
    ec2_cli = boto3.client('ec2')
    list_of_volid=[]
    snapids=[]
    paginator=ec2_cli.get_paginator('describe_volumes')
    for each_page in paginator.paginate(Filters=[{'Name':'tag:Prod','Values':['Devops']}]):
        for each_vol in each_page['Volumes']:
            list_of_volid.append(each_vol['VolumeId'])
    print("The list of Volume id's are {}",list_of_volid)
    for each_volid in list_of_volid:
        print("Taking snap of {}".format(each_volid))
        resp=ec2_cli.create_snapshot(
               Description='this is for creating snapshot',
               VolumeId=each_volid,
               TagSpecifications=[
                   {
                       'ResourceType':'snapshot',
                       'Tags':[
                           {
                               'Key':'Snap_shot',
                               'Value':'90'
                                   }]
                   }])
        snapids.append(resp['SnapshotId'])
        waiter=ec2_cli.get_waiter('snapshot_completed')
        waiter.wait(SnapshotIds=snapids)
        print("The volume id {} and there snap shots are {}".format(list_of_volid,snapids))
    
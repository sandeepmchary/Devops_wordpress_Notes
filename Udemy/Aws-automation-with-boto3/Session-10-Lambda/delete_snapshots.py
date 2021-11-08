import boto3
from datetime import datetime,timedelta,timezone
session=boto3.session.Session(profile_name="root")
ec2_re=session.resource("ec2")
f_name={'Name':'tag:Delete-on','Values':['90']}
snapshots=ec2_re.snapshots.filter(Filters=[f_name],OwnerIds=['self'])
for each_snap in snapshots:
    print(each_snap)
    # the above is for listing the snapshots in my owner id and 
    # the below is for deleting the snapshots
    each_snap.delete()
    print("Snapshot with ID = {} is deleted".format(each_snap.snapshot_id))
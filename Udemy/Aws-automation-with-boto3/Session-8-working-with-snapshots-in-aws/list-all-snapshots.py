import boto3
session=boto3.session.Session(profile_name="root")
ec2_res=session.resource(service_name="ec2",region_name="us-east-2")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
sts_cli=session.client("sts")
ownaccounid=sts_cli.get_caller_identity().get("Account")

print("Below is coming from Resources")
for each_snap in ec2_res.snapshots.filter(OwnerIds=[ownaccounid]):
	print (each_snap)

print ("Below is coming from client")
for each_snap in ec2_cli.describe_snapshots(OwnerIds=[ownaccounid])['Snapshots']:
	print (each_snap['SnapshotId'])


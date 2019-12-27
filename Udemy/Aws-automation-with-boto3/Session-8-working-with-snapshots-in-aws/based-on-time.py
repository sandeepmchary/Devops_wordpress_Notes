import boto3
import datetime
session=boto3.session.Session(profile_name="root")
ec2_res=session.resource(service_name="ec2",region_name="us-east-2")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
# session client for get the info of our account used for OwnerId 
sts_cli=session.client("sts")
ownaccounid=sts_cli.get_caller_identity().get("Account")
today=datetime.datetime.now()
start_time=str(datetime.datetime(today.year,today.month,today.day,13,13,46))
print (start_time)
print("Below is coming from Resources")
for each_snap in ec2_res.snapshots.filter(OwnerIds=[ownaccounid]):
	if each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S")==start_time:
		print(each_snap.id,each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))


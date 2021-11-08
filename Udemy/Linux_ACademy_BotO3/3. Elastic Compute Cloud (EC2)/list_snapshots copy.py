import boto3
import pprint
session=boto3.Session(profile_name="root",region_name="us-east-2")
client=session.client(service_name='ec2')
all_regions=client.describe_regions()
my_own_id=boto3.client('sts').get_caller_identity().get('Account')
#pprint.pprint(all_regions['Regions'])
# storing all the regions into a list
list_of_Regions=[]
for each_reg in all_regions['Regions']:
	#print(each_reg['RegionName'])
	list_of_Regions.append(each_reg['RegionName'])
	#print("List all the regions")
#pprint.pprint(list_of_Regions)

for each_reg in list_of_Regions:
	session=boto3.Session(profile_name="root",region_name=each_reg)
	resource=session.resource(service_name="ec2")
	#print("List of EC2 Instances from the region: ",each_reg)
	for each_snap in resource.snapshots.filter(OwnerIds=[my_own_id]):
		print(each_snap.description,each_snap.encrypted,each_snap.owner_id,each_snap.progress,each_snap.snapshot_id,each_snap.start_time,each_snap.state,each_snap.volume_id,each_snap.volume_size)
		
		
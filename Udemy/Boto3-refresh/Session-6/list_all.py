import boto3
import pprint
session=boto3.Session(profile_name="root")
ec2_re=session.resource(service_name='ec2',region_name='us-east-2')
client=session.client(service_name='ec2')
all_regions=client.describe_regions()
del_vol={'Name':'status','Values':['available']}
#print(reg)
list_of_regions=[]
for each_reg in all_regions['Regions']:
    #print(each_item['RegionName'])
    list_of_regions.append(each_reg['RegionName'])
pprint.pprint(list_of_regions)
for each_reg in list_of_regions:
	session=boto3.Session(profile_name="root",region_name=each_reg)
	resource=session.resource(service_name="ec2")
	print("List of EC2 Instances from the region: ",each_reg)
	for each_vol in resource.volumes.filter(Filters=[del_vol]):
		print(each_vol.id,each_vol.state,each_vol.tags)
       
    

    
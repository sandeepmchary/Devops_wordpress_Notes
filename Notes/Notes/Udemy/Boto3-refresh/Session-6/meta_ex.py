import boto3
import pprint
ec2=boto3.resource(service_name="ec2")
reg=ec2.meta.client.describe_regions()
#print(reg)
list_of_regions=[]
for each_item in reg['Regions']:
    #print(each_item['RegionName'])
    list_of_regions.append(each_item['RegionName'])
pprint.pprint(list_of_regions)    
    
    #for reg in ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}]):
                                #print(reg)
                                #print("----")
    
    

    
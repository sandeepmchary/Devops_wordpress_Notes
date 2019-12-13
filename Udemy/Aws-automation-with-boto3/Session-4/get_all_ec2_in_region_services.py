'''
import boto3
session=boto3.session.Session(profile_name="root")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
#print (ec2_cli.describe_regions()['Regions']) -- same output for the below
for each_region_info in  ec2_cli.describe_regions().get('Regions'):
    print ((each_region_info).get('RegionName'))
'''
import boto3
session=boto3.session.Session(profile_name="root")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
#print (ec2_cli.describe_regions()['Regions']) -- same output for the below
regions=[]
for each_region_info in  ec2_cli.describe_regions().get('Regions'):
    regions.append ((each_region_info).get('RegionName'))
print ("All regions for ec2 services are\n ",regions)
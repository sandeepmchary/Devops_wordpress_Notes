import boto3
ec2_cli=boto3.client('ec2')
all_region=ec2_cli.describe_regions()['Regions']
'''list_of_regions=[]
for each in all_region:
    #print(each['RegionName'])
    list_of_regions.append(each['RegionName'])'''
regions=[region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
print("------------------LIST OF EC2 INSTANCES------------------")
for each_reg in regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_reg)
    print("List of Ec2 instances in the region:",each_reg)
    for each_in in ec2_re.instances.all():
        print(each_in.id,each_in.state['Name'])

print("------------------LIST OF EBS VOLUMES------------------")
for each_reg in regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_reg)
    print("List of EBS volumes in the region:",each_reg)
    for each_vol in ec2_re.volumes.all():
        print(each_vol.id,each_vol.state)
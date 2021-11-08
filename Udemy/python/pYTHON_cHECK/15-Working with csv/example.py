import boto3
session=boto3.Session(profile_name="root",region_name="us-east-2")
ec2_client=session.client(service_name='ec2')
regions = [region['RegionName']
            for region in ec2_client.describe_regions()['Regions']]
for each_reg in regions:
    session=boto3.Session(profile_name="root",region_name=each_reg)
    ec2 = session.resource('ec2')
    print("List of EC2 Instances from the region: ",each_reg)
    for each_in in ec2.instances.all():
        print(each_in.id,each_in.state['Name'])


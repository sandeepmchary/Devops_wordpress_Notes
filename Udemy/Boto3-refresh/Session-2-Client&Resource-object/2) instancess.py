import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="ap-south-1")
for each_in in ec2_con_re.instances.all():
    print(each_in.id)
    

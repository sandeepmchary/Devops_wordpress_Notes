import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
#print (dir(ec2_con_re))
'''
for each_in in ec2_con_re.instances.all():
    print (each_in.id, each_in.state)
'''

running_filters={"Name":"instance-state-name","Values":["running"]}
stopped_filters={"Name":"instance-state-name","Values":["stopped"]}
zone_filters={"Name":"availability-zone","Values":["us-east-2b"]}
insta_type={"Name": "instance-type","Values": ["t2.micro"]}
'''
for each_in in ec2_con_re.instances.filter(Filters=[running_filters]):
    print("This is coming from running_filters: ")
    print (each_in.id, each_in.state)
for each_in in ec2_con_re.instances.filter(Filters=[stopped_filters]):
    print("This is coming from stopped_filters\n: ")
    print (each_in.id, each_in.state)
'''
'''
for each_in in ec2_con_re.instances.filter(Filters=[zone_filters,stopped_filters]):
    print (each_in.id,each_in.state)
for each_in in ec2_con_re.instances.filter(Filters=[zone_filters,running_filters]):
    print (each_in.id, each_in.state)
    
for each_in in ec2_con_re.instances.filter(Filters=[insta_type,running_filters]):
    print (each_in.id, each_in.state)
'''
# FILTERS USING TAGS
ftags={"Name": "tag:Name","Values": ["udemy-boto3"]}
env_filters={"Name":"tag:ENV","Values": ["boto3"]}
'''
for each_in in ec2_con_re.instances.filter(Filters=[ftags]):
    print (each_in.id, each_in.state)
'''
for each_in in ec2_con_re.instances.filter(Filters=[env_filters]):
    print (each_in.id, each_in.state)

    


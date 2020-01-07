import boto3
session=boto3.session.Session(profile_name="root")
#ec2_re=boto3.resource(service_name="ec2",region_name="us-east-2")
ec2_re=session.resource(service_name="ec2",region_name="us-east-2")
test_env={"Name":"tag:Env","Values":["Testing"]}
for each_in in ec2_re.instances.filter(Filters=[test_env]):
	each_in
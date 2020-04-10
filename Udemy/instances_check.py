import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=session.client(service_name="ec2",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
    print("The Instance ID is: {}\nThe State of the Instance is: {}".format(each_in.id,each_in.state))
print("instances info with client")
for each in ec2_con_cli.describe_instances()['Reservations']:
	for each_in in each['Instances']:
		print(each_in['InstanceId'],each_in['State']['Name'])

import boto3
from pprint import pprint
aws_mgm_cli=boto3.session.Session(profile_name="root")
ec2_con_cli=aws_mgm_cli.client(service_name="ec2",region_name="us-east-2")
'''
# WORKING WITH EC2
response=ec2_con_cli.describe_instances()['Reservations']
#print(response)
#pprint(response)
for each_item in response:
	#print(each_item['Instances'])
	# the above one has got again into the list
	for each_instances_list in each_item['Instances']:
		#pprint(each_instances_list)
               #pprint(each_instances_list['InstanceId'])
              print("The Image id is {}\nThe InstanceId is {}\nThe InstanceType is {}\nThe PrivateIpAddress is {}\nThe Instance launch time is {}".format(each_instances_list['ImageId'],each_instances_list['InstanceId'],each_instances_list['InstanceType'],each_instances_list['PrivateIpAddress'],each_instances_list['LaunchTime'].strftime("%Y-%m-%d")))
              print('------------------------------------------')
'''
response=ec2_con_cli.describe_volumes()['Volumes']
#pprint(response)

for each_item in response:
	print('=================================================')
	print("The Volume ID is: {}\nThe availbality zone: {}\nThe VolumeType: {}\nThe State of Volume: {}".format(each_item['VolumeId'],each_item['AvailabilityZone'],each_item['VolumeType'],each_item['State']))

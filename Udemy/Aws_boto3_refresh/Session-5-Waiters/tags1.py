import boto3
from pprint import pprint

ec2_re = boto3.resource('ec2',)
ec2_cli = boto3.client('ec2',)
response=ec2_cli.describe_tags()
values_list=[]
for each_in in ec2_cli.describe_instances()['Reservations']:
	for each_res in each_in['Instances']:
		for each_tag in response['Tags']:
			values_list.append(each_tag)
			#print("id:{0}\nState:{1}\nPublic_Dns_name:{2}\ntag:{3}".format(each_res['InstanceId'],each_res['State']['Name'],each_res['PublicDnsName'],each_tag['Value']))
			print(values_list[0]['Value'])			
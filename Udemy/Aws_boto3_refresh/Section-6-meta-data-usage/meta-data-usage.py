# TO ENTER INTO CLIENT OBJECT FROM RESOURCE OBJECT
# IN CLIENT OBJECT WE CAB DO  EACH AND EVERY OPERATION
# ==========================
# LIST AVAILABLE REGIONS FOR EC2 SERVICES
import boto3
ec2_re = boto3.resource('ec2')
#print(dir(ec2_re))
#print(dir(ec2_re.meta))
#print(dir(ec2_re.meta.client))
for each_item in ec2_re.meta.client.describe_regions()['Regions']:
	print(each_item.get('RegionName'))
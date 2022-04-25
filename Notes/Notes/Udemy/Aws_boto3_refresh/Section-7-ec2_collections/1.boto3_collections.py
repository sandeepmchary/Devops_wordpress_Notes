# used to collect group of resource information 
import boto3
ec2_re = boto3.resource('ec2')
# IN COLLECTIONS WE CAN WORK WITH EC2,INSTANCES,INSTANCES_TYPES,VOLUMES,AMI,SNAPSHOTS,SECURITY_GROUPS ARE GROUP
# OF RESOURCES COLLECTIVELY TO COLLECT THIS INFORMATION WE HAVE TO USE COLLECTIONS CONCEPT
# IN SOURCE RESOURCE WE HAVE THREE SETS
# 1) RESOURCE AVAILABLE ACTIONS
# 2) RESOURCE AVAILABLE SUB-RESOURCE
# 3) COLLECTIONS
#print(dir(ec2_re.instances)) # LIST OF OPERATIONS ON EC2_RE.INSTANCES
# EC2_RE.INSTANCES IS COLLECTION OBJECT
# THE OUTPUT FOR PRINT IS THE SUB-METHODS 
# HERE WE GOING TO CONCENTRATE ON 
# ALL,FILTER,LIMIT,FILTER
##for each in ec2_re.instances.all():
##for each in ec2_re.instances.limit(1):
f1={"Name": "instance-state-name","Values":['stopped']}
f2={'Name':'instance-type','Values':['t2.micro']}
for each in ec2_re.instances.filter(Filters=[f2]):
	print(each)














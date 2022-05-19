import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
# Start only non prod servers
# i changed the instance names to prod and non prod
np_ids=[]
# this is for the filter
f1={'Name':'tag:Name','Values':['non-prod']}
for each in ec2_re.instances.filter(Filters=[f1]):
	np_ids.append(each.id)
print(np_ids)
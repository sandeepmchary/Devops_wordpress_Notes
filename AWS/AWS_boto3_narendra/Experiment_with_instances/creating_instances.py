import boto3
ec2_cli=boto3.client('ec2')
ec2_re=boto3.resource('ec2')
resp=ec2_cli.run_instances(
							ImageId='ami-01e36b7901e884a10',
							InstanceType='t2.micro',
							MaxCount=1,
							MinCount=1)
ins_id=[]
for instance in resp['Instances']:
	print(instance['InstanceId'])
	ins_id.append(instance['InstanceId'])
print(ins_id)
f1={"Name":"instance-id","Values":ins_id}
for each in ec2_re.instances.filter(Filters=[f1]):
    print("Instance id:{}\nState:{}\npublic_ip:{}\ntags:{}".format(each.instance_id,each.state['Name'],each.public_ip_address,each.tags))
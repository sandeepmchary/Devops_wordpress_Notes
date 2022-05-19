import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
all_ins_id=[]
for each in ec2_re.instances.all():
	print(each.id,each.state['Name'])
	all_ins_id.append(each.id)
#print(all_ins_id)
print("Stopping all instances...")
ec2_re.instances.stop()
waiter=ec2_cli.get_waiter('instance_stopped')
waiter.wait(InstanceIds=all_ins_id)
print("All instances are stopped")

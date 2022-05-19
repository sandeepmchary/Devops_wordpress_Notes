'''
- before starting all the instance first we need to collect the instance id
- create a list for all instance ids
- then with append option we append the all the instance id that derived from for loop 
- 

'''
import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
all_ins_id=[]
for each in ec2_re.instances.all():
	all_ins_id.append(each.id)

print("Starting all instances...")
ec2_re.instances.start()
waiter=ec2_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=all_ins_id)
print("All instances are up and running")

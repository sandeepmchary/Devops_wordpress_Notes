import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
all_ins_id=[]
for each in ec2_re.instances.all():
    all_ins_id.append(each.id)
waiter=ec2_cli.get_waiter('instance_running')
ec2_re.instances.start()
waiter.wait(InstanceIds=all_ins_id)
print("Your instance are up and running")
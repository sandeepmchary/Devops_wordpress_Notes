import boto3
ec2_re=boto3.resource('ec2')
response=ec2_re.instances.all()
#print(response)
for each in response:
    print(each.tags)
    print(each.instance_id)
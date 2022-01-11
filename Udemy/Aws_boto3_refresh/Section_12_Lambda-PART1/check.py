import boto3
ec2_re=boto3.resource('ec2',region_name='us-east-1')
for each_in in ec2_re.instances.all():
     
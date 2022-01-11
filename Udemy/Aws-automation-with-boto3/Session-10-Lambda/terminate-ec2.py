import boto3
session=boto3.session.Session(profile_name="root")
ec2_re=session.resource('ec2')
for each_in in ec2_re.instances.all():
    print("id: {}".format(instance.id))
import boto3

ec2 = boto3.resource('ec2')
volume_iterator = ec2.volumes.all()
for v in volume_iterator:
    for a in v.attachments:
        print ("{0} {1} {2}".format(v.id, v.state, a['InstanceId']))
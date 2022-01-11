import boto3
ec2_re=boto3.resource('ec2')
req_ins=ec2_re.Instance("i-09cadc9593f35e6b5")
print("Instance stopping")
req_ins.stop()
req_ins.wait_until_stopped()
print("Instance stopped")
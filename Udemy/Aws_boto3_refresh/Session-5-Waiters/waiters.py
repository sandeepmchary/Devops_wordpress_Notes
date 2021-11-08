import boto3
import time
ec2_re = boto3.resource('ec2')
ec2_cli = boto3.client('ec2')
'''
ec2_re.Instance("i-0532ec7cf1d7603ac").stop()
ec2_re.Instance("i-0532ec7cf1d7603ac").wait_until_stopped()

ec2_re.Instance("i-0532ec7cf1d7603ac").start()
ec2_re.Instance("i-0532ec7cf1d7603ac").wait_until_running()
print("The ec2 instance is up and running")
'''
# RESOURCE WAITER WAITS FOR 200 SECS
# 40 CHECKS FOR EVERY 5 SECS
# BETTER TO TAKE WAITERS FROM CLIENT OBJECT
ec2_cli.stop_instances(InstanceIds=['i-0532ec7cf1d7603ac'])
waiter=ec2_cli.get_waiter('instance_stopped')
waiter.wait(InstanceIds=['i-0532ec7cf1d7603ac'])
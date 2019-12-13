#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
my_ins=ec2_con_re.Instance(id="i-0cc45f8ba2faaa1ca")
my_ins.start()
my_ins.wait_until_running()
# the default time is 200 the wait_until_running will check for every 5 seconds for the 40 internvals

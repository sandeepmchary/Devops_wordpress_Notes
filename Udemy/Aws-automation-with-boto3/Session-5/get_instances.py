#!/usr/bin/python
import boto3
#session=boto3.session.Session(profile_name="root")
#ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
ec2_con_re=boto3.resource(service_name="ec2",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
    print each_in
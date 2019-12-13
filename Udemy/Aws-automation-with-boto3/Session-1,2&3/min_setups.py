#!/bin/usr/python
import boto3
# Session
session=boto3.session.Session(profile_name="root")
# ec2 console
session_con_res=session.resource(service_name="ec2",region_name="us-east-2")
sesion_con_cli=session.resource(service_name="ec2",region_name="us-east-2")
# S3 console
s3_con_res=session.resource(service_name="s3",region_name="us-east-2")
for each_in in ec2_con_re.instances.all():
	print(each_in.id)


for each_in in ec2_con_re.instances.all():
    print(each_in.id,each_in.state)
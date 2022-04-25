#!/usr/bin/python
# for this to work in windows just start from import boto3
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
in_id=raw_input("Enter your instance id : ")
# input is for 2.7 version 
# raw_input is for 3.7 version
my_ins_ob=ec2_con_re.Instance(id=in_id)
#print (dir(my_ins_ob))
print (my_ins_ob.tags)
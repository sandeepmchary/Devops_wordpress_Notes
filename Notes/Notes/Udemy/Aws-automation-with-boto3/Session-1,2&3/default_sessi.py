#!/bin/usr/python
import boto3
ec2_con_re=boto3.resource('ec2','us-east-2')
for each_in in ec2_con_re.instances.all():
	print(each_in.id)
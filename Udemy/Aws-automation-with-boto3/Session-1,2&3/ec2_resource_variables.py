#!/bin/usr/python
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_cli=session.client(service_name="ec2",region_name="us-east-2")
print dir(ec2_con_cli)


#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
ec2_console_resource=session.resource(service_name="ec2",region_name="us-east-2")
print dir(ec2_console_resource)

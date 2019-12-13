#!/usr/bin/python
import boto3
import pprint
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=session.client(service_name="ec2",region_name="us-east-2")
#print (ec2_con_re.instances.all())
#for each_in in ec2_con_re.instances.all():
print "Below is using resource object"
for each_in in ec2_con_re.instances.all():
    #print(each_in)
    print (each_in.instance_id,each_in.instance_type,each_in.state)

#print ec2_con_cli.describe_instances().keys()
#pprint.pprint (ec2_con_cli.describe_instances())
# pprint.pprint(ec2_con_cli.describe_instances()['Reservations'])
print "Below is using client object"
for each_info in ec2_con_cli.describe_instances()['Reservations']:
    for each_inst in each_info['Instances']:
        print each_inst['InstanceId'], each_inst['InstanceType'], each_inst['State']
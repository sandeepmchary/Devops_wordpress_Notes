from collections import defaultdict
from pprint import pprint
import boto3
ec2_re=boto3.resource('ec2')
running_instances=ec2_re.instances.filter(Filters=[{'Name': 'instance-state-name','Values':['stopped']}])
ec2_info=defaultdict()
for instances in running_instances:
    for tags in instances.tags:
        print(tags)
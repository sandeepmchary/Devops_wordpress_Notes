import boto3
from pprint import pprint
ec2_cli = boto3.client('ec2')
resp = ec2_cli.run_instances(
       ImageId = "ami-0affd4508a5d2481b",
       InstanceType="t2.micro",
       MinCount=1,
       MaxCount=1,
       TagSpecifications=[
           {
               'ResourceType':'instance',
               'Tags':[
                   {
                       'Key':'Name',
                       'Value':'With_python1'
                   }
               ]
           }
       ]
)
instance_id = []
for each in resp['Instances']:
    instance_id.append(each['InstanceId'])

waiter=ec2_cli.get_waiter('instance_started')
for each_in in instance_id:
    print(each_in)
    waiter.wait(InstanceIds=[each_in])
for each in resp['Instances']:
    pprint(each)
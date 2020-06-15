import boto3
ec2=boto3.resource('ec2',region_name='us-east-2')

for each_vol in ec2.volumes.filter(
                                Filters=[{'Name': 'status', 'Values': ['available']}]
                                ):
                                print(each_vol)


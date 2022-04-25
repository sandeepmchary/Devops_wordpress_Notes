import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
np_ser_id=[]
'''
for each in ec2_re.instances.filter(
                                    Filters=[
                                        {
                                            "Name":"tag:Name",
                                            "Values":['Prod']
                                        }
                                    ]
                                    ):
    np_ser_id.append(each.id)
print(np_ser_id)
'''
# There is no collections concept with client
# but with filters we can collect the info
for each in ec2_cli.describe_instances(Filters=[
                                                {
                                                  "Name":"tag:Name",
                                                  "Values":['Prod']  
                                                    }])['Reservations']:
    for each_ins in each['Instances']:
        np_ser_id.append(each_ins['InstanceId'])
ec2_cli.start_instances(InstanceIds=np_ser_id)
waiter=ec2_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=np_ser_id)
for each in ec2_re.instances.all():
    print("Instance id:{}\nState:{}\npublic_ip:{}\ntags:{}".format(each.instance_id,each.state['Name'],each.public_ip_address,each.tags))
print("Your instances are up and running")
        
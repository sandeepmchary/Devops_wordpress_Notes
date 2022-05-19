import boto3
ec2_cli=boto3.client('ec2')
response=ec2_cli.describe_instances()['Reservations']
for each in response:
    for each_ins in each['Instances']:
        print("====================================")
        print("The Instance Id is:{}\nThe Instance State is:{}".format(each_ins['InstanceId'],each_ins['State']['Name']))
ins_id=input("Enter the Instance id :  ")
ec2_cli.start_instances(InstanceIds=[ins_id])
waiter=ec2_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=[ins_id])



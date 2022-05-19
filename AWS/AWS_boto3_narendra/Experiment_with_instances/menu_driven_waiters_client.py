import boto3
ec2_cli=boto3.client('ec2',region_name='us-east-1')
response=ec2_cli.describe_instances()['Reservations']
for each in response:
    for each_ins in each['Instances']:
        print("====================================")
         print("The instance id is: {}\nThe Instance State is : {}\nThe Public Ip: {}\nThe Instance tag value: {}".format(each_in['InstanceId'],each_in['State']['Name']))
while True:
    print("This script performs the following actions")
    print("""
          1. Start
          2. Stop
          3. Terminate
          4. Exit
          """)
    opt=int(input("Enter your option:  "))
    if opt==1:
        ins_id=input("Enter the instance id: ")
        ec2_cli.start_instances(
                        InstanceIds=[ins_id]
                 )
        waiter=ec2_cli.get_waiter('instance_running')
        waiter.wait(InstanceIds=[ins_id])
        print("Started the instance, The instance id is:{}".format(ins_id))
    if opt==2:
        ins_id=input("Enter the instance id: ")
        ec2_cli.stop_instances(
                        InstanceIds=[ins_id]
                 )
        waiter=ec2_cli.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[ins_id])
        print("Stopped the instance, The instance id is:{}".format(ins_id))        
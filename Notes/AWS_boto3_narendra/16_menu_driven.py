import boto3
from pprint import pprint
import sys
ec2_cli=boto3.client('ec2',region_name='us-east-1')
ec2_re=boto3.resource('ec2',region_name='us-east-1')
response=ec2_re.instances.all()
for each in response:
    print("====================================")
    print(each.instance_id,each.public_ip_address,each.tags)
while True:
    print("The Script performs the following Scripts")
    print("""
            1. Start
            2. Stop
            3. Terminate
            4. Exit
            """)
    opt=int(input("Enter Your choice from 1-4 only"))
    if opt==1:
        ins_id=input("Enter the Ec2 instances id:")
        my_req_action=ec2_re.Instance(ins_id)
        my_req_action.start()
        print("Starting the Instance...")
        # state of the instance
        resp=ec2_cli.describe_instances(
            InstanceIds=[ins_id]
        )
        for each in resp['Reservations']:
            for each_ins in each['Instances']:
                print("The instance id is : {}\nThe State is: {}".format(each_ins['InstanceId'],each_ins['State']['Name']))
        
    if opt==2:
        ins_id=input("Enter the Ec2 Instances id:")
        my_req_action=ec2_re.Instance(ins_id)
        my_req_action.stop()
        print("Stopping the Instance...")         
        # state of the instance
        resp=ec2_cli.describe_instances(
            InstanceIds=[ins_id]
        )
        for each in resp['Reservations']:
            for each_ins in each['Instances']:
                print("The instance id is : {}\nThe State is: {}".format(each_ins['InstanceId'],each_ins['State']['Name']))
    if opt==3:
        ins_id=input("Enter the Ec2 Instances id:")
        my_req_action=ec2_re.Instance(ins_id)
        my_req_action.terminate()
        print("Stopping the Instance...")         
        # state of the instance
        resp=ec2_cli.describe_instances(
            InstanceIds=[ins_id]
        )
        for each in resp['Reservations']:
            for each_ins in each['Instances']:
                print("The instance id is : {}\nThe State is: {}".format(each_ins['InstanceId'],each_ins['State']['Name']))
            
    if opt==4:
        print("Thankyou for using the script")
        sys.exit()
    else:
        print("Your option is invalid,Please choose between 1-4 only")
for each in response:
    print("====================================")
    print(each.instance_id,each.public_ip_address,each.tags)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
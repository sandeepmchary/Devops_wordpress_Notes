import boto3
import sys
from pprint import pprint
ec2_cli=boto3.client('ec2')
response=ec2_cli.describe_instances()['Reservations']
for each in response:
    for each_ins in each['Instances']:
        print("====================")
        print("The Instance id:{}\nThe Instance stae:{}".format(each_ins['InstanceId'],each_ins['State']['Name']))
        print("********************")
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
        ins_id=input("Enter your instance id:  ")
        resp=ec2_cli.start_instances(
            InstanceIds=[ins_id]
        )
        for each in resp:
            print(each)
        print(resp)
    
    if opt==2:
        ins_id=input("Enter your instance id:  ")
        resp=ec2_cli.stop_instances(
            InstanceIds=[ins_id]
        ) 
        print(resp)
    if opt==3:
        ins_id=input("Enter your instance id: ")
        resp=ec2_cli.terminate_instances(
            InstanceIds=[ins_id]
        )
    if opt==4:
        print("Thankyou for using the script")
        sys.exit()
    else:
        print("Choose between 1-4 only Bye..Bye")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
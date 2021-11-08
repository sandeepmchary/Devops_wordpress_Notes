import boto3
import sys
aws_con_mgm=boto3.session.Session(profile_name="root")
ec2_con_cli=aws_con_mgm.client(service_name="ec2",region_name="us-east-2")
while True:
    print("The following script has these actions on ec2 Instancres")
    print("""
        1. Start
        2.Stop
        3.Terminate
        4.Exit
    """)
    opt=int(input("Enter your option:"))
    if opt==1:
        instance_id=input("Enter your Instance id: ")
        print("starting the instance ...")
        ec2_con_cli.start_instances(InstanceIds=[instance_id])
    elif opt==2:
        instance_id=input("Enter your Instance id: ")
        print("stopping the instance ...")
        ec2_con_cli.stop_instances(InstanceIds=[instance_id])
    elif opt==3:
        instance_id=input("Enter your Instance id: ")
        print("Terminating the instances ...")
        ec2_con_cli.terminate_instances(InstanceIds=[instance_id])
    elif opt ==4:
        print("Thank you for using this script")
        sys.exit()
    else:
        print("Enter your valid option~")    

            
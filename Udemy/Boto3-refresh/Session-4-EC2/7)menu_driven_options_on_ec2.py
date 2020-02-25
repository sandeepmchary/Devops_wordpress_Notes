import boto3
import sys
aws_mgt_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mgt_con.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=aws_mgt_con.client(service_name="ec2",region_name="us-east-2")

while True:
    print("This Script performs the following actions")
    print("""
        1. Start
        2. Stop
        3. Terminate
        4. Exit""")
    opt=int(input("Enter your choice: "))
    if opt==1:
        instance_id=input("Enter your Ec2 Instance Id:")
        # WE CAN WORK THIS WITH VOLUME ALSO
        # my_req_instance_obj=ec2_con_re.Volume(Volume_id)
        # KEYPAIR
        # IMAGEiD
        my_req_instance_obj=ec2_con_re.Instance(instance_id)
        #print(dir(my_req_instance_obj))
        print(my_req_instance_obj)
        print("Starting Ec2 instances ....")
        my_req_instance_obj.start()
    elif opt==2:
        instance_id=input("Enter your Ec2 Instance Id:")
        my_req_instance_obj=ec2_con_re.Instance(instance_id)
        print("Stopping Ec2 Instances ....")
        my_req_instance_obj.stop()
    elif opt==3:
        instance_id=input("Enter your Ec2 Instance Id:")
        my_req_instance_obj=ec2_con_re.Instance(instance_id)
        print("Terminating Ec2 Instance ....")
        my_req_instance_obj.terminate()
    elif opt==4:
        print("Existing from the script")
        sys.exit()
    else:
        print("Choose in between the options")    
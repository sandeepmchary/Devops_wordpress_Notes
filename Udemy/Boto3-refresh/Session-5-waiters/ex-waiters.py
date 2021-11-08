import boto3
import time
aws_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-2")
my_ins_obj=ec2_con_re.Instance("i-08f0f706b4bd5acf6")
#print("starting given instance....")
my_ins_obj.start()
#print(my_ins_obj.state)
'''
while True:
    my_ins_obj=ec2_con_re.Instance("i-08f0f706b4bd5acf6")
    print("The current status of the instance is ...:",my_ins_obj.state['Name'])
    if my_ins_obj.state['Name']=="running":
        break
    print("waiting to get running state...")
    time.sleep(5)
'''    
#print(dir(my_ins_obj))
my_ins_obj.wait_until_running()
#print(my_ins_obj.ami_launch_index)
#print(my_ins_obj.state['Name'])
print("Now the instance is up and runnig ....")



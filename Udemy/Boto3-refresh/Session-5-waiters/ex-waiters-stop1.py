import boto3
aws_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-2")
my_inst_obj=ec2_con_re.Instance("i-08f0f706b4bd5acf6")
my_inst_obj.stop()
# Resource waiter checks only 200 seconds (40 checks after every 5 sec...)
my_inst_obj.wait_until_stopped()
print("The Instance is stopped now")
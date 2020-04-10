import boto3
import time
aws_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-2")
my_inst_obj=ec2_con_re.Instance("i-08f0f706b4bd5acf6")
print("stoping the instances")
my_inst_obj.stop()
while True:
	my_inst_obj=ec2_con_re.Instance("i-08f0f706b4bd5acf6")
	print("The instance state is ..",my_inst_obj.state['Name'])
	if my_inst_obj.state['Name']=="stopped":
		break
	time.sleep(5)
print("the state of the instance is ",my_inst_obj.state['Name'])	
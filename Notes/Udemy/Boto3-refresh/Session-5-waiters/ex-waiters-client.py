import boto3
aws_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-2")
ec2_con_cli.start_instances(InstanceIds=['i-08f0f706b4bd5acf6'])
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-08f0f706b4bd5acf6'])
print("Now the ec2 instance is up and running ....")
# IN REAL TIME WE USE CLIENT WAITERS
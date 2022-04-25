import boto3
from pprint import pprint
session=boto3.session.Session(profile_name="root")
ec2_re=session.resource(service_name="ec2",region_name="us-east-2")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
#ec2_re.instances.stop()
db_filter={"Name":"tag:ENV","Values":["db"]}
Instan_ids=[]
for each_in in ec2_re.instances.filter(Filters=[db_filter]):
    Instan_ids.append(each_in.id)
print ("All required ec2 Instances: ",Instan_ids)
#waiter = ec2_cli.get_waiter('instance_stopped')
waiter = ec2_cli.get_waiter('instance_running')
#ec2_re.instances.start(InstanceIds=Instan_ids)
#ec2_re.instances.stop(InstanceIds=Instan_ids)
#ec2_re.instances.reboot(InstanceIds=Instan_ids)
#ec2_re.instances.terminate(InstanceIds=Instan_ids)
ec2_cli.stop_instances(InstanceIds=Instan_ids)
#ec2_cli.start_instances(InstanceIds=Instan_ids)
waiter.wait(InstanceIds=Instan_ids)

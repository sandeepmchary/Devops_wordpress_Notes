'''
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
# list all the ebs volumes
for each_vol in ec2_con_re.volumes.all():
    print(each_vol.id, each_vol.state)
'''
'''
# above are boto3 defined filters
# this one below is for our own filters
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
for each_vol in ec2_con_re.volumes.all():
    if each_vol.state=="in-use" and each_vol.tags==dellen:
        print (each_vol.id,each_vol.state,each_vol.tags)
'''
# USING THE WAITERS FROM THE CLIENT IS THE BEST WAY
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
ec2_cli=session.client(service_name="ec2",region_name="us-east-2")
# List all EBS Volumes
all_req_vol_ids=[]
unused={'Name':'tag:Name','Values':["dellen"]}
for each_vol in ec2_con_re.volumes.filter(Filters=[unused]):
    print (each_vol.id,each_vol.state)
    all_req_vol_ids.append(each_vol)

# Deleting the Volumes
for each_vol in all_req_vol_ids:
    volume_ob=ec2_con_re.Volume(each_vol)
    #print (dir(volume_ob))
    print ("Deleting the volumes of id",each_vol)
    volume_ob.delete()


waiter = ec2_cli.get_waiter('volume_deleted')
try:
    waiter.wait(VolumeIds=all_req_vol_ids)
    print ("Successfully deleted the volumes: ")
except Exception as e:
    print (e)

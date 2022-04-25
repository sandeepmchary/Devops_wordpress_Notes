import boto3
import csv
from pprint import pprint
ec2_re = boto3.resource('ec2')
ec2_cli = boto3.client('ec2')
sno=1
inst_id=[]
required_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\ins.csv"
fo=open(required_file,"w",newline="")
fo_w=csv.writer(fo)
fo_w.writerow(["SNO","Instance_ID","Instance_Type","Architecture","Launch_Time","Private_IP","Volume_Id"])

for each in ec2_re.instances.all():
    inst_id.append([each,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%M-%D"),each.private_ip_address])
print(inst_id)    
for ec2_vol in ec2_re.volumes.all():
    print(each.instance_type,each.architecture,each.launch_time.strftime("%Y-%M-%D"),each.private_ip_address,each,inst_id.each_vol.volume_id)
    fo_w.writerow([sno,inst_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%M-%D"),each.private_ip_address,each,inst_id.each_vol.volume_id])
    sno=sno+1
fo.close()    
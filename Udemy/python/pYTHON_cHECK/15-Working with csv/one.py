import boto3
import csv
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
sno=1
required_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\ins.csv"
fo=open(required_file,"w",newline="")
fo_w=csv.writer(fo)
fo_w.writerow(["SNO","Instance_ID","Instance_Type","Architecture","Launch_Time","Private_IP","Volume_Id"])
for each in ec2_cli.describe_instances():
    print(sno,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%M-%D"),each.private_ip_address)
    fo_w.writerow([sno,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%M-%D"),each.private_ip_address])
    

    sno+=1
fo.close()



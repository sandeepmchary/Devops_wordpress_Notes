import boto3
from pprint import pprint
import csv
from pprint import pprint
ec2_re = boto3.resource('ec2')
ec2_cli = boto3.client('ec2')
sno=1
req_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\ins_cli.csv"
fo=open(req_file,"w",newline="")
fo_w=csv.writer(fo)
fo_w.writerow(["SNO","Instance_ID","Instance_Type","Architecture","Launch_Time","Private_IP","Public_DNS","Volume_Id"])
for each_in in ec2_cli.describe_instances()['Reservations']:
    for each_ins in each_in['Instances']:
        for each_vol in each_ins['BlockDeviceMappings']:
            print(each_ins['InstanceId'],each_ins['InstanceType'],each_ins['Architecture'],each_ins['LaunchTime'].strftime("%Y-%M-%D"),each_ins['PrivateIpAddress'],each_ins['PublicDnsName'],each_vol['Ebs']['VolumeId'])
            fo_w.writerow([sno,each_ins['InstanceId'],each_ins['InstanceType'],each_ins['Architecture'],each_ins['LaunchTime'].strftime("%Y-%M-%D"),each_ins['PrivateIpAddress'],each_ins['PublicDnsName'],each_vol['Ebs']['VolumeId']])
            sno+=1
fo.close()            

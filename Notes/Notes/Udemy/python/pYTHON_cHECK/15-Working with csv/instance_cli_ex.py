import boto3
import csv
from pprint import pprint 
ec2 = boto3.client('ec2')
#sno=1
#req_file="D:\\DevopS_giT\\Udemy\\python\\15-Working with csv\\ins_cli_ex.csv"
#fo=open(req_file,"w",newline="")
#fo_w=csv.writer(fo)
#fo_w.writerow(["SNO","Instance_ID","Instance_Type","Architecture","Launch_Time","Private_IP","Volume_Id"])
inst_id=[]
for each_in in ec2.describe_instances()['Reservations']:
    for each_ins in each_in['Instances']:
        
        inst_id.append(each_in)
print(inst_id['InstanceId'])        
            #print(each_ins['InstanceId'],each_ins['InstanceType'],each_ins['Architecture'],each_ins['LaunchTime'].strftime("%Y-%M-%D"),each_ins['PrivateIpAddress'],each_ins['PublicDnsName'],each_vol['VolumeId'])
            #fo_w.writerow([sno,each_ins['InstanceId'],each_ins['InstanceType'],each_ins['Architecture'],each_ins['LaunchTime'].strftime("%Y-%M-%D"),each_ins['PrivateIpAddress'],each_ins['PublicDnsName'],each_vol['VolumeId']])
            #sno+=1
#fo.close()           
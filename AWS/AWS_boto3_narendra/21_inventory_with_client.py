import boto3
import csv
from pprint import pprint
ec2_cli=boto3.client('ec2')
cnt=1
csv_ob=open("inventory.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_no","Instance_ID","Instance_type","Architecture","launch_time","public_ip_address","private_ip","Volume_id"])
for each in ec2_cli.describe_instances()['Reservations']:
    for each_item in each['Instances']:
        for each_vol in each_item['BlockDeviceMappings']:
            print(each_item['InstanceId'],
                 each_item['InstanceType'],
                 each_item['Architecture'],
                 each_item['LaunchTime'],
                 each_item['PublicDnsName'],
                 each_item['PrivateIpAddress'],
                  each_vol['Ebs']['VolumeId'])
            csv_w.writerow([cnt,each_item['InstanceId'],each_item['InstanceType'],each_item['Architecture'],each_item['LaunchTime'],each_item['PublicDnsName'],each_item['PrivateIpAddress'],each_vol['Ebs']['VolumeId']])
            cnt+=1
csv_ob.close()            
        
            
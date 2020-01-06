import boto3
import csv
session=boto3.session.Session(profile_name="root")
ec2_re=session.resource("ec2")
ec2_cli=session.client("ec2")
header_csv=['S_NO','instance_id','instance_type','Architecture','Launch_time','private_ip_address','public_ip_address']
S_No=1
fo=open("ec2_inv.csv","wb")
csv_w=csv.writer(fo)
csv_w.writerow(header_csv)
for each_in in ec2_re.instances.all():
    in_ID=each_in.instance_id
    in_TYPE=each_in.instance_type
    in_Architecture=each_in.architecture
    in_launch_time=each_in.launch_time
    in_private_ip_address=each_in.private_ip_address
    in_public_ip_address=each_in.public_ip_address
    print(S_No,in_ID,in_TYPE,in_Architecture,in_launch_time,in_private_ip_address,in_public_ip_address)
    csv_w.writerow([S_No,in_ID,in_TYPE,in_Architecture,in_launch_time,in_private_ip_address,in_public_ip_address])
    S_No=S_No+1
fo.close()
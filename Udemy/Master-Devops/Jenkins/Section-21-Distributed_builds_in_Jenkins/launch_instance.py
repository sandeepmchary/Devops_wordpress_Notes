import boto3
region=input("Enter the region: ")
client= boto3.client('ec2',region_name=region)
ami = input ("Enter the ami id : ")
ins_type = input("Enter the Instance Type: ")
minimum_count = input("Enter the minimum count for the instances: ")
maximum_count = input("Enter the maximum count for the instances: ")
response=client.run_instances(
                                ImageId=ami,
                                InstanceType=ins_type,
                                MinCount=int(minimum_count),
                                MaxCount=int(maximum_count)
                             )
instance_ids=[]                           
for instance in response['Instances']:
    instance_ids.append(instance['InstanceId'])
print(instance_ids)
for instance in instance_ids:
    resp = client.create_tags(Resources=[instance],Tags=[{'Key': 'Name','Value': 'jenki'}])

for each_in in client.describe_instances()['Reservations']:
    for each_res in each_in['Instances']:
        for each_tags in each_res['Tags']:
            print("id:{0}\nState:{1}\nPublic_Dns_name:{2}\ntag:{3}".format(each_res['InstanceId'],each_res['State']['Name'],each_res['PublicDnsName'],each_tags['Value']))
            print("***********************************************") 


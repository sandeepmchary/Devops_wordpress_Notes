import boto3
aws_mgm_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mgm_con.client(service_name="ec2",region_name="us-east-2")
response=ec2_con_re.describe_volumes()['Volumes']
#print(response)
for each_item in response:
   # print(each_item)
    if not "Tags" in each_item and each_item['State']=='available':
        #print("The Volume id is: {}\nThe state of volume is: {}\nThe size of volume is :{}\n".format(each_item['VolumeId'],each_item['State'],each_item['Size']))
        print('Deleting Volume id',each_item['VolumeId'])
        ec2_con_re.delete_volume(VolumeId=each_item['VolumeId'])
print("Deleted Unused volumes")        

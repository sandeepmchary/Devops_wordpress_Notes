# HELP ON CLIENT OBJECT
import boto3
import pprint
aws_mgm_con=boto3.session.Session(profile_name="root")
# iam,ec2,s3
iam_con_cli=aws_mgm_con.client(service_name="iam",region_name="us-east-2")
ec2_con_cli=aws_mgm_con.client(service_name="ec2",region_name="us-east-2")
s3_con_cli=aws_mgm_con.client(service_name="s3",region_name="us-east-2")

# List all IAM users using client object
response=iam_con_cli.list_users()
# print(response)
#print(response['Users'])
for each_item in response['Users']:
    #print(each_item)
    print(each_item['UserName'])

# List all ec2 instances
# print(ec2_con_cli.describe_instances) or
response=ec2_con_cli.describe_instances()
# print(response)
#print(response['Reservations'])
for each_item in ec2_con_cli.describe_instances()['Reservations']:
    #print(each_item)
    #print(each_item['Instances'])
    # {} --- MEANS DICTIONARY
    # [] --- LIST
    # THE OUTPUT FOR THE ABOVE FOR LOOP AGAING HAVE DICTIONARY SO AGAGIN TAKING FOR LOOP
    # IN THE DICTIONARY IF WE NEED ANY PARTICULAR OPERATION (INSTANCEID,IMAGEID..ETC) USE ['OPERATION_NAME]
    # LIKE EACH_INSTANCE['INSTANCEID']
    for each_instance in each_item['Instances']:
        print(each_instance['InstanceId'])
    print('-------------------------------')



# List all buckets
response = s3_con_cli.list_buckets()
#print(response['Buckets'])
for each_bucket in response['Buckets']:
    print(each_bucket['Name'])



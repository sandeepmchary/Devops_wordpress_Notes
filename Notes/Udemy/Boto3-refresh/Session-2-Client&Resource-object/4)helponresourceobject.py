# HELP ON RESOURCE OBJECT
import boto3
aws_mgm_con=boto3.session.Session(profile_name="root")
iam_con_re=aws_mgm_con.resource(service_name="iam",region_name="us-east-2")
ec2_con_re=aws_mgm_con.resource(service_name="ec2",region_name="us-east-2")
s3_con_re=aws_mgm_con.resource(service_name="s3",region_name="us-east-2")
'''
# List all IAM Users
#print(iam_con_re.users)
#print(dir(iam_con_re.users))
#print(iam_con_re.users.all())

for each_item in iam_con_re.users.all():
    #print(dir(each_item))
    #print(each_item.user_name)

for each_item in iam_con_re.users.limit(2):
    print(each_item.user_name)
'''
# For S3 Bucket
for each_bucket in s3_con_re.buckets.all():
    #print(each_bucket)
    #print(dir(each_bucket))
    print(each_bucket.name)
  
    
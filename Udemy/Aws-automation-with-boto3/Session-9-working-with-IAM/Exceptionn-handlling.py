import boto3
from pprint import pprint
iam_user=input("Enter Iam user name: ")
session=boto3.session.Session(profile_name="root")
iam_re=session.resource(service_name="iam",region_name="us-east-2")
req_iam_user=iam_re.User(iam_user)
#pprint(dir(req_iam_user))
print ("IAM User: boto3-user details ")
# Here we are trying if the iam-user is there it will work
try:
    print(("User Name :{}\nUser Id: {}\nUser ARN:{}\nUser AccessKey:{}\nUser LoginProfile {}\nUser Creation Date: {} ".format(req_iam_user.user_name,req_iam_user.user_id,req_iam_user.arn,req_iam_user.access_keys,req_iam_user.LoginProfile,req_iam_user.create_date)))
# if the iam-user is not there this will execute
except Exception as e:
    print (e.response['Error']['Code'])
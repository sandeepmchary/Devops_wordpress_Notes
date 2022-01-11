import boto3
from pprint import pprint
session=boto3.session.Session(profile_name="root")
iam_re=session.resource(service_name="iam",region_name="us-east-2")
IAMNam=input("Enter your iam user name: ")
req_user_name=iam_re.User(IAMNam)
#pprint(dir(req_user_name))
print("User Name: {}\nUser ID: {}\nUser Creation Date : {}".format(req_user_name.user_name,req_user_name.user_id,req_user_name.create_date))
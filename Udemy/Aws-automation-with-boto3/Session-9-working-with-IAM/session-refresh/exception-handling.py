import boto3
session=boto3.session.Session(profile_name="root")
iam_re=session.resource(service_name="iam",region_name="us-east-2")
iam_user=input("Enter the user name: ")
req_usrname=iam_re.User(iam_user)
try:
    print("UserName:{}\nUserID:{}\nUserArn:{}".format(req_usrname.user_name,req_usrname.user_id,req_usrname.arn))
# if we give username not in the iam user list then this block will execute
# if we do dir(e) we have an function called response
except Exception as e:
    print (e.response)['Error']['Code']
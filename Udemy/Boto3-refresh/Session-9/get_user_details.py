import boto3
import datetime
iam_re = boto3.resource('iam')
iam_cli = boto3.client('iam')
# Get details of any iam users
user_ob=iam_re.User("admin")
#print("User name: {0}\nUser_id:{1}\nUser_arn:{2}\nUser_Create_date:{3}".format(user_ob.user_name,
                                                                               #user_ob.user_id,
                                                                               #user_ob.arn,
                                                                               #user_ob.create_date.strftime("%y-%m-%d")))
for user_ob in iam_re.users.all():
    print(user_ob)
    print("User name: {0}\nUser_id:{1}\nUser_arn:{2}\nUser_Create_date:{3}".format(user_ob.user_name,user_ob.user_id,user_ob.arn,user_ob.create_date.strftime("%y-%m-%d")))

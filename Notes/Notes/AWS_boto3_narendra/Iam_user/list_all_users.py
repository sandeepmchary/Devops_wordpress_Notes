import boto3
iam=boto3.client('iam')
users=iam.list_users()
for user in users['Users']:
    #print(user)
    print("UserName:{0}\nUserId:{1}\nArn:{2}\nCreateDate:{3}".format(user['UserName'],user['UserId'],user['Arn'],user['CreateDate']))
    print("==================")
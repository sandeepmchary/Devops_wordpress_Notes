import boto3
iam_re=boto3.resource('iam')
user=iam_re.User("admin")
#print(dir(user))
#print(user.user_name,user.user_id,user.arn,user.create_date)
print(user.user_name,user.user_id)


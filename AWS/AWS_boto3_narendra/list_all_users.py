import boto3
iam_re=boto3.resource('iam')
for each in iam_re.users.all():
    print(each.user_id,each.arn)
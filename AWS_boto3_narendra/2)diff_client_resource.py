import boto3
aws_mgt=boto3.session.Session(profile_name="root")
iam_re=aws_mgt.resource('iam','us-east-2')
iam_cli=aws_mgt.client('iam','us-east-2')
#Listing iam users with resources object
for each_user in iam_re.users.all():
	print(each_user.name)
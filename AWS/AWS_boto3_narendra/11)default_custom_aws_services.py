import boto3
iam_re=boto3.resource("iam")
for each_user in iam_re.users.all():
	print(each_user.name)
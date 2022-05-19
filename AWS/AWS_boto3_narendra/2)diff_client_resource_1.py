import boto3
aws_mgt=boto3.session.Session(profile_name='root')
iam_cli=aws_mgt.client('iam','us-east-2')
iam_re=aws_mgt.resource('iam','us-east-2')
#print(iam_cli.list_users())
#print(iam_cli.list_users()['Users'])
# above we get the list so we take for loop
for each in iam_cli.list_users()['Users']:
	#print(each)
	print(each['UserName'],each['UserId'],each['Arn'])
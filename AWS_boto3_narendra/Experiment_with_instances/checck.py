import boto3
iam_cli=boto3.client('iam')
response=iam_cli.list_users()['Users']
for each in response:
    print(each)
    break
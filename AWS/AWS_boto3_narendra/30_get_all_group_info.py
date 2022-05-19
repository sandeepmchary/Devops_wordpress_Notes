import boto3
iam_cli=boto3.client('iam')
response=iam_cli.list_groups()
for each_group in response['Groups']:
    print(each_group['GroupName'])
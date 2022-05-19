import boto3
iam_cli=boto3.client('iam')
ec2_cli=boto3.client('ec2')
s3_cli=boto3.client('s3')
# listing all users using client object
response=iam_cli.list_users()
resp=s3_cli.list_buckets()['Buckets']
for user in response['Users']:
    for s3_buc in resp:
        print(user['UserName'],s3_buc['Name'])
import boto3
sts_cli=boto3.client('sts')
response=sts_cli.get_caller_identity()
print(response)
'''
import boto3
session=boto3.session.Session(profile_name="root")
sts_cli=session.client("sts")
print (sts_cli.get_caller_identity().get("Arn"))

'''
'''
#!/usr/bin/python
import boto3
client=boto3.client("sts")
response = client.get_caller_identity()
print response
'''
import boto3
client=boto3.client("sts")
response = client.get_caller_identity(
)

print(response)
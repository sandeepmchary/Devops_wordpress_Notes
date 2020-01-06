import boto3
session=boto3.session.Session(profile_name="root")
iam_cli=session.client(service_name="iam",region_name="us-east-2")
print (iam_cli.list_groups())
for each_group in iam_cli.list_groups()['Groups']:
    print("Group Name:{}\nGroup ID:{}\nUser arn:{}\nUser Createdate:{}".format(each_group['GroupName'],each_group['GroupId'],each_group['Arn'],each_group['CreateDate']))
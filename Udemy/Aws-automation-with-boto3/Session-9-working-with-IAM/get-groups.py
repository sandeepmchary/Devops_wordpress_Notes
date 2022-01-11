import boto3
session=boto3.session.Session(profile_name="root")
iam_group_cli=session.client(service_name="iam",region_name="us-east-2")
for each_grp in iam_group_cli.list_groups()['Groups']:
	print ("Group Name={}\nGroup ID={}".format(each_grp['GroupName'],each_grp['GroupId']))
import boto3
session=boto3.session.Session(profile_name="root")
'''
iam_re=session.resource('iam')
# in instances we used instances.all() to list all the instances here we use users.all
# for all iam users
for each_user in iam_re.users.all():
    print ("User Name={}\nUser id={}\nUser ARN={}\nUser Create Date ={}".format(each_user.user_name,each_user.user_id,each_user.arn,each_user.create_date))
'''
iam_cli=session.client(service_name="iam",region_name="us-east-2")
#for each_iam in iam_cli.list_users():
	#print (each_iam['UserName'],each_iam['UserId'])
print (iam_cli.list_users())

    
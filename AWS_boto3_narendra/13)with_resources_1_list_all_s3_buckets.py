import boto3
# list ec2,iam and s3
ec2_re=boto3.resource('ec2')
iam_re=boto3.resource('iam')
s3=boto3.resource('s3')
'''
# List all IAM users
response=iam_re.users.all() 
# with resource we get iteratble so start using for loop
for each in response:
    #print(dir(each))
    #print(each.user_name)
    print(each.name)
    #break
'''
# list all buckets
response=s3.buckets.all()
#print(dir(response))
#for each in response:
#    print(each.name)
# Using limit here
for each in response.limit(1):
    print(each.name)
    
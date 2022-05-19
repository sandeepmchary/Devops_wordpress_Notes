import boto3
s3_re=boto3.resource('s3')
for each in s3_re.buckets.all():
    print(each.name)
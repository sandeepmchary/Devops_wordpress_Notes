import boto3
aws_con=boto3.session.Session(profile_name="root")
s3_re=aws_con.resource(service_name="s3",region_name="us-east-2")
s3_cli=aws_con.client(service_name="s3",region_name="us-east-2")
#print(s3_re.buckets.all())
for each_bucket_info in s3_re.buckets.all():
	#print(each_bucket_info)
	print(each_bucket_info.name)
import boto3
aws_con=boto3.session.Session(profile_name="root")
s3_cli=aws_con.client(service_name="s3",region_name="us-east-2")
#print(s3_cli.list_buckets().get('Buckets'))
for each_bucket_info in s3_cli.list_buckets().get('Buckets'):
	#print(each_bucket_info)
	print(each_bucket_info.get('Name'))
# PAGINATORS ARE APPLICABLE FOR CLIENT OBJECT
# S3 BUCKETS MAX WE CAN CREATE 100 BUCKETS AS AN EXAMPLE
# FOR LISTING ALL THE 100 BUCKETS OBJECTS
# FOR MAKING THE API CALLS & FOR GETTING THE RESULTS
# API CALLS MAKE LISTS MAX ONLY FOR 50 OR 100
# FOR ONCE QUERY
# EX: WE HAVE S3 BUCKET AND WE HAVE 1200 OBJECTS IN THE BUCKET
# TO LIST THE S3 OBJECTS WE MAKE SOME API CALLS
# FOR THE MORE OF 1000+ OBJECTS TO LIST WE NEED PAGES
# IN THE FIRST PAGE WE GET 1000 OBJECTS
# REMAINING 200 IN SECOND PAGE
# BOTO3 WILL GET THE INFO FOR S3 BUCKETS 
# FOR S3 BUCKET OBJECTS WE NEED PAGINATORS
import boto3
session=boto3.session.Session(profile_name="root")
s3_re=session.resource(service_name="s3",region_name="us-east-2")
bucket_name="dowithpython"
bukcet_object=s3_re.Bucket(bucket_name)
cnt=1
for each_obj in bukcet_object.objects.all():
	#print(cnt,each_obj) #for both name and key
	#print(cnt,each_obj.bucket_name) # for only name
	print(cnt,each_obj.key) # for getting all the key 
	cnt=cnt+1
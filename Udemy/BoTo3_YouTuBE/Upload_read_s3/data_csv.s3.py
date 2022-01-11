import boto3
import os
import sys
import datetime
import pandas as pd
from pprint import pprint
d=datetime.datetime.now()
print("Now the time is: ", d)


current_time="{}{}{}".format(d.month,d.year,d.month)
client = boto3.client('s3')
'''
response = client.create_bucket(
	     ACL='private',
	     Bucket='samsam{}'.format(current_time),
	     CreateBucketConfiguration={
	        'LocationConstraint':'us-east-2'
	     }
	     )
pprint(response)

with open("data.csv",'rb') as f:
	data=f.read()
resp = client.put_object(
	   ACL='private',
	   Bucket='samsam{}'.format(current_time),
	   Body=data,
	   Key='data.csv')
pprint(resp)

# THIS IS FOR LISTING ALL THE BUCKETS
bucket_name=[]
response=client.list_buckets()
for each in response['Buckets']:
	print(' The Bucket name is:', each['Name'])
	bucket_name.append(each['Name'])
#print(bucket_name)	
for each in bucket_name:
	for each_buc in client.list_objects(Bucket=each)['Contents']:
		pprint(each_buc['Key'])
		print("===========")
'''
# READ THE FILE FROM S3 BUCKET
# ON THE AMAZON CONSOLE SELECT THE FILE
# GO TO PERMISSIONS --> Access Control List --> Canonical ID
# GIVE THE READ AND WRITE PERMISSIONS
# ONLY SELECT {{Key}}
path = 's3://samsam720207/data.csv'
df = pd.read_csv(path)
print(df.head())


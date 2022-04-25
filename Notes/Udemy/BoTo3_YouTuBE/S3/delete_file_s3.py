import boto3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pprint import pprint
client = boto3.client('s3')
response = client.list_buckets()
bucket_name=[]
for each in response['Buckets']:
	print(f'The name of the backet is:', each['Name'])
	bucket_name.append(each['Name'])
print(bucket_name)
for each_bucket in bucket_name:
	resp=client.delete_object(
	     Bucket=each_bucket,
	     Key='lion.jpg',
	     )
pprint(resp)

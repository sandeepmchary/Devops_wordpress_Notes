import boto3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pprint import pprint
l_f=os.listdir()
print(l_f)
d=datetime.datetime.now()
print(d)
current_time="{}{}{}".format(d.month,d.day,d.year)
print(current_time)
client = boto3.client('s3')
'''
response=client.create_bucket(
	       ACL='private',
	       Bucket='samantha{}'.format(current_time),
	       CreateBucketConfiguration={
	          'LocationConstraint':'us-east-2'
	       }
	       )
print(response)
'''
# upload files to s3 Buckets
'''
with open("Cute-.jpg",'rb') as f:
	data=f.read()
#print(data)
response=client.put_object(
	      ACL='private',
	      Bucket='samantha{}'.format(current_time),
	      Body=data,
	      Key='Cute-.jpg')
pprint(response)
'''
# again with lion file
with open("lion.jpg",'rb') as f:
	data=f.read()
response=client.put_object(
	      ACL='private',
	      Bucket='samantha{}'.format(current_time),
	      Body=data,
	      Key='lion.jpg')
print(response)

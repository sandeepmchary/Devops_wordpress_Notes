#!/usr/bin/python
import boto3
s3_re=boto3.resource("s3","us-east-2")
for each_bucket in s3_re.buckets.all():
    print each_bucket
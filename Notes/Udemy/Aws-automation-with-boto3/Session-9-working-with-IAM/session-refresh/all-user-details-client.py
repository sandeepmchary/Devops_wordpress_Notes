#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
iam_cli=session.client("iam","us-east-2")
# in client we have to use dictionary operations
for each_user in iam_cli.list_users()['Users']:
    print("User Name:{}\nUser ID:{}".format(each_user['UserName'],each_user['UserId']))
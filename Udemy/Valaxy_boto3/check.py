#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import boto3
import json
import pdb


client = boto3.client('ec2')
resp = client.describe_instances()

"""
Funtion to get the Intance IDs
@arg - response from boto describe instances call
Returns a dictionary , Key - Instance ID, Value (Type :Dict) : Status & Tag-Name
"""
def getInstanceId():
    # Describe instances returns an dict of reservations
    instanceDict = {}

    if resp['Reservations']:
        for item in resp['Reservations']:
            if item['Instances']:
                instanceMetaData = {}
                instanceMetaData[ 'Status' ] = item['Instances'][0]['State']['Name']
                instanceMetaData[ 'Tag-Name' ] = item['Instances'][0]['Tags'][0]['Value']
            instanceDict[ item['Instances'][0]['InstanceId'] ] = instanceMetaData
    print(instanceDict)
getInstanceId()    
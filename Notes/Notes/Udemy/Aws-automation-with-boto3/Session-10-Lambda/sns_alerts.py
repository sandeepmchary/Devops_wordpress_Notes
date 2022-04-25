import boto3
import json
client = boto3.client('sns')
def lambda_handler(event, context):
    topic_arn='arn:aws:sns:us-east-2:199651813682:stop-ec2'
    message='Ec2 is down'
    client.publish(TopicArn=topic_arn,Message=message)

# select the sns --> topics --> create topics --> give some name -- > create topic
# after this we need Subscriptions --> create one select the created topic 
# select the Protocol --> sms or email --> Create Subscription
# after this we need create a policy for sns and cloudwatch logs and add this policy to a role 
# in the role search for the created policy name and append to items
# 
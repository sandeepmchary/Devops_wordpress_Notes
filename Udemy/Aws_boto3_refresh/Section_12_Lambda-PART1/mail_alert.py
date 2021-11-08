import json
import boto3

def lambda_handler():
    ec2_re=boto3.resource('ec2')
    sns_cli=boto3.client('sns')
    my_ins = ec2_re.Instance('i-0532ec7cf1d7603ac')
    print(my_ins.state['Name'])
    sns_cli.publish(TargetArn="arn:aws:sns:us-east-1:122453661730:Mail_Alert",Message=my_ins.state['Name'])
lambda_handler()    
'''
for sns
  - Create topic --> Name --> Display name - optional --> Create subscription --> Protocol --> Email -->Endpoint
    --> email id --> go to email and confirm the subscription
after this go to cloud watch --> create rule --> Event patter --> service name --> ec2 --> Ec2 instance state
change notifications --> specific change --> running or stopped --> any instance or specific instance -->
Target --> Add target --> select the above written function --> configure details --> 

- Target arn should be same as Topic arn while creating for the subscription 
'''
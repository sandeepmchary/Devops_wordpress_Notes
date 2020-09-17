import boto3
ec2_cli=boto3.client('ec2')
response=ec2_cli.create_image(
	      )
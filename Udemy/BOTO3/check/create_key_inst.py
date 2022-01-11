import boto3
ec2_cli=boto3.client('ec2')
outfile=open('ec2_key.pem','w')
keypair=ec2_cli.create_key_pair(KeyName='ec2_key')
outfile.write(keypair['KeyMaterial'])
instance=ec2_cli.run_instances(
         ImageId='ami-0affd4508a5d2481b',
         InstanceType='t2.micro',
         MinCount=1,
         MaxCount=1,
         KeyName='ec2_key',
         SecurityGroupIds=['All_TCP_IP'],
         TagSpecifications=[
         {
         'ResourceType':'instance',
         'Tags':[
         {
         'Key':'Name',
         'Value':'with-python'
         }
         ]
         }
         ]
	     )
    

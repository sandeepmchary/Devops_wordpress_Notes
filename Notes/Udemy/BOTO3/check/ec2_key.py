import boto3
ec2_re=boto3.resource('ec2')

# Create a file to store the key
outfile=open('ec2_key_pair.pem','w')
keypair=ec2_re.create_key_pair(KeyName='ec2_key_pair')
# this key_material comes from the dir of keypairs print(dir(keypair))
keypairout=str(keypair.key_material)
print(keypairout)
outfile.write(keypairout)

instance=ec2_re.create_instances(
	     ImageId='ami-0affd4508a5d2481b',
         InstanceType='t2.micro',
         MinCount=1,
         MaxCount=1,
         KeyName='ec2_key_pair'
	     )
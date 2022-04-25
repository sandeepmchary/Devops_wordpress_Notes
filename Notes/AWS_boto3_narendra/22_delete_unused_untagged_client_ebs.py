import boto3
ec2_cli=boto3.client('ec2')
response=ec2_cli.describe_volumes(
    Filters=[
        {
            "Name":"status",
            "Values":['available']
        }
    ]
    )
del_vol=[]
for each_vol in response['Volumes']:
    #print(each_vol)
    #print(each_vol['VolumeId'])
    #print(each_vol['VolumeId'],each_vol['Tags'])
    # NOW WE WANT TAGS WHICH IS NOT HAVING THE TAGS
    if not "Tags" in each_vol and each_vol['State']=='available':
        print(each_vol['VolumeId'])
        ec2_cli.delete_volume(
                                VolumeId=each_vol['VolumeId']
                                )

for each_vol in response['Volumes']:
    print(each_vol['VolumeId'])
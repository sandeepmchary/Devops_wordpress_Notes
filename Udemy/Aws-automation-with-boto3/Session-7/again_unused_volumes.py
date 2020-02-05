import boto3
session=boto3.session.Session(profile_name="root")
ec2_re=session.resource("ec2")
ec2_cli=session.client("ec2")
unused={'Name':'tag:Name','Values':['dellen']}
all_req_vol_ids=[]
for each_vol in ec2_re.volumes.filter(Filters=[unused]):
    #print(each_vol.id,each_vol.state)
    all_req_vol_ids.append(each_vol)
    print("the volume id's are {}".format(all_req_vol_ids))
    print("each Volume {}".format(each_vol))
    each_vol.delete()

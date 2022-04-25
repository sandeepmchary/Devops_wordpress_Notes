import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
running_filters={"Name":"instance-state-name","Values":["running"]}
stopped_filters={"Name":"instance-state-name","Values":["stopped"]}
zone_filters={"Name":"availability-zone","Values":["us-east-2b"]}
insta_type={"Name": "instance-type","Values": ["t2.micro"]}
# FILTERS USING TAGS
ftags={"Name": "tag:Name","Values": ["udemy-boto3","master"]}
for each_in in ec2_con_re.instances.filter(Filters=[ftags],InstanceIds=['i-0f8e31fd646541373','i-0cc45f8ba2faaa1ca'],DryRun=True
):
    print (each_in.id, each_in.state)

    


#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-2")
while True:
    in_id=raw_input("Enter your Instance id: ")
    my_inc=ec2_con_re.Instance(id=in_id)
	print "1. start"
	print "2. stop"
	print "3. reboot"
	print "4. terminate"
	print "5. Exit"
	option=input("Enter your action by selecting the number from 1-5")
    if option==1:
    print "please wait we are starting your Instance"
    my_inc.start()
    elif option==2:
        print "starting"
        my_inc.start()
    elif option==3:
        print "stopping"
        my_inc.stop()
        
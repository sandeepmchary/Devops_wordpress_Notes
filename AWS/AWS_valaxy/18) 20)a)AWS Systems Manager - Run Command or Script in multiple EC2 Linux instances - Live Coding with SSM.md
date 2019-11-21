<pre>
# AWS SYSTEMS MANAGER - SSM
* Run commands /scripts in multiple EC2 instances
# STEPS
- iam roles
- create role
- select EC2
- select EC2 role for simple systems manager
- next
- policy
- review
- role name: Ec2-role-for-ssm
- create role
- create 2 instances
- select role Ec2-role-for-ssm
- go to Advanced Detials

* # install AWS SSM
cd /tmp
sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
yum install -y amazon-ssm-agent.rpm
sudo systemctl start amazon-ssm-agent
sudo systemctl enable amazon-ssm-agent


* Add tags:
Name: ssm-demo
ENV: Prod
OS: Linux
* after installation  
* SYSTEMS MANAGERS SERVICES
* run command
* run command
* run a shell script
* select instances
* commands
#/bin/bash
echo -e "{ 'Hostname':'`curl http://169.254.169.254/latest/meta-data/local-hostname --silent`', \ \n 
'AMI-ID':'`curl http://169.254.169.254/latest/meta-data/ami-id --silent`', \ \n 
'Kernel-Version':'`rpm -q kernel`' \ \n 
'Instance Type':'`curl http://169.254.169.254/latest/meta-data/instance-type --silent`' }"
* click run
* select the command id 
* select the command id choose the output
* view output
------
what if i want to run on a few instances
-- use tagging
- run the shell script
- Select targets by :specifying a tag
* select the tag : prod
* paste the same command
* run


</pre>
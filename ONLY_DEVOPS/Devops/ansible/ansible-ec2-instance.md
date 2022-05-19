# AWS EC2 Instance Creation Using Ansible Playbook Automation

Amazon Web Services is introduced term called “Infrastructure as a Code” where you no need to provisioning and maintenance manually everything is going to be peace of code. In this case Ansible AWS EC2 Instance creation using ansible playbook which provides automated provisioning of EC2 instances.

No need of manual login to AWS EC2 console and clicking and creating instances, use feature to provision/create ansible is the power full tool.
# AWS EC2 Instance Creation Using Ansible
Preparing Environment before invoking playbook

I am using Centos 7.4 Operating System version as Ansible main node. To communicate with AWS we are going to use boto / boto3 aws
<pre>
# yum install python python-setuptools* ansible git curl wget
# curl -O https://bootstrap.pypa.io/get-pip.py
# python get-pip.py 

$ python --version
Python 2.7.5

$ pip --version
pip 18.1 from /usr/lib/python2.7/site-packages/pip (python 2.7)

# pip install boto 
# pip install boto3
</pre>
Use this Amazon lab practice guide to create IAM user with programmatic access and user should have access to create/launch EC2 instance

Create a boto file with access key and access secret id to authenticate to aws
<pre>
# vi ~/.boto

[Credentials]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
</pre>
# Write Ansible Playbook to launch aws ec2 instance

    Define Variables
    Tasks
        Create New Security Group
        Launch EC2 Instance
        Add Tags for identification
* Look for spinawsec2.yml file
<pre>
---
  - name: Provision an EC2 Instance
    hosts: localhost
    connection: local
    gather_facts: False
    tags: provisioning

    vars:
      instance_type: t2.micro
      security_group: webservers
      image: ami-0080e4c5bc078760e
      region: us-east-1
      keypair: sshkeypair
      count: 1

    tasks:

      - name: Create New security group with below given name
        local_action:
          module: ec2_group
          name: "{{ security_group }}"
          description: Security Group for Newly Created EC2 Instance
          region: "{{ region }}"
          rules:
            - proto: tcp
              from_port: 22
              to_port: 22
              cidr_ip: 0.0.0.0/0
            - proto: tcp
              from_port: 80
              to_port: 80
              cidr_ip: 0.0.0.0/0
          rules_egress:
            - proto: all
              cidr_ip: 0.0.0.0/0


      - name: Launch the new t2 micro EC2 Instance
        local_action: ec2
                      group={{ security_group }}
                      instance_type={{ instance_type}}
                      image={{ image }}
                      wait=true
                      region={{ region }}
                      keypair={{ keypair }}
                      count={{count}}
        register: ec2

      - name: Wait for EC2 Instance to Spin-up and ready for SSH access
        local_action: wait_for
                      host={{ item.public_ip }}
                      port=22
                      state=started
        with_items: "{{ ec2.instances }}"

      - name: Adding Tags to Identify
        local_action: ec2_tag resource={{ item.id }} region={{ region }} state=present
        with_items: "{{ ec2.instances }}"
        args:
          tags:
            Name: Web Server
            Owner: Ravi Kumar
            PurPose: Testing EC2 Instance From Ansible
</pre>
Pro’s and Con’s

Using this ansible playbook aws ec2 instance creation can be done, however every time when you want to launch remember to change below variable values

    AMI ID
    Region
    Instance Type
    Security Group Name
    SSH Key Pair Name
    Count of instances to be created

To make play book more flexible and interactive delete vars section and pass the same variables on playbook execution
<pre>
    vars:
      instance_type: t2.micro
      security_group: webservers
      image: ami-0080e4c5bc078760e
      region: us-east-1
      keypair: NVirginia
      count: 1
</pre>

Example of passing variables while running ansible playbook
<pre>
ansible-playbook spinawsec2.yml -e instance_type=t2.micro -e security_group=WebServers -e image=ami-0080e4c5bc078760e -e region=us-east-1 -e keypair=NVirginia -e count=1
</pre>
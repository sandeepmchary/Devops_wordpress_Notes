#Class 2
-------------------
<pre>validate the installation of ansible 
    rpm -qa | grep ansible
Information about the package
    rpm -ql ansible...noarch(full) | more
creating user with home directory
    useradd -d /home/ansadm -m ansadm
changing the user to non expiry 
    passwd -x -l ansadm
    
Creating password less authentication
    ssh-keygen on the ansible server
    mkdir .ssh on the home directory on the client system
    chmod 700 .ssh/
    chown ansible:ansible .ssh/
    cd .ssh
    vi authorized_keys</pre>
    
--------------------------------------------------
#Class 3
---------
<pre>ansible configuration file and commands

under /etc/ansible/hosts
create a groups for the servers
----
/etc/ansible/ansible.cfg
    we can change the fork values here the default is 5 
--> Ansible communicate on port 22 (ssh)
--> To list out all the modules in ansible
        ansible-doc -l  | more
--> To we view count of ansible module
    ansible-doc -l | wc -l
--> To check module function 
    ansible-doc -s (yum)
    ansible-doc -s (module name)
--> -m (module) -- 
           ansible -m ping
           ansible all -m ping
--> -o for view the above result in single line
    ansible all -m ping -o
--> shell -- we can add commands here   
    ex: ansible all -m shell -a "uname-a;df -h"
--> with module if we want to use any command use -a 
--> -s use sudo on the client system
---> Installing the httpd with yum command only
ansible (server or groupname) -m yum -a "name=httpd state=present" -s
--> ansible (server or groupname) -m service -a "name=httpd state=started" -s
-------------------------------------------------
--> copy module
    create a file in /tmp/testingfile
    echo "test form ansadm" > /tmp/testingfile
    ansible all -m copy -a "src=(file path) dest=(file path)" -s
--> check for the se-linux status 
    sestatus
--> or some python might miss on the client server, install that </pre>
-----------------------------------------------
    


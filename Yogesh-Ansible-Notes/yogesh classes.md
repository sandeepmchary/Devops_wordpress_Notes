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
# class 4 
<pre>ONLY ROLES EXPLAINED</pre>
-----------------------------------
# CLASS 5
<pre>* creating AWS EC2 instance
fully yml files </pre>
-----------------------------------
# Class 6
</pre>This is for patching the servers
--> ansible -m setup (all) | grep ansible_distribution
--> ansible (server names or groupname) -m shell -a "uname -a;uptime"
--> if we want to limit it to one server use -l 
--> serial it will run serial way


* Usermanagement yml files</pre>
------------------------------------
# Class 7
<pre>Playbook demo 
ansible-playbook (file.yml) -i (location of the host file) -l(for the one server only) (server name)</pre>
------------------------------------------
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
# class 4 
<pre>ONLY ROLES EXPLAINED</pre>
-----------------------------------
# CLASS 5
<pre>* creating AWS EC2 instance
fully yml files </pre>
-----------------------------------
# Class 6
</pre>This is for patching the servers
--> ansible -m setup (all) | grep ansible_distribution
--> ansible (server names or groupname) -m shell -a "uname -a;uptime"
--> if we want to limit it to one server use -l 
--> serial it will run serial way
* Usermanagement yml files</pre>
------------------------------------
# Class 7
<pre>Playbook demo 
ansible-playbook (file.yml) -i (location of the host file) -l(for the one server only) (server name)</pre>
------------------------------------------
# Class 8
<pre>perform password hashing
and use hashed password with ansible

what is password hashing?
to take variable length password as input and creating a cryptic,fixed length password from it using cryptic mechanism
    To make your hashed password more secure ,we can in our input,Salt is a random value used for generated hashed password 

Methods to generate
1) There are different hashing algorithms , the most commonly being used is MD5 and SHA,sha-512 is the secure algorithms on the date

*Using Python :
# python -c 'import crypt,getpass; print crypt.crypt(getpass.getpass())'
 Above command with add randon salt and prompt user to type passord. This method used sha-512 as hash method 
*Using openssl: (With Randon salt)  
# openssl passwd -1 -salt $(openssl rand -base64 6) SecurePass 


ansible (server) -m shell -a "authconfig --test | grep password hashing algorithm" -s
--> python -c 'import crypt,getpass; print crypt.crypt(getpass.getpass())'
--> it will ask for the password give any password
    if the starting of the hash password is $6 is sha-512 and $5 is sha-256 and $1 is MD5</pre>
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Ansible vault
<pre>  ansible-vault create (file name)
   ansible-vault edit test1.yml(for editing the file it will ask for the password)
   ansible-vault encrypt test1.yml
   ansible-playbook test1.yml --ask-vault-pass(for ruuning the playbook with password)</pre>
   
    



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Ansible vault
<pre>  ansible-vault create (file name)
   ansible-vault edit test1.yml(for editing the file it will ask for the password)
   ansible-vault encrypt test1.yml
   ansible-playbook test1.yml --ask-vault-pass(for ruuning the playbook with password)</pre>
   
    



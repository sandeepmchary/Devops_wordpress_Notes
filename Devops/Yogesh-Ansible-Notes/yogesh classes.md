
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
<pre> curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install boto boto3 </pre>

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
----------------------------------
# Class 9
Configuring and Managing the NTP client on the Enterprise servers is one of the tasks for systems administrators. 


NTP client is responsible for the time sync of client server with the time sources. Assume a scenario, you have to configure NTP client on multiple servers and in manual way it is going to take long time and always chance of error. 


How if we Ansible to perform this tasks? 
I have written a small playbook, which you can customize further to install, configure and manage the NTP client on Linux/Unix Systems. Below modules as part of tasks 
1. Yum
2. Template
3. Service 


Along with modules, I have used variables and handlers to make this demo playbook more efficient. 
---- Technical ______
<pre> anisble all -m shell -a "ntpq -p"</pre>
<pre> anisble (server names or group names) -m shell -a "ntpq -p"</pre>
<pre> ansible all -m shell -a "rpm -qa | grep ntp" </pre> 
# CHRONY IS NOT RECOMMEDED ON ENTERPRISE SYSTEM, THESE ARE SUITABLE FOR SHORT PERIOD OF TIME 
* the use of two tags is that if we use that single tags which are there in both the tasks, the both tasks will excuted

--> backup = yes (if any the same file is already there, with backup module, the first file is backuped and the coming file will be copied here)
--------------------------------------------------------------------------------------------------
# Class 10 roles for hardening confusing also
-----------------------------------------------------
# Class 11

<pre>*List all tasks in the playbook 
* ansible-playbook playbook.yml --list-tasks</pre>

<pre>*Start the play from a particular task 
*ansible-playbook playbook.yml --start-at-task="task name" </pre>

<pre>*Start the play step by step with interactive way. This will prompt the user for to confirm each task before running. 
*ansible-playbook playbook.yml --step </pre>

<pre>Check syntax of the playbook 
ansibe-playbook playbook.yml --syntax-check </pre>

<pre>Execute the playbook in the check (dry-run) mode ,which check what changes will be performed.
ansible-playbook playbook.yml --check </pre>

<pre>List hosts on which playbook will be executed 
ansible-playbook playbook.yml --list-hosts -1 subset </pre>

<pre>List tags in the playbook 
ansible-playbook playbook.yml --list-tags </pre>

<pre>Only run plays and tasks tagged with these tag values 
ansible-playbook playbook.yml --tags tagl,tag2...tagN </pre>

<pre>Skip the tasks associated with specific tasks 
ansible-playbook playbook.yml --skip-tags tag1,tag2...tagN </pre>

<pre>The --forks what lets ansible run on multiple hosts in parallel. NUM is specified as an integer, the default is 5. 
ansible-playbook playbook.yml --forks-NOM </pre> 

<pre>Run a playbook on the target hosts without inventory files.
ansible-playbook playbook.yml -1 (IP I ServerName] </pre>
------------------------------------------------------------------------------------------------------------


    



<pre>
# ANSIBLE
- $sudo su -
- $ sudo apt-get update
- $ echo "ansible ALL=(ALL) NOPASSWD:ALL " >> /etc/sudoers
- $ adduser ansible
- $ passwd ansible
- $ su ansible
- $ sed -ie 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
- $ service sshd restart
- for ubuntu 
- $service sshd stop 
- $service sshd start
- ssh-keygen
- ssh-copy-id (user)@private dns
- ---- Installing ANSIBLE ----
$ sudo apt-get update
$ sudo apt-get install software-properties-common -y
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt-get install python -y
------
# ANSIBLE COMMANDS:
$ ansible -m ping all
# check for the server and node for the same python version
$ python --version
********************************************************************************************************************************
---
- hosts: localhost
  tasks:
  - name: ping all
      ansible -m ping all
***********
---
- hosts: localhost
  tasks:
  - name: Execute ansible on hosts
      ping
********************************************************************************************************************************
### for sudo apt-get update we have ## update_cache:yes
update_cache: yes
state:present
***********
- name: packages in ubuntu
  tasks:
  - name: git
    update_cache: yes
    state: present
  - name: tree
    state: present
  - name: git
    state: absent (to remove git)
********************************************************************************************************************************
- steps on ACS(Ansible Control Server)
- adduser ansible
- $ echo "ansible ALL=(ALL) NOPASSWD:ALL " >> /etc/sudoers
- $ sed -ie 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
- $ service sshd restart
- for ubuntu 
- $service sshd stop 
- $service sshd start
- su - ansible
- cd ~
- cp /etc/ansible/hosts .
# To insert the servers names in ansible hosts
sudo bash -c 'echo *private ip address* >> /etc/ansible/hosts'
- add hosts in /etc/ansible/hosts
- ssh-copy-id host@ip
********************************************************************************************************************************
## as the python is already installed on the rhel/centos we need to install pyhton on ubuntu based systems
- $ sudo apt-get update
- $ sudo apt-get install software-properties-common -y
- $ sudo apt-add-repository --yes --update ppa:ansible/ansible
- $ sudo apt-get install python -y
********************************************************************************************************************************
# LAMP ON UBUNTU
create a lamp.yml
################################################################################################################################
---
- hosts: all
  become: yes
  tasks:
  - name: update and install apache
    apt:
      name: apache2
      state: present
  - name: restart apache after installation
    service:
      name: apache2
      state: restarted
      enabled: yes
  - name: Install PHP packages
    apt:
      name: "{{ item }}"
      state: present
    with_items:
      - php5
      - libapache2-mod-php5 
      - php5-mcrypt
  - name: Restart after the php packages
    service
      name: apache2
      state: restarted
################################################################################################################################# on Centos
---
- hosts: all
  become: yes
  tasks:
  # sudo yum install httpd
  - name: install httpd
    yum:
      name: httpd
      state: present
   # sudo systemctl stop httpd.service
   # sudo systemctl start httpd.service
   # sudo systemctl enable httpd.service
  - name: restart after installation
    service:
      name: httpd
      enabled: yes
      state: restarted
    # sudo yum install php php-mysql
  - name: install php packages
    yum:
      name: "{{ item }}"
      state: present
    with_items:
      - php 
      - php-mysql
  - name: Restart apache after php 
    service:
      name: httpd
      state: restarted
  - name: create file
    file:
      path: /var/www/html/index.html
      state: file
################################################################################################################################
# on Centos
---
- hosts: all
  become: yes
  tasks:
  # sudo yum install httpd
  - name: install httpd
    yum:
      name: httpd
      state: present
    notify:
      - restart apache
    # sudo yum install php php-mysql
  - name: install php packages
    yum:
      name: "{{ item }}"
      state: present
    with_items:
      - php 
      - php-mysql
    notify:
      - restart apache
   - name: php file
     blockinfile:
     dest: /var/www/html/info.php
     block: |
      <?php phpinfo(); ?>
     backup: yes
  
   handlers:
     - name: Restart apache
         service:
           name: httpd
           state: restarted
################################################################################################################################# HOW TO WRITE SCRIPTS FOR 2 OS'S

- copy all the entries to another location
- $ cp /etc/ansible/hosts len/myinventory

          
     

    
    






































</pre>
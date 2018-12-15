Delopying with jenkins and ansible
a) code commit -- git
b) build test -- jenkins
c)Intialize ansible
d)Apache tomcat

1) login to jenkins server same as before in the project
2) in the Ansible server we have to create the user and give password less authentication
 for creating the ansible user and password less authentication
 a) $sudo su -
 $useradd ansadmin
 $passwd ansadmin
 $visudo
 #same thing without password
 $ansadmin ALL=(ALL) NOPASSWD:ALL (!wq)
 vi /etc/ssh/sshd_config 
 $Password Authentication yes
 $ sudo service sshd restart
 3)in Ansible server su - ansadmin
 cd ~
 ssh-keygen
 ssh-copy-id ansadmin@<tomcat private dns name > 
 # for this to happen the java is needed while installing the tomcat java is installed along with the tomcat #

 once check for that ssh ansadmin@<tomcat private dns> if you are logged in it went successful
 $ cp /etc/ansible/hosts hosts_backup # Backup for the host file
 add the <tomcat private dns name > to /etc/ansible/hosts # while installing the ansible this folder is creaed #
 # for checking the connection status
  $ ansible -m ping all
  
 4) in the ansible server write a playbook 
 
 vi copyfile
 ---
 - hosts : all
   become : true
   tasks:
     - name : copy war into tomcat server
       copy:
         src: /opt/playbook/webapp/target/webapp.war
         dest: /opt/apache-tomcat/webapps
            
 
 
 
 4) same useradd in the tomcat also
 $ useradd ansadmin
 $ passwd ansadmin
 $ visudo
 #same thing without password
 $ansadmin ALL=(ALL) NOPASSWD:ALL (!wq)
  vi /etc/ssh/sshd_config 
 $Password Authentication yes
 $ sudo service sshd restart
 
 5) Install publish over ssh in the jenkins server 
 Manage plugin
 >> Aviable
 >> publish over ssh
 >> install without restart

 Manage Jenkins >> system configuration  >> check for the publish over ssh >> ADD >> we will get server name >> < name of the ssh server > <ansible_server>  >>
 <Host name > <private ip of the ansible file >// >> click Advanced >> use password authentication or use a different key >> enter the password >> Test the connection >> save and apply >> 
 
 under post steps in the jenkins main page
 select >> send files or execute commands over SSH >> select the target system  
 source files <webapp/target/*.war> # or else the copy the war file to the file directory #
 # else give the git path in the jenkins git folder option #
 
 Remote Directory < //opt//playbooks >
 
 #it is not a good practice to give the two different tasks to the single send files or execute commands over SSH it might fail #
again select the ansible_server >> Exec command <<ansible-playbook /opt/playbook/copyfile>> apply >> save
build now 

< tomcat public ip address >:8080

 
 
 
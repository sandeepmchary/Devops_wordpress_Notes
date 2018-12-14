Login to jenkins server
check for the "maven plugins" in pluguins install it without restart
hello-world name of the project

Make sure that git is installed in the jenkins server
paste the link into the git link https://github.com/sandeepmchary/hello-world-master.git




Under Build 
-------------
Root POM is POM.xml
Goals and options : clean install package

now apply and save 

run the build now options
the archived file .war file will stored in the /var/lib/jenklins/workspace/hello-world/webapp/target/webapp.war

The above can shown under in the build success 

---- Make sure tomcat is up and running in the another server  ---
in jenkis server 

go to credentials
select jenkins 
global credentials
add credentials

for deploying a war files through jenkins the user must have manager-script role 
give id and password 
id deployer
passwdd deployer
save

in Jenkins server under post build actions

add post build actions -- we cannot find any option to deploy any war or ear file option for that we need to install $$ Deploy to Container $$

after installing $$ Deploy to Container $$ we will get Deploy war or ear to a container option is shown in the post build options

( post build => Deploy war or ear to container)

war /ear files : < we need to provide the path > (**/*.war) or (/var/lib/jenklins/workspace/hello-world/webapp/target/webapp.war) as per in this case only
containers => tomcat 8 => provide credentials and tomcat url 

save and apply

Then it will be shown on the tomcat server 

In jenkins server go to 

Build Triggers => select POLL SCM => */2 * * * * 

if we change the any thing in the github the same will be updated in the jenkins server with in 2 minutes
 



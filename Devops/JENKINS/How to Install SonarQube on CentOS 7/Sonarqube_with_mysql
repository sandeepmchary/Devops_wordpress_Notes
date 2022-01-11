Sonarqube Installation on centos 7/Rhel
Install mysql:
Create db and user for Sonarqube:
Download and install SonarQube:
Create a user for SonarQube:
Configure sonarqube with MySQL database:
Start SonarQube
Configuring sonarqube as a Systemd service:
restart the sonar service with systemd:

# Sonarqube Installation on centos 7/Rhel
## Install mysql:
sudo yum install wget unzip -y
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum update -y
sudo yum install mysql-server
sudo systemctl start mysqld

### Create db and user for Sonarqube:
mysql -u root
CREATE DATABASE sonarqube_db;
CREATE USER 'sonarqube_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON sonarqube_db.* TO 'sonarqube_user'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
exit

### Download and install SonarQube:
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-6.7.6.zip
unzip sonarqube-6.7.6.zip
mv sonarqube-6.7.6 /opt/sonarqube

### Create a user for SonarQube:
useradd sonarqube
passwd sonarqube
chown -R sonarqube:sonarqube /opt/sonarqube


vi /opt/sonarqube/bin/linux-x86-64/sonar.sh
#add below line
RUN_AS_USER=sonarqube

### Configure sonarqube with MySQL database:
vi /opt/sonarqube/conf/sonar.properties add the below lines

#vi /opt/sonarqube/conf/sonar.properties
#add below lines
sonar.jdbc.username=sonarqube_user
sonar.jdbc.password=password
sonar.jdbc.url=jdbc:mysql://localhost:3306/sonarqube_db?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true&useConfigs=maxPerformance

## Start SonarQube
/opt/sonarqube/bin/linux-x86-64/sonar.sh start
sudo /opt/sonarqube/bin/linux-x86-64/sonar.sh stop

## Configuring sonarqube as a Systemd service:
sudo vi /etc/systemd/system/sonar.service
add below lines

[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking

ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop

User=sonarqube
Group=sonarqube
Restart=always

[Install]
WantedBy=multi-user.target

### restart the sonar service with systemd:

sudo systemctl restart sonar
sudo systemctl start sonar
sudo systemctl enable sonar




























# Install Tomcat
sudo yum install tomcat
# open /usr/share/tomcat/conf/tomcat.conf file to change the java heap memory
JAVA_OPTS="-Djava.security.egd=file:/dev/./urandom -Djava.awt.headless=true -Xmx512m -XX:MaxPermSize=256m -XX:+UseConcMarkSweepGC"
# Install Admin Packages
sudo yum install tomcat-webapps tomcat-admin-webapps 
# Install Online Documentation
sudo yum install tomcat-docs-webapp tomcat-javadoc
# Configure Tomcat Web Management Interface
/usr/share/tomcat/conf/tomcat-users.xml
'''
<tomcat-users>
    <user username="admin" password="password" roles="manager-gui,admin-gui"/>
</tomcat-users>
'''
# Start Tomcat
sudo systemctl start tomcat
# restart Tomcat
sudo systemctl restart tomcat
# Enable Tomcat Service
sudo systemctl enable tomcat

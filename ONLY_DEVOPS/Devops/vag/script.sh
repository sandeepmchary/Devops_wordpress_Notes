sudo apt-get install -y java-1.8.0-openjdk-devel
sudo apt-get install git -y
sudo apt-get install -y wget
sudo apt-get upate
java -version
echo "JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" | sudo tee -a /etc/profile
source /etc/profile

cd /opt
sudo wget http://www-us.apache.org/dist/maven/maven-3/3.5.3/binaries/apache-maven-3.5.3-bin.tar.gz
sudo tar -zxvf apache-maven-3.5.3-bin.tar.gz
sudo ln -s /opt/apache-maven-3.5.3/bin/mvn /usr/bin/mvn
echo 'export PATH=$PATH:/opt/apache-maven/bin' | sudo tee -a /etc/profile
source /etc/profile
mvn --version

cd ~ 
sudo wget -O /etc/apt-get.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo apt-get install -y jenkins
sudo systemctl start jenkins.service
sudo systemctl enable jenkins.service

java -version
java --version
mvn --version
echo $JAVA_HOME
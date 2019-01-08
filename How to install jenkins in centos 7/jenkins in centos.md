#Apache Maven requires Java 1.7 or greater. For this reason, you can install OpenJDK 8 as follows.

#  install wget

sudo yum install -y wget

# Step 1: Install OpenJDK 8

sudo yum install -y java-1.8.0-openjdk-devel

# to check the java version

java -version

# Finally, setup the JAVA_HOME environment variable.

echo "JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" | sudo tee -a /etc/profile

source /etc/profile

# Step 2: Install Apache Maven 3.5

#First, download and extract the Apache Maven 3.5 archive.

cd

wget http://www-eu.apache.org/dist/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz

tar xzf apache-maven-3.5.4-bin.tar.gz

sudo mv ~/apache-maven-3.5.4 /opt

sudo chown -R root:root /opt/apache-maven-3.5.4

sudo ln -s /opt/apache-maven-3.5.4 /opt/apache-maven

echo 'export PATH=$PATH:/opt/apache-maven/bin' | sudo tee -a /etc/profile

source /etc/profile

mvn --version

# Step 3: Install Jenkins

#Use the official YUM repo to install the latest stable version of Jenkins, which is 1.651.2 at the time of writing:

cd ~

sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

sudo yum install -y jenkins

sudo systemctl start jenkins.service

sudo systemctl enable jenkins.service

echo "JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" | sudo tee -a /etc/profile

source /etc/profile
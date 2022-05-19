sudo apt get update
sudo apt install openjdk-8-jdk -y
sudo apt instll maven git unzip wget -y
wget -q -o https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key-add
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins -y

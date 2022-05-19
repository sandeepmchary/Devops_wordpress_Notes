Module 2
Working with docker
- manual installation of docker
- pull latest image of Centos
- Test the Image
- Verify the Image
-----
Class-2
*****
What we learn
* Manual installation of Docker
$ yum install docker-ce,systemctl start docker
* Pull latest image of centos
$ docker pull centos:latest
* Test the image
$ docker run -d --name test_instance centos:latest
* verify the image
$ docker ps -a
------
class-3
- Installing dokcer
- $ yum install -y yum-utils device-mapper-persistent-data lvm2
- $ yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
- $ systemctl start docker

Module 3: Modifying a Docker image
Create Docker file 
- updating centos to most recent
- installing apache httpd webserver ans supporting tools
- start Apache in the background inside the container
* Build the image
* Start the container with new build image
* Validate if container is running
* check container ip
* Browse index page
-- create a docker folder and in this folder create a docker file
********************
FROM centos:latest
RUN yum update -y
RUN yum install -y httpd net tools
RUN echo "Welcome to sam : Managing Docker container with ansible " > /var/www/html/index.html
ENTRYPOINT apachectl "-DFOREGROUND"
*******************
- entrypoint is a command which instructs docker which executable should run when a container is started from the image 
- $ docker build -t centos/apache:v1 .
- $ docker run -d --name apache_web1 -p 8080:80 centos/apache:v1
- $ docker ps -a
-------------------------
class -3
* what we learn
- How to Create Docker file
  - $ vi Dockerfile
- Build the image
 - $ docker build -t centos/apache:v1 .
- Start the container with new build image
 - $ docker run -d --name apahce_web1 -p 8080:80 centos/apache:v1
- Validate if the container is running
 - $ docker ps -a
- check container IP
 - $ docker inspect apache_web1 | grep IPAddress
- Browse Index page
 - $ curl localhost:8080
 - $ curl (containerip):80
  
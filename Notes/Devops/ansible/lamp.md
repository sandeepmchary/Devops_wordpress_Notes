Installation from :
https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04

1. sudo apt-get update
        package update
2. sudo apt-get install apache2
        install apache2
3. sudo systemctl restart apache2
        restart apache2
4. sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql
            install php modules
5. sudo systemctl restart apache2
        restart apache service
6. create a file @ sudo nano /var/www/html/info.php
<?php
phpinfo();
?>

        create a home page


for centos 
sudo yum install httpd
sudo systemctl start hhtpd
sudo yum install php php-mysql
sudo systemctl restart httpd

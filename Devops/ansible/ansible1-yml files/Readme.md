sudo apt-get update
package update
sudo apt-get install apache2 -y
installing apache server
sudo systemctl restart apache2
restart apache service
sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql 
install php modules
sudo systemctl restart apache2
restart apache service
create a file /var/www/html/info.php
'''
<?php
phpinfo();
?>
'''
create a home page
<?php
// find the private ip address  for the local machine
$ip = gethostbyname(trim(`hostname`));
echo "Your IP address is: $ip\n";
// find the public ip address for the local machine
$ip = gethostbyname(trim(`hostname -f`));
echo "Your public IP address is: $ip\n";
//find the hostname for the local machine
$hostname = trim(`hostname`);
echo "Your hostname is: $hostname\n";
// find the domain name for the local machine
$domain = trim(`domainname`);
echo "Your domain name is: $domain\n";
// find the fully qualified domain name for the local machine
$fqdn = trim(`hostname -f`);
echo "Your fully qualified domain name is: $fqdn\n";
// find the operating system for the local machine
$os = trim(`uname -a`);
echo "Your operating system is: $os\n";
// find the kernel version for the local machine
$kernel = trim(`uname -r`);
echo "Your kernel version is: $kernel\n";
// find the uptime for the local machine
$uptime = trim(`uptime`);
echo "Your uptime is: $uptime\n";
// find the load average for the local machine
$load = trim(`uptime | cut -d " " -f 4`);
echo "Your load average is: $load\n";
// find the number of users logged in to the local machine
$users = trim(`who | wc -l`);
echo "There are $users users logged in\n";
// find the number of processes running on the local machine
$processes = trim(`ps -ef | wc -l`);
echo "There are $processes processes running\n";
// find the number of files in the current directory
$files = trim(`ls -l | wc -l`);
echo "There are $files files in the current directory\n";
?>

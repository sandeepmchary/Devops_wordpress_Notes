<pre>
# LOCAL TO REMOTE
scp -i "C:\xxxx\xxxx\xxxx\key.pem" -r chef-repo ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:~
scp -i "C:\xxxx\xxxx\xxxx\key.pem" (folder or file) ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:~

# REMOTE TO LOCAL

scp -i "xxxx.pem" ubuntu@ec2-x.x.x.x.us-east-2.compute.amazonaws.com:/etc/default/tomcat7 .

</pre>
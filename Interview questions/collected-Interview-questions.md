'netstat' is the command to find the port no. of a running applications. 
#netstat -ta (for tcp port)
#netstat -ua (for udp port)
********************
sudo lsof -i:8080 -n

COMMAND  PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
java    1483 tomcat6   36u  IPv6   3496      0t0  TCP *:http-alt (LISTEN)

*******************************'
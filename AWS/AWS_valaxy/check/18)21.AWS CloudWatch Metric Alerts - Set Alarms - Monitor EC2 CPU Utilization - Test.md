<pre>AWS cloud watch alarms
Alarm triggers one or more actions based on the values of the monitored metric
select the running instance 
if we go to the monitoring sessions
copy the instance id 
go to the cloud watch dash board
create alarm
choose Ec2 metrics
paste the instance id there
search for the cpu utlization (here we are checking for the cpu utlization only)
select the cpu utlization
--------------------
Here we are defining the alarm
Name : (any thing)
Description: (any thing)
period for 1 min
statistic: average
whenever :Cpu utlization
above 51 % 
for 3 out of 5 data points
--------------------------------
under actions
state alarm
select notification(select L1 support team)
L1 support team will get email whenever alarm is triggered
-----------------------
top command will show the cpu utlization
to stress the cpu use this command
stress --cpu 10 -v -- timeout 400s
if we do top command again it will show the cpu process
then wait for some time for the alarm to trigger
</pre>

<pre>
AWS CLOUD WATCH EVENTS set rules
CLOUD WATCH EVENTS DELIVERS A NEAR REAL TIME STREAM OF SYSTEM EVENTS
CLOUD WATCH EVENTS <-- 1 --> EC2 INSTANCE <-- 2 --> SNS NOTIFICATIONS
---------------------------------------------------------------------
for suppose we need to notified whenever the state of the instance changed with email
# steps
* cloud watch dash board
* under events
* create rule
-------
* service name: EC2
* EVENT TYPE: EC2 instance state change
* choose any state or specific state
* choose any instance or specific instance
* on the right hand side we have targets
* ADD target
* SNS topic
* Topic: L1-support team or any thing
* configure details
* give name and Description
* state: enabled
* create rule
* when ever instance changes the state we will get email notifications
</pre>

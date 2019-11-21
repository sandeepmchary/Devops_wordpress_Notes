<pre>
# Chef Cheat Sheet

General
*********************
Chef Dry Run
*********************

$ chef-client -Fmin --why-run

List Facts
*********************

$ ohai

Bootstrap Chef client

$ knife bootstrap <FQDN/IP>

Change Chef Run List

$ knife node run_list <add|remove> <node> <cookbook>::<recipe>

Runlist Status

$ knife status --run-list
$ knife status "role:webserver" --run-list

Nodes and Roles
List Node Info

$ knife node show <node>

List Nodes per Role

$ knife search node 'roles:<role name>'

Load role from file

$ knife role from file <file> [<file> [...]]

Data Bags
Load data bag from file

$ knife data bag from file <data bag name> <file>

knife + SSH

$ knife ssh -a ipaddress name:server1 "chef-client"

you can also use patterns:

$ knife ssh -a ipaddress name:www* "uptime"

Debugging
Inheritance

Debugging Attribute Inheritance

*# Invoke chef shell in attribute mode
chef-shell -z
chef > attributes
chef:attributes >

*# Query attributes examples
chef:attributes > default["authorized_keys"]
[...]
chef:attributes > node["packages"]
[...]


</pre>
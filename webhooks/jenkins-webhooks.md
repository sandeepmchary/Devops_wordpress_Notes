$ jenkins --> manage plugins --> available --> github integration --> install without restart
$ jenkins --> GitHub project --> <provide the project url> --> 
under
Source Code Management
-->  Git --> provide Repository URL
Build Triggers
--> GitHub hook trigger for GITScm polling

$ github --> select the repository --> settings --> webhooks --> <jenkins url/github-webhook/> 
## last / is important

$ Content type
application/json

$ save

$ when we commit any changes in the git 
$ a new build starts

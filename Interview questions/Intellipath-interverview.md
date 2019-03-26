<pre>
1)Explain Git Architecture
    - Dev1 --> Commits --> local repo
    - Dev2 --> Commits --> local repo
    - these 2 will to remote repo 
    - pull and push are allowed
    - * But first we need to pull the code from the branch
    
2) In Git how can revert a commit that was already pushed
    - for ex we added some changes to git and pushed to git to revert old one /previous one
    - $ git log
    - check for the latest commit 
    - copy the commit id
    - $ git revert (id just copied)
    - review every thing and save it 
    - then commit will be reverted
    - even before pushing the changes the old one/previous one comes back in the servers
    - to make these changes to remote repository as well 
    - $ git push origin master
3) Have you encounter failed deployment and how you handled them?
    - Best Practice:
                    1) Automate testing code
                    2) use docker for same environment
                    3) use microservices
                    4) overcome risks to avoid failure
                                        # VIRTULIZATION AND CONTAINERIZATION

4) Difference between virtulization and containerization
    - virtulization: host os > hypervisor > guest os > bin/libs > app1/app2
    - containerization : host os > container engine > bin/libs > app1/app2
        --> container engine does not encourage to install whole os, we can do that we will have bare min/.. libraries that are useful to   run  to run the os without kernel
        -- > no kernel
5) without using docker can you see process running inside container form the outside ?
    - yes we can
    - go to the container
    - docker ps
    - docker run -it -d ubuntu
    - docker ps
    - docker exec -it <container id > bash
    - watch -n 1 ls -l
    - comeout of the container
    - ps -aux | grep watch
    
6) what is docker file used for ?
    it is a test document that contains  all the commands a user could call on the command to assemble an image
    EX:
       FROM ubuntu
       RUN apt-get update
       RUN apt-get install apache2 -y
       ADD ./var/www/html
       ENTRYPOINT apachectl -D FOREGROUND
       ENV name Intellpath
    - build now
    - docker build . -t new_dockerfile
    - sudo usermod -aG docker $USER
    - relogin
    - cd dockerfile
    - docker build . -t new_dockerfile
7) Explain container orchestration ?
    - Applications that are typically made of individually containerized components(microservices) that must be organized at the n/w ing  
    level in order for the application to run as intended
    - the process of organizing multiple containers
8) Difference between Docker Swarm and Kubernetes(K8s)
    - both are container orchestration tools
    - Docker Swarm: 
                    > Easy installation
                    > faster than K8s
                    > less features
                    > no auto scaling
    - Kubernetes:
                    > tough to install and run
                    > little complex and deployment are slower
                    > provides auto scaling
                            
                            
                                        # CONTINOUS INTERGRATION
        - it is the stage which connects all the other stages of the devops lifecycle
        - like jenkins which helps us to integrate difference like devops lifecycle stages together so that they woek like organism
9) create a CI/CD pipeline using Git and jenkins to deploy a website on every commit on the main branch?
    - check whether jenkins is running or not 
    - # service jenkins status
    - login to jenkins
    - new item
    - demojob
    - freestyle project
        - Ingeneral
          github project
            project url: (paste project url)
        - source code management
          git (paste git source)
        - Build trigger
          github hook triggers for GITSCN polling
        - Build
          Execute shell
                commands:
                  $sudo docker rm -f $(sudo docker ps -a -q)
                  (push the code to remote repository)
                  $sudo docker build /var/lib/jenkins/workspace/demojob/ -t jenkins
                  $sudo docker run -it -p 87:80 -d jenkins 
                  [save and apply]
        - GITHUB webhook
          setting > webhooks > Add webhook
            under payload url: http://(ip address of the jenkins)/github-webhook
            [Add webhook]
        - push to git
10) Configuration management and continous monitoring
    - Ansible: 
                > Easy to learn as uses python
                > preferred for env/.. designed to scale repidly
                > offers simplified orchestration
                > under developed  GUI with limited features
    - Chef:
                > Ruby based difficult to learn
                > Intial setup is complicated
                > very stable,reliable and mature
                > configuration management of the most flexible solution for os and middleware management
                > first configuration management to comeout
    - puppet: 
                > uses puppet DSL, difficult to learn
                > Intial setup is smooth and supports different os's
                > storng compliance automation and reporting tools
                > not suitable for scaling deployment
11) Asset management and configuration management?
    -Asset management: 
                        > how to accumaltely manages the resources that allow IT to working more efficently
    - configuration management: 
                                > s/w related quires done here
                                > Installing right s/w on the right system with which particular workload is going to run
12) what are NRPE plugins in nagios?
    - These are extensions to nagios helps us to monitor local resources of the client machines

13) Active checks and passive checks in nagios ?
    Active Checks:
                    > The data the monitoring log that are getting from the your client if it is being delivered by an nagios agent
    passive Checks:
                    > Rather than nagios the s/w component pushes the logs to nagios master the logs that defined by some other s/w.
                    
14) create a anisble playbook to deploy apache on the client server?
    ---
    - hosts: all
      become: yes
      tasks:
      - name: Install apache2
        apt:
          name: apache2
          update_cache: yes
          state: latest
15) continous testing:
                        selenium : only for web application
    
    
</pre>
<Pre>
1)explain git architecture
    - dev1 --> commits --> local repo
    - dev2 --> commits --> local repo
    - these 2 will to remote repo 
    - pull and push are allowed
    - * but first we need to pull the code from the branch
    
2) In git how can revert a commit that was already pushed
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
3) have you encounter failed deployment and how you handled them?
    - Best practice:
                    1) automate testing code
                    2) use docker for same environment
                    3) use microservices
                    4) overcome risks to avoid failure
                                        # virtulization and containerization

4) Difference between virtulization and containerization
    - virtulization: host os > hypervisor > guest os > bin/libs > app1/app2
    - containerization : host os > container engine > bin/libs > app1/app2
        --> container engine does not encourage to install whole os, we can do that we will have bare min/.. Libraries that are useful to   run  to run the os without kernel
        -- > no kernel
5) without using docker can you see process running inside container form the outside ?
    - Yes we can
    - go to the container
    - docker ps
    - docker run -it -d ubuntu
    - docker ps
    - docker exec -it <container id > bash
    - watch -n 1 ls -l
    - comeout of the container
    - ps -aux | grep watch
    
6) What is docker file used for ?
    It is a test document that contains  all the commands a user could call on the command to assemble an image
    ex:
       from ubuntu
       run apt-get update
       run apt-get install apache2 -y
       add ./Var/www/html
       entrypoint apachectl -d foreground
       env name intellpath
    - build now
    - docker build . -T new_dockerfile
    - sudo usermod -ag docker $user
    - relogin
    - cd dockerfile
    - docker build . -T new_dockerfile
7) explain container orchestration ?
    - Applications that are typically made of individually containerized components(microservices) that must be organized at the n/w ing  
    level in order for the application to run as intended
    - the process of organizing multiple containers
8) difference between docker swarm and kubernetes(k8s)
    - both are container orchestration tools
    - docker swarm: 
                    > easy installation
                    > faster than k8s
                    > less features
                    > no auto scaling
    - kubernetes:
                    > tough to install and run
                    > little complex and deployment are slower
                    > provides auto scaling
                            
                            
                                        # Continous intergration
        - it is the stage which connects all the other stages of the devops lifecycle
        - like jenkins which helps us to integrate difference like devops lifecycle stages together so that they woek like organism
9) create a ci/cd pipeline using git and jenkins to deploy a website on every commit on the main branch?
    - Check whether jenkins is running or not 
    - # service jenkins status
    - login to jenkins
    - new item
    - demojob
    - freestyle project
        - ingeneral
          github project
            project url: (paste project url)
        - source code management
          git (paste git source)
        - build trigger
          github hook triggers for gitscn polling
        - build
          execute shell
                commands:
                  $sudo docker rm -f $(sudo docker ps -a -q)
                  (push the code to remote repository)
                  $sudo docker build /var/lib/jenkins/workspace/demojob/ -t jenkins
                  $sudo docker run -it -p 87:80 -d jenkins 
                  [save and apply]
        - github webhook
          setting > webhooks > add webhook
            under payload url: http://(ip address of the jenkins)/github-webhook
            [add webhook]
        - push to git
10) configuration management and continous monitoring
    - ansible: 
                > easy to learn as uses python
                > preferred for env/.. Designed to scale repidly
                > offers simplified orchestration
                > under developed  gui with limited features
    - chef:
                > ruby based difficult to learn
                > intial setup is complicated
                > very stable,reliable and mature
                > configuration management of the most flexible solution for os and middleware management
                > first configuration management to comeout
    - puppet: 
                > uses puppet dsl, difficult to learn
                > intial setup is smooth and supports different os's
                > storng compliance automation and reporting tools
                > not suitable for scaling deployment
11) asset management and configuration management?
    -Asset management: 
                        > how to accumaltely manages the resources that allow it to working more efficently
    - configuration management: 
                                > s/w related quires done here
                                > installing right s/w on the right system with which particular workload is going to run
12) what are nrpe plugins in nagios?
    - These are extensions to nagios helps us to monitor local resources of the client machines

13) Active checks and passive checks in nagios ?
    Active checks:
                    > the data the monitoring log that are getting from the your client if it is being delivered by an nagios agent
    passive checks:
                    > rather than nagios the s/w component pushes the logs to nagios master the logs that defined by some other s/w.
                    
14) Create a anisble playbook to deploy apache on the client server?
    ---
    - hosts: all
      become: yes
      tasks:
      - name: install apache2
        apt:
          name: apache2
          update_cache: yes
          state: latest
15) continous testing:
                        selenium : only for web application
    
    
</Pre>
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
        
    
    
    
    
    
</pre>
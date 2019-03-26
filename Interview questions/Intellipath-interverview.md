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
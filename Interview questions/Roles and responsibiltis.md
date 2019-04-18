    <pre>
    release process:
    - core banking :1.0
    - 10 features , add these to above
    - within 3 months
    jan---------|mar(2.0)|---------||----- ||
                 releaseed 2.0      3.0     4.0
    - release types
    1) Major release: 3-6 months --features development
    2) minor release: 2 weeks --- 3 months -- features development
    3) Hotfix release: 1 day --- 2 weeks    -- bug fix
    - Release Versions - x.x.x.x
    1.0.0.0
    1 - Major
    0 - minor
    0 - hotfix
    0 - this is for build no.
    - jan---------|mar(1.1.0)|---------|(2.0.0)|----- |2.0.1|---|(2.0.2)| --- |(2.1.0)|
                                6 months                     hotfix 
    - fourth digit called as build no. used in for only internal purpose, for testing and quality assurance
    ------------------
    svn/git: release-1.0.1
    ----------------------
    VCS:
        version control services
                FOR DEV TEAM
                --------------
        - create a branch/tag for new release (1.0.0) or (2.0.0){once in 3 months or 15 days}
        - Request to create user accounts
        - reset password
        
                    FOR OPS TEAM
                    --------------
        - Administration of vcs (svn/git)
        - backups
        - rollbacks
        - hooks
        - upgrades
    ---------------------------------------------------------------------------------------------------------------------
    -> how do we get requests
    1) Email to your groups(small organization)
    2) Ticketing system (jira,remedy)
    ---------------------------------------------------------------------------------------------------------------------
                                            # CONTINOUS INTEGRATION
                                              ---------------------
    - create CI job for new release (nightly/hourly)
    - create a manual job in CI tools(manual)
    - Accounts for developers
    - Administration
      - backups
      - plugins
      - 3rd party tools integration(selenium)
    - monitor CI jobs (manual), check the nightly builds, it's our responsibility for send mail to respected developers team
    - if it fails on the second day send mail to manager
    ---------------------------------------------------------------------------------------------------------------------
    - above are the minor responsibilties
    ---------------------------------------------------------------------------------------------------------------------
    - Actual responsibilties are builds
    -> QA/Release builds:
     ---------------------
                        - Release/Delivary/Project manager coordinated b/w all the teams and release project
                        - This guy work coordinates with all  teams DEV,QA,OPS and get data and assigned tasks
    -> QA build: day by day (mon & thursday)
       ---------
    -> performance build: wednesday
    -> UAT builds: 1.5 months and 1.5 months (twice)
    - above are the teams we need to 
***********************************************************************************************************************                    
12 am-3 pm	|positive	        |negative
------------------------------------------------------------------
12	        |svn/git checkout	|svn maybe down/svn access issues
------------------------------------------------------------------
15 min	    |waiting	        |   waiting
------------------------------------------------------------------
12:15	    |svn/git checkout	
------------------------------------------------------------------
1 hour	    |ant/mvn	compile |    errors - report developers
------------------------------------------------------------------
1:15	    |stopping services	|server down -- n/w team
------------------------------------------------------------------
15 min	    |waiting	        |    waiting
------------------------------------------------------------------
1:30	    |backup	            |server disk 100% full
------------------------------------------------------------------
15 min	    |waiting	        |    waiting
------------------------------------------------------------------
1:45	    |Deploy	            |disk full,read only file-system,permission issues
----------------------------------------------------------------------------------
30 min	    |waiting	        |    waiting
------------------------------------------------------------------
2:15	    |Localiation	    |    mostly no issues
------------------------------------------------------------------
15 min	    |waiting	        |    waiting
------------------------------------------------------------------
2:30	    |start	            |if services is ready started or started with root users
------------------------------------------------------------------
15 min	    |waiting	        |    waiting
------------------------------------------------------------------
2:45	    |Smoke Test	        |errors, go back to devlopers
------------------------------------------------------------------
15 min	    |waiting	        |    Waiting
------------------------------------------------------------------
3:00	    |Report email	
------------------------------------------------------------------

- trail this before
- reasons for the build delivery
- compile failed , dev team fixed
- servers unreachable, n/w team will fix this
- 
-Ex:
--- 10 servers - QA
--- 5 servers - performance
--- 2 servers - UAT

-------------------
pre build check list
- ex: At 11:30 we will circulate a email plz dont touch VCS
- mock builds: 11 am mock build, lock the branch at 11 am

---------------------------------------------------------------------------------------------------------------------
3) N/W issues: 
server verfication scripts
at 11:00 am
- ping
- disk Free space available at least 80%
- Service not running with root 
- software versions like JDK version my SQL 
- stop services
- 90% of issues will be sorted out 
Assume we have 4 people 
- 1-- QA 
- 2 -- performance 
- 3 -- UAT 
- 4 -- vcs and CI and CD 
- in the middle time we will automate the process 
- could you please tell me a great achievement in your company like which is not already there 
---- release the build, and give it to QA, start at 4:00 p.m. And at the 5:00 p.m. Environment is down, QA will send a email to build team at 5:00 p.m. Built team  look at that at 6:00 p.m., respond at 7:00 p.m. 
- 2 hours of QA Ideal to avoid this 
- write a script to avoid this 
- it should start automatically 
----------------------------------------------------- 
in the ideal time we explore new tools 
- POC of new tool 
- try with one application
- benefits of tools quality,time ,reporting ,feature 
- in 3.0 version we use jenkins/teamcity if the release is successful(100%) 
- in 4.0 version they can roleout Teamcity 
------------------------------------------------------------------- 
I am working in tech Mahindra company for 3.6 years as a devops engineer 
- when comes to my roles as a part of devops team working in the organisation 
- we handle enter application build and release Management process 
- for every release it will keep changing 
- taking responsibility of version control system 
- implementing the branching strategy 
- implementing the access control on the VCS, and CI systems it our  responsibility to implement the CI across the project in the account 
- as a part of it we use tools like jenkins 
- when comes to deployment part  we use ansible as deployment tool 
- we write all the ansible Playbooks 
- we check into git repository 
- we follow different release cycles like waterfall and V model 
- We have different types of releases each releases handled by one team member of our team 
- I deal with QA builds in our organisation QA builds are done Monday and Thursday
- Buils will take in 12-3pm, i do builds manually before ansible came in picture , we automates the builds, we use ansible to do the deployment


    </pre>
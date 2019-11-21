<pre>

1) sudo yum install wget -y
2) wget https://packages.chef.io/files/stable/chef-server/12.19.31/el/7/chef-server-core-12.19.31-1.el7.x86_64.rpm
3) rp -ivh chef*.rpm
4) sudo chef-server-ctl reconfigure
5) sudo chef-server-ctl user-create devopsjan Devops Jan devops.jan@gmail.com devops123 --filename /home/centos/devops.pem ##admin user
6) sudo chef-server-ctl org-create devops-jan "DevopsTraining software Inc" --association_user devopsjan --filename /home/centos/devops-validator.pem
7) sudo yum udpate
8) https://packages.chef.io/files/stable/chef-manage/2.2.0/el/6/chef-manage-2.2.0-1.el6.x86_64.rpm and install it rpm -ivh chef-manage-2.2.0-1.el6.x86_64.rpm
9) sudo chef-manage-ctl reconfigure
10) take the public ip of this instance paste it on the browser
11) login with the userid and password given

----------------------------------------------------------------------------------------------------------
                    WORKSTATION

1) install sdk chefdk in here
2) wget https://packages.chef.io/files/stable/chefdk/1.5.0/el/7/chefdk-1.5.0-1.el7.x86_64.rpm
3) rpm -ivh chef*.rpm
4) copy the chef-starter.zip into workstation
5) ** get the key from the chef server at below location and copy to chef-repo/.chef/trusted-certs
6) create a file trusted-certs $ touch /home/centos/chef-repo/.chef/trusted-certs
7) knife ssl check
8) find this file on the SERVER /var/opt/opscode/nginx/ca
9) send the .pem file to SERVER and change to readonly mode $ chmod 400 xxxx.pem
10) mkdir -p /home/centos/chef-repo/.chef/trusted_certs
11) from home directory to /home/centos/chef-repo/.chef/trusted_certs/ $cp chef.mycompany.com.crt /home/centos/chef-repo/.chef/trusted_certs/
12) knife ssl check
knife ssh fetch
knife client lsit
13) mkdir recipes
14) vi hello.rb
file 'uuu.txt' do
    content ' .....'
end
15) chef-apply hello.rb
</pre>
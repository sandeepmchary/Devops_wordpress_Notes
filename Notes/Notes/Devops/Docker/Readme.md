<pre>
# First, install the required packages.
yum -y install lvm2 device-mapper device-mapper-persistent-data device-mapper-event device-mapper-libs device-mapper-event-libs
{
    # First, install the required packages
    package:
      name: "{{ item}}"
      state: present
    with_items:
      - lvm2
      - device-mapper
      - device-mapper-persistent-data
      - device-mapper-event
      - device-mapper-libs
      - device-mapper-event-libs
      - wget
}
# yum  -y remove  docker-common docker container-selinux docker-selinux docker-engine
{
    # # Uninstall older versions of Dockers
    package:
      name: "{{ item }}"
      state: absent
    with_items:
    - docker-common
    - docker
    - container-selinux
    - docker-selinux
    - docker-engine
}

#  Configuring docker-ce repo
   wget https://download.docker.com/linux/centos/docker-ce.repo -O /etc/yum.repos.d/docker-ce.repo
   {
       - name: Configure docker-ce repo
         get_url:
           url: https://download.docker.com/linux/centos/docker-ce.repo
           dest: /etc/yum.repos.d/docker-ce.repo
   }
#  Install docker latest version
    yum -y install docker-ce
    {
        - name: Install docker latest version
          package:
            name: docker-ce
            state: present
    }
# systemctl start docker

# systemctl enable docker
    {
        - name: Enable and start docker
          service:
            name:docker
            state: started
            enabled: yes
            
    }
</pre>
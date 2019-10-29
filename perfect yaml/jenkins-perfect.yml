---
- hosts: all
  become: yes
  vars:
    req_java_version : java-1.8.0-openjdk-devel
    ALTERNATIVES: /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.232.b09-0.el8_0.x86_64
  tasks:
    - name: Install Java
      yum:
        name: "{{ req_java_version }}"
        state: present
    - name: Correct the alternatives to change default Java version.
      alternatives:
        name: Java
        link: /bin/java
        path: "{{ ALTERNATIVES }}"
    - name: download jenkins repo
      get_url:
        url: http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
        dest: /etc/yum.repos.d/jenkins.repo
    - name: import jenkins key
      rpm_key:
        state: present
        key: https://jenkins-ci.org/redhat/jenkins-ci.org.key
    - name: Install jenkins
      yum:
        name: jenkins
        state: present
    - name: Start jenkins
      service:
        name: jenkins
        state: started
        enabled: yes
    -                  
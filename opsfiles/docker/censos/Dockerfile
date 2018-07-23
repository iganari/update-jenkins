FROM iganarix/base-centos-7

MAINTAINER iganari

### ADD Jenkins PATH
RUN mkdir -p /usr/lib/jenkins

### make dummyfile
RUN touch           /usr/lib/jenkins/jenkins.war &&\
    chown root.root /usr/lib/jenkins/jenkins.war &&\
    chmod 0644      /usr/lib/jenkins/jenkins.war

### install package
RUN yum install -y \
                wget


### cppy BASH_RC
# ADD _bashrc /root/.bashrc

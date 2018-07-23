FROM iganarix/base-ubuntu-16.04

MAINTAINER iganari

# ### apt-get
# RUN apt-get update
# RUN apt-get install -y vim python-pip
 

### ADD Jenkins PATH
RUN mkdir -p /usr/share/jenkins

### make dummyfile
RUN touch           /usr/share/jenkins/jenkins.war &&\
    chown root.root /usr/share/jenkins/jenkins.war &&\
    chmod 0644      /usr/share/jenkins/jenkins.war


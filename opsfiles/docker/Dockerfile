# FROM jenkins:2.60.3
FROM python:3.6.2-stretch

MAINTAINER iganari

### setting jp
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale
RUN rm -rfv /etc/localtime &&\
    ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime 

### apt-get
RUN apt-get update
RUN apt-get install -y vim python-pip
 
### install pip
RUN pip install --upgrade pip
# RUN pip install --upgrade pip &&\
#     pip install ipython

### ADD Jenkins PATH
RUN mkdir -p /usr/lib/jenkins
### make dummyfile
RUN touch           /usr/lib/jenkins/jenkins.war &&\
    chown root.root /usr/lib/jenkins/jenkins.war &&\
    chmod 0644      /usr/lib/jenkins/jenkins.war

# 
# # ADD _vimrc  /root/.vimrc
# # ADD _bashrc /root/.bashrc

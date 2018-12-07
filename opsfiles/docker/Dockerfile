ARG _TAG='3.7.1-alpine3.8'
FROM python:${_TAG}
# https://hub.docker.com/_/python/

MAINTAINER iganari

### setting jp
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale
RUN rm -rfv /etc/localtime &&\
    ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime 

### apt-get
RUN apt-get update
RUN apt-get install -y vim python-pip
 
### install pip
# RUN pip install --upgrade pip
RUN pip install --upgrade pip &&\
    pip install ipython

### ADD Jenkins PATH
RUN mkdir -p /usr/lib/jenkins
### make dummyfile
RUN touch           /usr/lib/jenkins/jenkins.war &&\
    chown root.root /usr/lib/jenkins/jenkins.war &&\
    chmod 0644      /usr/lib/jenkins/jenkins.war

# ### Temp pip install
# RUN pip install requests \
#                 feedparser

### cppy BASH_RC
ADD _bashrc /root/.bashrc

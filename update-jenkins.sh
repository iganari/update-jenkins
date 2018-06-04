#!/bin/bash

# set -xeu
set -x

## $1 でverを入れさせる
## ex 2.89.4

check_arg()
{
  if [ "$1" = "" ]; then
      echo "no argument"
      ### latest
      _VER=`curl http://updates.jenkins-ci.org/download/war/index.html | grep jenkins.war | grep download | head -n1 | awk -F\/ '{print $10}'`
  
  elif [ "$1" = "latest" ]; then
      echo "$1"
      ### latest
      _VER=`curl http://updates.jenkins-ci.org/download/war/index.html | grep jenkins.war | grep download | head -n1 | awk -F\/ '{print $10}'`
  
  elif [ "$1" = "lts" ]; then
      echo "$1"
      ### get LTS version
      _VER=`curl https://jenkins.io/changelog-stable/rss.xml | grep '<title>Jenkins' | cut -c8- | cut -d\< -f1 | cut -d\  -f2 | head -n1`
  
  else
      _VER=$1
  fi
}


#     expr $1 + 1 > /dev/null 2>&1
#     if [ $? -lt 2 ] ; then
#         # 数値
#         echo "number."
#         _VER=$1
#     else
#         echo "not number."
#         exit 1
#     fi

_J_DIR='/usr/lib/jenkins'

check_os()
{
    # When CentOS
    _J_DIR='/usr/lib/jenkins'
    # When Other
    # WIP
}

replace_jenkins_warfile()
{
  unlink                              ${_J_DIR}/jenkins.war
  ln -s ${_J_DIR}/${_VER}/jenkins.war ${_J_DIR}/jenkins.war 
}

restart_jenkins_process()
{
  systemctl stop   jenkins &&\
  systemctl start  jenkins &&\
  systemctl status jenkins
}

# echo $_VER
check_arg $1
mkdir ${_J_DIR}/${_VER}
wget http://updates.jenkins-ci.org/download/war/${_VER}/jenkins.war -O ${_J_DIR}/${_VER}/jenkins.war

replace_jenkins_warfile
# restart_jenkins_process

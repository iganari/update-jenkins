#!/bin/bash

# For Example
# sh update-jenkins.sh lts
# sh update-jenkins.sh latst


# set -xeu
set -x

url_latest='http://updates.jenkins-ci.org/download/war/index.html'
url_lts='https://jenkins.io/changelog-stable/rss.xml'

check_arg()
{
  ## sh update-jenkins.sh version -y の形しか許さない

  if [ "$1" = "" ]; then
    echo "Usage: $(basename $0) {lts|latest}"
    exit 1

  elif [ "$1" = "-f" ]; then
    echo "Usage: $(basename $0) {lts|latest}"
    exit 1

  elif [ "$1" = "latest" ]; then
    echo "$1"
    ### latest
    _VER=`curl ${url_latest} | grep jenkins.war | grep download | head -n1 | awk -F\/ '{print $10}'`
    if [ "$2" = "" ];then
      _FORCE_FRAG='false'  
    elif [ "$2" = "-y" ];then
      _FORCE_FRAG='true'
    else
      echo 'bad arg'
      exit 0
    fi

  elif [ "$1" = "lts" ]; then
    echo "$1"
    ### get LTS version
    _VER=`curl ${url_lts} | grep '<title>Jenkins' | cut -c8- | cut -d\< -f1 | cut -d\  -f2 | head -n1`
    if [ "$2" = "" ];then
      _FORCE_FRAG='false'  
    elif [ "$2" = "-y" ];then
      _FORCE_FRAG='true'
    else
      echo 'bad arg'
      exit 0
    fi
  
  else
    echo 'bad arg'
    exit 0
  fi
}



check_jenkins_path()
{
  echo helloworld
  if [ -e '/etc/redhat-release' ];then
    if [ `cat /etc/redhat-release | awk '{print $1}'` = 'CentOS' ];then
      echo 'centos'
      _J_DIR='/usr/lib/jenkins'
    else
      echo 'no idea'
    fi
  elif [ -e '/etc/lsb-release' ];then
    if [ `cat /etc/lsb-release | awk -F\= 'NR==1 {print $2}'` = 'Ubuntu' ];then
      echo 'ubuntu'
      _J_DIR='/usr/share/jenkins'
    else
      echo 'no idea'
    fi
  else
    echo 'no idea'
  fi
}

replace_jenkins_warfile()
{
  unlink                              ${_J_DIR}/jenkins.war
  ln -s ${_J_DIR}/${_VER}/jenkins.war ${_J_DIR}/jenkins.war 
}

restart_jenkins_process()
{

  # _FORCE_FRAG='true'
  if [ "${_FORCE_FRAG}" = "true" ];then
    systemctl stop   jenkins &&\
    systemctl start  jenkins &&\
    systemctl status jenkins
  elif [ "$_FORCE_FRAG" = "false" ];then
    echo "force push ?? [y/N]"
    read ans
    if [ "${ans}" = "y" ];then
      systemctl stop   jenkins &&\
      systemctl start  jenkins &&\
      systemctl status jenkins
    elif [ "${ans}" = "N" ];then
      echo 'pass'
      :
    else
      :
    fi
  else
    echo "bad request"
    :
  fi
}


# Main
check_arg $1 $2
check_jenkins_path
mkdir ${_J_DIR}/${_VER}
wget http://updates.jenkins-ci.org/download/war/${_VER}/jenkins.war -O ${_J_DIR}/${_VER}/jenkins.war

replace_jenkins_warfile
restart_jenkins_process

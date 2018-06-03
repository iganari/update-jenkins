#!/bin/bash

# set -xeu
set -x

## $1 でverを入れさせる
## ex 2.89.4

if [ "$1" = "" ]; then
    echo "no argument"
    ## latest
    _VER=`curl http://updates.jenkins-ci.org/download/war/index.html | grep jenkins.war | grep download | head -n1 | awk -F\/ '{print $10}'`

elif [ "$1" = "latest" ];then
    echo "latest"
    ## latest
    _VER=`curl http://updates.jenkins-ci.org/download/war/index.html | grep jenkins.war | grep download | head -n1 | awk -F\/ '{print $10}'`
else
    _VER=$1

#     expr $1 + 1 > /dev/null 2>&1
#     if [ $? -lt 2 ] ; then
#         # 数値
#         echo "number."
#         _VER=$1
#     else
#         echo "not number."
#         exit 1
#     fi
fi

_JDIR='/usr/lib/jenkins'

# echo $_VER

mkdir ${_VER}
wget http://updates.jenkins-ci.org/download/war/${_VER}/jenkins.war -O ${_VER}/jenkins.war

unlink ${_JDIR}/jenkins.war
ln -s ${_JDIR}/${_VER}/jenkins.war ${_JDIR}/jenkins.war
systemctl stop jenkins && systemctl start jenkins

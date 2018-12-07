#!/bin/bash

set -x
# set -xeu

_TAG='update-jenkins'
BASEPATH=$(cd ../../`dirname $0`; pwd)

docker build . -t ${_TAG}

docker rm -f ${_TAG}
docker run --rm \
           -it \
           -v ${BASEPATH}:/usr/local/hejda \
           -w /usr/local/hejda \
           --name ${_TAG} \
           ${_TAG} \
           /bin/bash

#!/bin/bash

set -x

BASEPATH=$(cd ../../`dirname $0`; pwd)
docker rm -f ${1}
docker run --rm \
           -it \
           -v ${BASEPATH}:/usr/local/hejda \
           -w /usr/local/hejda \
           --name ${1} ${1} \
           /bin/bash

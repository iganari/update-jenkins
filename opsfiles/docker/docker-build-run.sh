#!/bin/bash

set -xeu

_TAG='update-jenkins'

docker build . -t ${_TAG}

sh ./docker-run.sh ${_TAG}

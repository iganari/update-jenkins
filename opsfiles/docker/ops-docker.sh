#!/bin/bash

# set -x

# See how we were called
# ref: https://github.com/apache/httpd/blob/trunk/build/rpm/httpd.init
case "${1}" in
    start)
        echo "docker-compose up"
        docker-compose up -d
        ;;
    stop)
        echo "docker-compose stop"
        docker-compose stop
        ;;
    down)
        echo "docker-compose down"
        docker-compose down
        ;;
  status)
        echo "docker-compose status"
        docker-compose ps
        ;;
    *)
        echo "Usage: $(basename $0) {start|stop|down|status}"
        exit 1
esac

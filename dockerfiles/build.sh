#!/bin/bash

[ -n "${1}" ] && DOCKER_REGISTRY="${1%%/*}/"

#DOCKER_BUILD_LIST=`cat build.list`
DOCKER_BUILD_LIST=`grep -vE '\s*#|^\s*$' build.list`

for LINE in ${DOCKER_BUILD_LIST}
do

  FROM_IMAGE=`echo ${LINE} | awk -F',' '{print $1}'`
  TO_IMAGE=`echo ${LINE} | awk -F',' '{print $2}'`
  DOCKERFILE_FILE=`echo ${LINE} | awk -F',' '{print $3}'`
  DOCKERFILE_PATH=${DOCKERFILE_FILE%/*}

  if [ 'scratch' != "${FROM_IMAGE}" ]
  then
    docker pull ${DOCKER_REGISTRY}${TO_IMAGE} || echo "${DOCKER_REGISTRY}${TO_IMAGE} not found!"
    sed -i '/^FROM/d' ${DOCKERFILE_FILE}
    sed -i "1iFROM ${DOCKER_REGISTRY}${FROM_IMAGE}" ${DOCKERFILE_FILE}
    docker build --no-cache --rm -m 2G -t ${DOCKER_REGISTRY}${TO_IMAGE} -f ${DOCKERFILE_FILE} ${DOCKERFILE_PATH}
    docker push ${DOCKER_REGISTRY}${TO_IMAGE}
  else
    docker pull ${DOCKER_REGISTRY}${TO_IMAGE} || echo "${DOCKER_REGISTRY}${TO_IMAGE} not found!"
    sed -i '/^FROM/d' ${DOCKERFILE_FILE}
    sed -i "1iFROM ${FROM_IMAGE}" ${DOCKERFILE_FILE}
    docker build --rm -m 2G -t ${DOCKER_REGISTRY}${TO_IMAGE} -f ${DOCKERFILE_FILE} ${DOCKERFILE_PATH}
    docker push ${DOCKER_REGISTRY}${TO_IMAGE}
  fi 

done

#!/bin/bash

## Prepare BuildInfo file

# GIT_COMMIT is typically set by Jenkins. If they are missing
# we will try to find them from the current git branch and logs
VERSION=${GIT_COMMIT}
BRANCH=`git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`
if [ -z ${VERSION} ]; then
  VERSION=`git log | head -1 | cut -f 2 -d " " 2> /dev/null`
fi

# Create a version.json file that will be used by buildInfo resource
TIME=`date "+%Y-%m-%dT%H:%M:%S"`

echo { "\""branch"\"":"\""${BRANCH}"\"", "\""version"\"":"\""${VERSION}"\"", "\""buildTime"\"":"\""${TIME}"\""} > app/version.json

# Create Virtual Env and install requirements (Make sure you use python 3.5.x)
virtualenv env
env/bin/pip install --upgrade pip
cd app/
../env/bin/pip install -r requirements.txt

## Run the tests ##
../env/bin/python -m unittest discover -p "*_test.py"
ret=$?
cd ..
exit $ret
